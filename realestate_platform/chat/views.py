from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import Q
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
import json

from .forms import AppointmentForm, MessageForm
from .models import Appointment, AppointmentEvent, Conversation, Message
from .chatbot_engine import generate_buyer_bot_response, generate_seller_bot_response, get_user_notifications


def _participant_conversation(user, pk):
    conversation = get_object_or_404(
        Conversation.objects.select_related("property", "buyer", "seller"), pk=pk
    )
    if not conversation.includes(user):
        raise Http404
    return conversation


@login_required
def start_conversation(request, property_id):
    from properties.models import Property
    prop = get_object_or_404(Property, pk=property_id)
    if prop.seller_id == request.user.pk:
        messages.error(request, "You cannot message yourself about your own listing.")
        return redirect("property_detail", pk=prop.pk)
    conversation, _ = Conversation.objects.get_or_create(
        property=prop, buyer=request.user,
        defaults={"seller_id": prop.seller_id},
    )
    return redirect("chat_thread", pk=conversation.pk)


@login_required
def inbox(request):
    conversations = Conversation.objects.filter(Q(buyer=request.user) | Q(seller=request.user)).select_related(
        "property", "buyer", "seller"
    ).prefetch_related("messages")
    return render(request, "chat/inbox.html", {"conversations": conversations})


@login_required
def thread(request, pk):
    conversation = _participant_conversation(request.user, pk)
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                message = form.save(commit=False)
                message.conversation = conversation
                message.sender = request.user
                message.save()
                Conversation.objects.filter(pk=conversation.pk, first_message_at__isnull=True).update(
                    first_message_at=message.created_at
                )
                Conversation.objects.filter(pk=conversation.pk).update(updated_at=timezone.now())
            messages.success(request, "Message sent.")
            return redirect("chat_thread", pk=conversation.pk)
    else:
        form = MessageForm()
    Message.objects.filter(conversation=conversation).exclude(sender=request.user).filter(read_at__isnull=True).update(
        read_at=timezone.now()
    )
    appointments = conversation.appointments.select_related("requested_by").prefetch_related("events")
    return render(request, "chat/thread.html", {
        "conversation": conversation, "form": form,
        "chat_messages": conversation.messages.select_related("sender"),
        "appointments": appointments, "appointment_form": AppointmentForm(),
    })


@login_required
def messages_since(request, pk):
    """Return new messages for a conversation participant (polling fallback)."""
    conversation = _participant_conversation(request.user, pk)
    try:
        after_id = max(0, int(request.GET.get("after", "0")))
    except (TypeError, ValueError):
        after_id = 0
    new_messages = conversation.messages.filter(pk__gt=after_id).select_related("sender").order_by("pk")[:100]
    return JsonResponse({
        "messages": [
            {
                "type": "message",
                "id": item.pk,
                "body": item.body,
                "sender_id": item.sender_id,
                "sender": item.sender.username,
                "created_at": item.created_at.isoformat(),
            }
            for item in new_messages
        ]
    })


@login_required
def request_appointment(request, conversation_id):
    conversation = _participant_conversation(request.user, conversation_id)
    if request.user.pk != conversation.buyer_id:
        messages.error(request, "Only the buyer can request an appointment.")
        return redirect("chat_thread", pk=conversation.pk)
    if request.method != "POST":
        return redirect("chat_thread", pk=conversation.pk)
    form = AppointmentForm(request.POST)
    if form.is_valid():
        appointment = form.save(commit=False)
        appointment.conversation = conversation
        appointment.requested_by = request.user
        appointment.save()
        AppointmentEvent.objects.create(
            appointment=appointment, actor=request.user,
            old_status=Appointment.Status.REQUESTED, new_status=Appointment.Status.REQUESTED,
            note="Appointment requested by buyer",
        )
        messages.success(request, "Appointment request sent to seller.")
    else:
        messages.error(request, "Could not request appointment. Please verify the date and time.")
    return redirect("chat_thread", pk=conversation.pk)


@login_required
def update_appointment(request, pk, action):
    appointment = get_object_or_404(
        Appointment.objects.select_related("conversation", "conversation__property"), pk=pk
    )
    conversation = appointment.conversation
    if not conversation.includes(request.user):
        raise Http404
    if request.method != "POST":
        return redirect("chat_thread", pk=conversation.pk)
    previous_status = appointment.status
    if action == "confirm":
        if request.user.pk != conversation.seller_id:
            messages.error(request, "Only the seller can confirm appointments.")
            return redirect("chat_thread", pk=conversation.pk)
        if previous_status != Appointment.Status.REQUESTED:
            messages.error(request, "Only requested appointments can be confirmed.")
            return redirect("chat_thread", pk=conversation.pk)
        new_status = Appointment.Status.CONFIRMED
    elif action == "decline":
        if request.user.pk != conversation.seller_id:
            messages.error(request, "Only the seller can decline appointments.")
            return redirect("chat_thread", pk=conversation.pk)
        new_status = Appointment.Status.DECLINED
    elif action == "cancel":
        new_status = Appointment.Status.CANCELLED
    else:
        raise Http404
    appointment.status = new_status
    if new_status == Appointment.Status.CONFIRMED:
        appointment.confirmed_at = timezone.now()
    appointment.save(update_fields=["status", "confirmed_at", "updated_at"])
    AppointmentEvent.objects.create(
        appointment=appointment, actor=request.user, old_status=previous_status,
        new_status=new_status, note=f"Appointment {new_status.lower()} by {request.user.username}",
    )
    messages.success(request, f"Appointment {new_status.lower()}.")
    return redirect("chat_thread", pk=conversation.pk)


@login_required
def appointment_metrics(request):
    if not request.user.is_staff:
        raise Http404
    confirmed = Appointment.objects.filter(status=Appointment.Status.CONFIRMED, confirmed_at__isnull=False).select_related(
        "conversation", "conversation__property", "conversation__buyer", "conversation__seller"
    )
    durations = [a.time_to_appointment_minutes for a in confirmed if a.time_to_appointment_minutes is not None]
    durations.sort()
    median = None
    if durations:
        mid = len(durations) // 2
        median = durations[mid] if len(durations) % 2 else (durations[mid - 1] + durations[mid]) / 2
    return render(request, "chat/appointment_metrics.html", {
        "confirmed_appointments": confirmed, "measured_count": len(durations),
        "median_minutes": median, "all_count": Appointment.objects.count(),
    })


from django.views.decorators.csrf import csrf_exempt

# ==================== AI CHATBOT & NOTIFICATIONS API ====================

@csrf_exempt
def api_chatbot(request):
    """
    Dual AI Chatbot API:
    - Mode 'buyer': Estate Concierge AI
    - Mode 'seller': Portfolio Strategist AI
    """
    if request.method != "POST":
        return JsonResponse({"error": "POST method required"}, status=405)

    try:
        data = json.loads(request.body or "{}")
        user_message = data.get("message", "").strip()
        mode = data.get("mode", "buyer").lower()
    except Exception:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    if not user_message:
        return JsonResponse({"error": "Empty message"}, status=400)

    # Determine user role or requested mode
    if mode == "seller":
        reply = generate_seller_bot_response(user_message, request.user)
    else:
        reply = generate_buyer_bot_response(user_message, request.user)

    alerts = get_user_notifications(request.user) if request.user.is_authenticated else []

    return JsonResponse({
        "mode": mode,
        "reply": reply,
        "notifications": alerts,
    })


def api_notifications(request):
    """Fetches real-time notification alerts and unread count."""
    alerts = get_user_notifications(request.user) if request.user.is_authenticated else []
    return JsonResponse({
        "count": len(alerts),
        "alerts": alerts,
    })


def advisor_view(request):
    """Dedicated full-screen AI Advisory & Intelligence Center."""
    is_seller = request.user.is_authenticated and request.user.properties.exists()
    default_mode = "seller" if is_seller else "buyer"
    return render(request, "chat/advisor.html", {
        "default_mode": default_mode,
        "alerts": get_user_notifications(request.user) if request.user.is_authenticated else []
    })
