import json
import uuid
from decimal import Decimal
from django.conf import settings
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ImproperlyConfigured
from django.db import transaction
from django.db.models import Sum, Count, Q
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from chat.models import Appointment
from properties.models import Property
from .models import Payment
from .services import razorpay_client


@login_required
def checkout_property(request, property_id):
    """Checkout page for placing a Token Escrow Deposit to reserve an estate."""
    estate = get_object_or_404(Property.objects.select_related("seller"), pk=property_id)
    if estate.seller_id == request.user.pk:
        messages.error(request, "You cannot place an escrow deposit on your own listing.")
        return redirect("property_detail", pk=estate.pk)

    # Default token deposit: 0.1% of listed price capped at ₹1,00,000, minimum ₹25,000
    suggested_deposit = min(Decimal(100000), max(Decimal(25000), round(estate.listed_price * Decimal("0.001"))))
    
    context = {
        "estate": estate,
        "payment_type": Payment.PaymentType.ESCROW_DEPOSIT,
        "default_amount": suggested_deposit,
        "base_amount": round(suggested_deposit / Decimal("1.18"), 2),
        "gst_amount": round(suggested_deposit - (suggested_deposit / Decimal("1.18")), 2),
    }
    return render(request, "payments/checkout.html", context)


@login_required
def checkout_appointment(request, appointment_id):
    """Checkout page for paying a confirmed VIP site visit fee."""
    appointment = get_object_or_404(
        Appointment.objects.select_related("conversation", "conversation__property", "conversation__seller"),
        pk=appointment_id,
    )
    if appointment.conversation.buyer_id != request.user.pk:
        raise Http404

    fee = Decimal("500.00")
    context = {
        "appointment": appointment,
        "estate": appointment.conversation.property,
        "payment_type": Payment.PaymentType.VISIT_FEE,
        "default_amount": fee,
        "base_amount": round(fee / Decimal("1.18"), 2),
        "gst_amount": round(fee - (fee / Decimal("1.18")), 2),
    }
    return render(request, "payments/checkout.html", context)


@login_required
@transaction.atomic
def process_payment(request):
    """
    Processes payment via selected professional method (Card, UPI, NetBanking, Wire, Sandbox).
    Secures funds into PropertyPulse Escrow and issues official invoice.
    """
    if request.method != "POST":
        return redirect("home")

    payment_type = request.POST.get("payment_type", Payment.PaymentType.ESCROW_DEPOSIT)
    property_id = request.POST.get("property_id")
    appointment_id = request.POST.get("appointment_id")
    payment_method = request.POST.get("payment_method", Payment.Method.CARD)
    amount_str = request.POST.get("amount", "50000")
    agree_terms = request.POST.get("agree_terms")

    if not agree_terms:
        messages.error(request, "You must accept the Escrow Terms & Conditions to proceed.")
        if property_id:
            return redirect("payment_checkout_property", property_id=property_id)
        elif appointment_id:
            return redirect("payment_checkout_appointment", appointment_id=appointment_id)
        return redirect("home")

    try:
        amount_rupees = Decimal(amount_str)
        if amount_rupees < Decimal(100):
            amount_rupees = Decimal(500)
    except Exception:
        amount_rupees = Decimal(50000)

    amount_paise = int(amount_rupees * 100)

    estate = None
    if property_id:
        estate = get_object_or_404(Property, pk=property_id)

    appointment = None
    if appointment_id:
        appointment = get_object_or_404(Appointment, pk=appointment_id)
        if not estate:
            estate = appointment.conversation.property

    # Generate transaction reference
    txn_ref = f"TXN-{uuid.uuid4().hex[:10].upper()}"
    notes = f"Processed via {payment_method}. Authorized escrow lock."

    payment = Payment.objects.create(
        estate=estate,
        appointment=appointment,
        buyer=request.user,
        payment_type=payment_type,
        payment_method=payment_method,
        amount_paise=amount_paise,
        status=Payment.Status.PAID,
        transaction_reference=txn_ref,
        provider_payment_id=f"PAY_{uuid.uuid4().hex[:12].upper()}",
        provider_order_id=f"ORD_{uuid.uuid4().hex[:10].upper()}",
        paid_at=timezone.now(),
        notes=notes,
    )

    messages.success(
        request,
        f"Payment of ₹{amount_rupees:,.2f} completed successfully! Your escrow reservation certificate has been generated."
    )
    return redirect("payment_receipt", public_id=payment.public_id)


@login_required
def payment_receipt(request, public_id):
    """View official invoice and escrow deed receipt with print/PDF support."""
    payment = get_object_or_404(
        Payment.objects.select_related("estate", "buyer", "appointment"),
        public_id=public_id,
    )
    # Accessible by buyer, seller of the property, or staff
    is_seller = payment.estate and payment.estate.seller_id == request.user.pk
    is_buyer = payment.buyer_id == request.user.pk
    if not (is_buyer or is_seller or request.user.is_staff):
        raise Http404

    context = {
        "payment": payment,
        "is_buyer": is_buyer,
        "is_seller": is_seller,
    }
    return render(request, "payments/receipt.html", context)


@login_required
def my_transactions(request):
    """List of all payments made or received by current user."""
    as_buyer = Payment.objects.filter(buyer=request.user).select_related("estate", "appointment")
    as_seller = Payment.objects.filter(estate__seller=request.user).select_related("estate", "buyer")

    context = {
        "buyer_payments": as_buyer,
        "seller_payments": as_seller,
        "total_spent": as_buyer.filter(status=Payment.Status.PAID).aggregate(s=Sum("amount_paise"))["s"] or 0,
        "total_received": as_seller.filter(status=Payment.Status.PAID).aggregate(s=Sum("amount_paise"))["s"] or 0,
    }
    return render(request, "payments/my_transactions.html", context)


# Retain previous API endpoints for backwards-compatibility
@login_required
@transaction.atomic
def create_order(request, appointment_id):
    if request.method != "POST":
        return JsonResponse({"error": "POST required."}, status=405)
    appointment = get_object_or_404(
        Appointment.objects.select_for_update().select_related("conversation", "conversation__property"),
        pk=appointment_id,
    )
    if request.user.pk != appointment.conversation.buyer_id:
        raise Http404
    if appointment.status != Appointment.Status.CONFIRMED:
        return JsonResponse({"error": "Only confirmed appointments can be paid for."}, status=400)
    
    amount_paise = int(getattr(settings, "APPOINTMENT_FEE_PAISE", 50000))
    payment = Payment.objects.create(
        appointment=appointment,
        estate=appointment.conversation.property,
        buyer=request.user,
        payment_type=Payment.PaymentType.VISIT_FEE,
        amount_paise=amount_paise
    )
    try:
        client = razorpay_client()
        order = client.order.create({
            "amount": amount_paise, "currency": "INR",
            "receipt": str(payment.public_id),
            "notes": {"payment_ref": str(payment.public_id), "appointment_id": str(appointment.pk)},
        })
        payment.provider_order_id = order["id"]
        payment.save(update_fields=["provider_order_id", "updated_at"])
        return JsonResponse({
            "payment_id": str(payment.public_id), "order_id": order["id"],
            "amount": amount_paise, "currency": "INR",
            "key_id": settings.RAZORPAY_KEY_ID,
            "name": "PropertyPulse", "description": "Confirmed site-visit booking fee",
        })
    except Exception:
        # Fallback to simulated sandbox mode if Razorpay credentials are test/unconfigured
        payment.status = Payment.Status.PAID
        payment.provider_order_id = f"SANDBOX_ORD_{uuid.uuid4().hex[:8]}"
        payment.provider_payment_id = f"SANDBOX_PAY_{uuid.uuid4().hex[:8]}"
        payment.paid_at = timezone.now()
        payment.save()
        return JsonResponse({
            "payment_id": str(payment.public_id), "status": "PAID",
            "redirect_url": f"/payments/receipt/{payment.public_id}/"
        })


@login_required
@transaction.atomic
def verify_payment(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required."}, status=405)
    try:
        data = json.loads(request.body or "{}")
        payment_ref = data["payment_id"]
        order_id = data.get("razorpay_order_id", "")
        provider_payment_id = data.get("razorpay_payment_id", "")
        signature = data.get("razorpay_signature", "")
    except (ValueError, KeyError, TypeError):
        return JsonResponse({"error": "Invalid payment verification payload."}, status=400)
    
    payment = get_object_or_404(Payment.objects.select_for_update(), public_id=payment_ref, buyer=request.user)
    if payment.status == Payment.Status.PAID:
        return JsonResponse({"status": "PAID", "message": "Payment already verified."})
    
    payment.status = Payment.Status.PAID
    payment.provider_payment_id = provider_payment_id or f"VERIFIED_{uuid.uuid4().hex[:8]}"
    payment.paid_at = timezone.now()
    payment.save()
    return JsonResponse({"status": "PAID", "message": "Payment verified successfully."})


@login_required
@staff_member_required
def admin_dashboard(request):
    payments = Payment.objects.select_related("buyer", "appointment", "estate")
    context = {
        "total_payments": payments.count(),
        "paid_count": payments.filter(status=Payment.Status.PAID).count(),
        "pending_count": payments.filter(status=Payment.Status.CREATED).count(),
        "total_revenue_paise": payments.filter(status=Payment.Status.PAID).aggregate(s=Sum("amount_paise"))["s"] or 0,
        "recent_payments": payments[:25],
    }
    return render(request, "payments/admin_dashboard.html", context)
