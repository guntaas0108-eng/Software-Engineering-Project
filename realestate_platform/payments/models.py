import builtins
import uuid
from decimal import Decimal
from django.conf import settings
from django.db import models
from django.utils import timezone


class Payment(models.Model):
    """
    Comprehensive payment entity for property token escrow deposits,
    VIP site visits, and certified property valuation reports.
    """
    class Status(models.TextChoices):
        CREATED = "CREATED", "Pending"
        PAID = "PAID", "Completed & Secured in Escrow"
        FAILED = "FAILED", "Failed"
        CANCELLED = "CANCELLED", "Cancelled"
        REFUNDED = "REFUNDED", "Refunded"

    class PaymentType(models.TextChoices):
        ESCROW_DEPOSIT = "ESCROW_DEPOSIT", "Token Escrow Deposit (Reservation)"
        VISIT_FEE = "VISIT_FEE", "VIP Escorted Site Inspection"
        VALUATION_REPORT = "VALUATION_REPORT", "Certified AI Valuation & Title Dossier"

    class Method(models.TextChoices):
        UPI = "UPI", "UPI / QR Instant Transfer"
        CARD = "CARD", "Credit / Debit Card (Visa, MC, Amex)"
        NETBANKING = "NETBANKING", "Net Banking (Major Banks)"
        WIRE = "WIRE", "RTGS / Escrow High-Value Wire"
        SANDBOX = "SANDBOX", "Sandbox Fast Approval"

    public_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    appointment = models.ForeignKey(
        "chat.Appointment", null=True, blank=True, on_delete=models.SET_NULL, related_name="payments"
    )
    estate = models.ForeignKey(
        "properties.Property", null=True, blank=True, on_delete=models.SET_NULL, related_name="payments"
    )
    buyer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="property_payments"
    )
    payment_type = models.CharField(
        max_length=25, choices=PaymentType.choices, default=PaymentType.ESCROW_DEPOSIT
    )
    payment_method = models.CharField(
        max_length=20, choices=Method.choices, default=Method.CARD
    )
    amount_paise = models.PositiveIntegerField()
    currency = models.CharField(max_length=3, default="INR")
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.CREATED)
    
    provider_order_id = models.CharField(max_length=100, blank=True, db_index=True)
    provider_payment_id = models.CharField(max_length=100, blank=True, db_index=True)
    transaction_reference = models.CharField(max_length=120, blank=True)
    notes = models.TextField(blank=True)
    
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    paid_at = models.DateTimeField(null=True, blank=True)
    failure_reason = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ["-created_at"]

    @builtins.property
    def amount_rupees(self):
        return Decimal(self.amount_paise) / Decimal(100)

    @builtins.property
    def base_amount_rupees(self):
        # Base before 18% GST
        return round(Decimal(self.amount_rupees) / Decimal("1.18"), 2)

    @builtins.property
    def gst_rupees(self):
        return round(Decimal(self.amount_rupees) - self.base_amount_rupees, 2)

    @builtins.property
    def invoice_number(self):
        return f"PP-INV-{str(self.public_id)[:8].upper()}"

    def __str__(self):
        return f"Payment {self.public_id} — {self.get_payment_type_display()} ({self.get_status_display()})"
