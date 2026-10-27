from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("public_id", "appointment", "buyer", "amount_paise", "currency", "status", "created_at", "paid_at")
    list_filter = ("status", "currency", "created_at")
    search_fields = ("public_id", "provider_order_id", "provider_payment_id", "buyer__username")
    readonly_fields = ("public_id", "created_at", "updated_at", "paid_at", "provider_order_id", "provider_payment_id")
