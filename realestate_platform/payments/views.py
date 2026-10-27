import json
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ImproperlyConfigured
from django.db import transaction
from django.db.models import Sum, Count
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from chat.models import Appointment
from .models import Payment
from .services import razorpay_client


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
    # Fixed visit booking fee, in paise; configure in .env. Never trust a client-supplied amount.
    amount_paise = int(getattr(settings, "APPOINTMENT_FEE_PAISE", 50000))
    if amount_paise < 100:
        return JsonResponse({"error": "Configured payment amount is invalid."}, status=500)
    payment = Payment.objects.create(appointment=appointment, buyer=request.user, amount_paise=amount_paise)
    try:
        client = razorpay_client()
        order = client.order.create({
            "amount": amount_paise, "currency": "INR",
            "receipt": str(payment.public_id),
            "notes": {"payment_ref": str(payment.public_id), "appointment_id": str(appointment.pk)},
        })
    except (ImproperlyConfigured, Exception) as exc:
        payment.status = Payment.Status.FAILED
        payment.failure_reason = "Gateway order creation failed"
        payment.save(update_fields=["status", "failure_reason", "updated_at"])
        if isinstance(exc, ImproperlyConfigured):
            return JsonResponse({"error": str(exc)}, status=503)
        return JsonResponse({"error": "Payment gateway could not create an order. Check gateway configuration."}, status=502)
    payment.provider_order_id = order["id"]
    payment.save(update_fields=["provider_order_id", "updated_at"])
    return JsonResponse({
        "payment_id": str(payment.public_id), "order_id": order["id"],
        "amount": amount_paise, "currency": "INR",
        "key_id": settings.RAZORPAY_KEY_ID,
        "name": "PropertyPulse", "description": "Confirmed site-visit booking fee",
    })


@login_required
@transaction.atomic
def verify_payment(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required."}, status=405)
    try:
        data = json.loads(request.body or "{}")
        payment_ref = data["payment_id"]
        order_id = data["razorpay_order_id"]
        provider_payment_id = data["razorpay_payment_id"]
        signature = data["razorpay_signature"]
    except (ValueError, KeyError, TypeError):
        return JsonResponse({"error": "Invalid payment verification payload."}, status=400)
    payment = get_object_or_404(Payment.objects.select_for_update(), public_id=payment_ref, buyer=request.user)
    if payment.status == Payment.Status.PAID:
        return JsonResponse({"status": "PAID", "message": "Payment already verified."})
    if not payment.provider_order_id or order_id != payment.provider_order_id:
        return JsonResponse({"error": "Order does not match this payment."}, status=400)
    try:
        razorpay_client().utility.verify_payment_signature({
            "razorpay_order_id": order_id,
            "razorpay_payment_id": provider_payment_id,
            "razorpay_signature": signature,
        })
    except Exception:
        return JsonResponse({"error": "Payment signature verification failed."}, status=400)
    payment.status = Payment.Status.PAID
    payment.provider_payment_id = provider_payment_id
    payment.paid_at = timezone.now()
    payment.failure_reason = ""
    payment.save(update_fields=["status", "provider_payment_id", "paid_at", "failure_reason", "updated_at"])
    return JsonResponse({"status": "PAID", "message": "Payment verified successfully."})


@login_required
@staff_member_required

def admin_dashboard(request):
    payments = Payment.objects.select_related("buyer", "appointment", "appointment__conversation__property")
    context = {
        "total_payments": payments.count(),
        "paid_count": payments.filter(status=Payment.Status.PAID).count(),
        "pending_count": payments.filter(status=Payment.Status.CREATED).count(),
        "failed_count": payments.filter(status=Payment.Status.FAILED).count(),
        "revenue_rupees": (payments.filter(status=Payment.Status.PAID).aggregate(total=Sum("amount_paise"))["total"] or 0) / 100,
        "recent_payments": payments[:25],
        "appointment_count": Appointment.objects.count(),
        "confirmed_appointment_count": Appointment.objects.filter(status=Appointment.Status.CONFIRMED).count(),
    }
    return render(request, "payments/admin_dashboard.html", context)
