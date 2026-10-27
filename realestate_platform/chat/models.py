from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Conversation(models.Model):
    """A buyer's conversation with the seller about one property."""
    property = models.ForeignKey("properties.Property", on_delete=models.CASCADE, related_name="conversations")
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="buyer_conversations")
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="seller_conversations")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_message_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-updated_at"]
        constraints = [models.UniqueConstraint(fields=["property", "buyer"], name="unique_buyer_property_conversation")]

    def clean(self):
        if self.buyer_id and self.seller_id and self.buyer_id == self.seller_id:
            raise ValidationError("A seller cannot start a buyer conversation with themselves.")
        if self.property_id and self.seller_id and self.property.seller_id != self.seller_id:
            raise ValidationError("Conversation seller must own the property.")

    def includes(self, user):
        return user.is_authenticated and user.pk in (self.buyer_id, self.seller_id)

    def __str__(self):
        return f"{self.property.title}: {self.buyer} ↔ {self.seller}"


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="sent_property_messages",
    )
    body = models.TextField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["created_at", "pk"]

    def clean(self):
        if self.conversation_id and self.sender_id and not self.conversation.includes(self.sender):
            raise ValidationError("Only conversation participants can send messages.")
        if not self.body.strip():
            raise ValidationError("Message cannot be empty.")

    def __str__(self):
        return f"Message {self.pk} in conversation {self.conversation_id}"


class Appointment(models.Model):
    class Status(models.TextChoices):
        REQUESTED = "REQUESTED", "Requested"
        CONFIRMED = "CONFIRMED", "Confirmed"
        DECLINED = "DECLINED", "Declined"
        CANCELLED = "CANCELLED", "Cancelled"
        COMPLETED = "COMPLETED", "Completed"

    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="appointments")
    requested_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="requested_property_appointments",
    )
    scheduled_for = models.DateTimeField()
    note = models.CharField(max_length=500, blank=True)
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.REQUESTED)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    confirmed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["scheduled_for"]

    def clean(self):
        if self.conversation_id and self.requested_by_id and self.requested_by_id != self.conversation.buyer_id:
            raise ValidationError("Only the buyer can request an appointment.")
        if self.scheduled_for and self.scheduled_for <= timezone.now():
            raise ValidationError("Appointment must be scheduled in the future.")

    @property
    def time_to_appointment_minutes(self):
        """Minutes from first message to confirmation; None until measurable."""
        start = self.conversation.first_message_at
        if not start or not self.confirmed_at:
            return None
        return max(0, int((self.confirmed_at - start).total_seconds() // 60))

    def __str__(self):
        return f"Visit for {self.conversation.property.title} ({self.get_status_display()})"


class AppointmentEvent(models.Model):
    """Audit trail for appointment status changes and time-to-appointment reporting."""
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name="events")
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    old_status = models.CharField(max_length=12, blank=True)
    new_status = models.CharField(max_length=12, choices=Appointment.Status.choices)
    note = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]
