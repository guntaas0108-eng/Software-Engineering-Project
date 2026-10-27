import uuid
from django.conf import settings
from django.db import models
from django.utils import timezone


class Payment(models.Model):
    """Payment attempt for a confirmed property visit; secrets are never stored here."""
    class Status(models.TextChoices):
        CREATED = "CREATED", "Created"
        PAID = "PAID", "Paid"
        FAILED = "FAILED", "Failed"
        CANCELLED = "CANCELLED", "Cancelled"

    public_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    appointment = models.ForeignKey("chat.Appointment", on_delete=models.PROTECT, related_name="payments")
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="property_payments")
    amount_paise = models.PositiveIntegerField()
    currency = models.CharField(max_length=3, default="INR")
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.CREATED)
    provider_order_id = models.CharField(max_length=100, blank=True, db_index=True)
    provider_payment_id = models.CharField(max_length=100, blank=True, db_index=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    paid_at = models.DateTimeField(null=True, blank=True)
    failure_reason = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ["-created_at"]
        constraints = [models.UniqueConstraint(fields=["provider_payment_id"], condition=~models.Q(provider_payment_id=""), name="unique_nonempty_provider_payment_id")]

    @property
    def amount_rupees(self):
        return self.amount_paise / 100

    def __str__(self):
        return f"Payment {self.public_id} — {self.get_status_display()}"
