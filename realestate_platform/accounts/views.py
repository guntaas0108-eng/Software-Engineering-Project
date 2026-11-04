from functools import wraps
from decimal import Decimal
from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum, Count, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from properties.models import Property
from payments.models import Payment
from chat.models import Conversation, Appointment
from .models import UserProfile

User = get_user_model()


def platform_admin_required(view_func):
    """Restricts access exclusively to platform administrators (staff, superuser, or ADMIN role)."""
    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        if not (request.user.is_authenticated and (
            request.user.is_staff
            or request.user.is_superuser
            or (hasattr(request.user, "profile") and request.user.profile.role == UserProfile.Role.ADMIN)
        )):
            messages.error(request, "Access Restricted: Sovereign Command Center is reserved exclusively for Platform Administrators.")
            return redirect("home")
        return view_func(request, *args, **kwargs)
    return _wrapped


def signup(request):
    """Accredited user registration."""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Assign requested role if provided, otherwise default to BUYER
            role = request.POST.get("role", UserProfile.Role.BUYER)
            if role in [UserProfile.Role.BUYER, UserProfile.Role.SELLER]:
                profile, _ = UserProfile.objects.get_or_create(user=user)
                profile.role = role
                profile.save()
            login(request, user)
            return redirect("property_list")
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})


# ==============================================================================
# PLATFORM ADMINISTRATOR COMMAND CENTER (Staff / Superuser Only)
# ==============================================================================

@platform_admin_required
def platform_admin_dashboard(request):
    """
    Sovereign Administrator Command Center:
    Supervises platform health, flagged duplicate listings, escrow custody holds,
    and bilateral dispute resolution.
    """
    all_properties = Property.objects.select_related("seller").prefetch_related("images").order_by("-created_at")
    total_asset_value = sum(p.listed_price for p in all_properties)
    
    payments = Payment.objects.select_related("estate", "buyer").order_by("-created_at")
    escrow_held_paise = payments.filter(status=Payment.Status.PAID).aggregate(s=Sum("amount_paise"))["s"] or 0
    escrow_held_rupees = Decimal(escrow_held_paise) / Decimal(100)

    # Problems and Issues needing admin intervention
    flagged_duplicates = Property.objects.filter(possible_duplicate_of__isnull=False).select_related("seller", "possible_duplicate_of")
    in_dispute_payments = payments.filter(status__in=[Payment.Status.CREATED, Payment.Status.FAILED])

    all_users = User.objects.select_related("profile").order_by("-date_joined")
    buyers_count = UserProfile.objects.filter(role=UserProfile.Role.BUYER).count()
    sellers_count = UserProfile.objects.filter(role=UserProfile.Role.SELLER).count()

    context = {
        "all_properties": all_properties[:25],
        "total_properties": all_properties.count(),
        "total_asset_value": total_asset_value,
        "payments": payments[:25],
        "escrow_held_rupees": escrow_held_rupees,
        "flagged_duplicates": flagged_duplicates,
        "in_dispute_payments": in_dispute_payments,
        "all_users": all_users[:25],
        "total_users": all_users.count(),
        "buyers_count": buyers_count,
        "sellers_count": sellers_count,
        "total_conversations": Conversation.objects.count(),
        "total_appointments": Appointment.objects.count(),
    }
    return render(request, "accounts/admin_dashboard.html", context)


@platform_admin_required
def admin_resolve_duplicate(request, pk, action):
    """Admin tool to resolve AI duplicate detection flags."""
    property_obj = get_object_or_404(Property, pk=pk)
    if request.method == "POST":
        if action == "dismiss":
            property_obj.possible_duplicate_of = None
            property_obj.save(update_fields=["possible_duplicate_of"])
            messages.success(request, f"Flag cleared: '{property_obj.title}' approved as authentic and unique.")
        elif action == "deactivate":
            property_obj.status = Property.Status.INACTIVE
            property_obj.save(update_fields=["status"])
            messages.warning(request, f"Duplicate de-listed: '{property_obj.title}' set to Inactive status.")
        elif action == "delete":
            title = property_obj.title
            property_obj.delete()
            messages.error(request, f"Duplicate permanently expunged: '{title}'.")
    return redirect("platform_admin")


@platform_admin_required
def admin_moderate_payment(request, pk, action):
    """Admin tool to manage escrow custody disputes, release funds, or execute refunds."""
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == "POST":
        if action == "refund":
            payment.status = Payment.Status.REFUNDED
            payment.notes += f" | Admin dispute refund authorized by {request.user.username} on {timezone.now()}."
            payment.save(update_fields=["status", "notes", "updated_at"])
            messages.info(request, f"Escrow Refund Executed: ₹{payment.amount_rupees:,.0f} returned to {payment.buyer.username}.")
        elif action == "release":
            payment.status = Payment.Status.PAID
            payment.notes += f" | Escrow cleared & disbursed to seller by Admin {request.user.username} on {timezone.now()}."
            payment.save(update_fields=["status", "notes", "updated_at"])
            messages.success(request, f"Escrow Disbursed: ₹{payment.amount_rupees:,.0f} released.")
    return redirect("platform_admin")


@platform_admin_required
def admin_toggle_verification(request, user_id):
    """Admin tool to toggle verified KYC / Gold accreditation seal on user accounts."""
    target_user = get_object_or_404(User, pk=user_id)
    profile, _ = UserProfile.objects.get_or_create(user=target_user)
    profile.is_verified = not profile.is_verified
    profile.save(update_fields=["is_verified"])
    status_label = "Verified" if profile.is_verified else "Unverified"
    messages.success(request, f"User {target_user.username} status updated to: {status_label}.")
    return redirect("platform_admin")


@platform_admin_required
def admin_toggle_property_status(request, pk):
    """Admin tool to toggle listing active / suspended state."""
    prop = get_object_or_404(Property, pk=pk)
    if prop.status == Property.Status.ACTIVE:
        prop.status = Property.Status.INACTIVE
        messages.warning(request, f"Estate '{prop.title}' has been suspended / unlisted.")
    else:
        prop.status = Property.Status.ACTIVE
        messages.success(request, f"Estate '{prop.title}' has been reinstated to Active marketplace.")
    prop.save(update_fields=["status"])
    return redirect("platform_admin")


@platform_admin_required
def admin_toggle_user_status(request, user_id):
    """Admin tool to suspend/ban or reactivate a platform account."""
    target_user = get_object_or_404(User, pk=user_id)
    if target_user.is_superuser:
        messages.error(request, "Cannot suspend root superuser.")
        return redirect("platform_admin")
    target_user.is_active = not target_user.is_active
    target_user.save(update_fields=["is_active"])
    state = "Active & In Good Standing" if target_user.is_active else "Suspended & Access Revoked"
    messages.info(request, f"Account {target_user.username} is now: {state}.")
    return redirect("platform_admin")


@platform_admin_required
def admin_run_diagnostics(request):
    """1-Click automated platform audit scanning pricing outliers, duplicate risks, and custody integrity."""
    props = Property.objects.all()
    pricing_anomalies = 0
    missing_media = 0
    for p in props:
        if p.predicted_price and (p.listed_price > p.predicted_price * Decimal("1.8") or p.listed_price < p.predicted_price * Decimal("0.5")):
            pricing_anomalies += 1
        if p.images.count() == 0:
            missing_media += 1

    dup_count = Property.objects.filter(possible_duplicate_of__isnull=False).count()
    unverified_sellers = User.objects.filter(profile__role="SELLER", profile__is_verified=False).count()
    escrow_disputes = Payment.objects.filter(status__in=[Payment.Status.CREATED, Payment.Status.FAILED]).count()

    messages.success(
        request,
        f"Platform Health Scan Complete: {props.count()} Estates Verified · "
        f"{pricing_anomalies} Price Deviations Flagged · {dup_count} Duplicate Risks · "
        f"{missing_media} Listings Lacking Media · {escrow_disputes} Pending Escrows · "
        f"{unverified_sellers} Unverified Sellers Awaiting KYC."
    )
    return redirect("platform_admin")
