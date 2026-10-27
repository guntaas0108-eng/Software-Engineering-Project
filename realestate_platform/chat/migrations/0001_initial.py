# Generated for PropertyPulse Sprint 4 (chat and appointment scheduling).
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("properties", "0003_savedproperty"),
    ]
    operations = [
        migrations.CreateModel(
            name="Conversation",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("first_message_at", models.DateTimeField(blank=True, null=True)),
                ("buyer", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="buyer_conversations", to=settings.AUTH_USER_MODEL)),
                ("property", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="conversations", to="properties.property")),
                ("seller", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="seller_conversations", to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["-updated_at"]},
        ),
        migrations.CreateModel(
            name="Appointment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("scheduled_for", models.DateTimeField()),
                ("note", models.CharField(blank=True, max_length=500)),
                ("status", models.CharField(choices=[("REQUESTED", "Requested"), ("CONFIRMED", "Confirmed"), ("DECLINED", "Declined"), ("CANCELLED", "Cancelled"), ("COMPLETED", "Completed")], default="REQUESTED", max_length=12)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("confirmed_at", models.DateTimeField(blank=True, null=True)),
                ("conversation", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="appointments", to="chat.conversation")),
                ("requested_by", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="requested_property_appointments", to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["scheduled_for"]},
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("body", models.TextField(max_length=4000)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("read_at", models.DateTimeField(blank=True, null=True)),
                ("conversation", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="messages", to="chat.conversation")),
                ("sender", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="sent_property_messages", to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["created_at", "pk"]},
        ),
        migrations.CreateModel(
            name="AppointmentEvent",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("old_status", models.CharField(blank=True, max_length=12)),
                ("new_status", models.CharField(choices=[("REQUESTED", "Requested"), ("CONFIRMED", "Confirmed"), ("DECLINED", "Declined"), ("CANCELLED", "Cancelled"), ("COMPLETED", "Completed")], max_length=12)),
                ("note", models.CharField(blank=True, max_length=500)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("actor", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ("appointment", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="events", to="chat.appointment")),
            ],
            options={"ordering": ["created_at"]},
        ),
        migrations.AddConstraint(
            model_name="conversation",
            constraint=models.UniqueConstraint(fields=("property", "buyer"), name="unique_buyer_property_conversation"),
        ),
    ]
