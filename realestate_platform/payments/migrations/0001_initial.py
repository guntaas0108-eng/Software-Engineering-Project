# Generated for Sprint 5 payment tracking.
import uuid
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chat", "0001_initial"),
    ]
    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("public_id", models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ("amount_paise", models.PositiveIntegerField()),
                ("currency", models.CharField(default="INR", max_length=3)),
                ("status", models.CharField(choices=[("CREATED", "Created"), ("PAID", "Paid"), ("FAILED", "Failed"), ("CANCELLED", "Cancelled")], default="CREATED", max_length=10)),
                ("provider_order_id", models.CharField(blank=True, db_index=True, max_length=100)),
                ("provider_payment_id", models.CharField(blank=True, db_index=True, max_length=100)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("paid_at", models.DateTimeField(blank=True, null=True)),
                ("failure_reason", models.CharField(blank=True, max_length=250)),
                ("appointment", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="payments", to="chat.appointment")),
                ("buyer", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="property_payments", to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["-created_at"]},
        ),
        migrations.AddConstraint(
            model_name="payment",
            constraint=models.UniqueConstraint(condition=models.Q(("provider_payment_id", ""), _negated=True), fields=("provider_payment_id",), name="unique_nonempty_provider_payment_id"),
        ),
    ]
