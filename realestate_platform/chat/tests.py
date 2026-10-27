from datetime import timedelta
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from properties.models import Property
from .models import Appointment, AppointmentEvent, Conversation, Message

User = get_user_model()


class ChatAndAppointmentTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.buyer = User.objects.create_user(username="buyer", password="pass12345")
        cls.seller = User.objects.create_user(username="seller", password="pass12345")
        cls.other = User.objects.create_user(username="other", password="pass12345")
        cls.prop = Property.objects.create(
            seller=cls.seller, title="Sunny Apartment", locality="Model Town", city="Patiala",
            area_sqft=1000, listed_price=5000000,
        )
        cls.conversation = Conversation.objects.create(property=cls.prop, buyer=cls.buyer, seller=cls.seller)

    def test_buyer_can_open_inbox_and_thread(self):
        self.client.login(username="buyer", password="pass12345")
        self.assertEqual(self.client.get(reverse("chat_inbox")).status_code, 200)
        self.assertEqual(self.client.get(reverse("chat_thread", args=[self.conversation.pk])).status_code, 200)

    def test_anonymous_user_is_redirected(self):
        response = self.client.get(reverse("chat_inbox"))
        self.assertEqual(response.status_code, 302)

    def test_non_participant_cannot_view_thread(self):
        self.client.login(username="other", password="pass12345")
        self.assertEqual(self.client.get(reverse("chat_thread", args=[self.conversation.pk])).status_code, 404)

    def test_buyer_can_send_message_and_sets_first_message_timestamp(self):
        self.client.login(username="buyer", password="pass12345")
        response = self.client.post(reverse("chat_thread", args=[self.conversation.pk]), {"body": "Hello seller"})
        self.assertEqual(response.status_code, 302)
        self.conversation.refresh_from_db()
        self.assertIsNotNone(self.conversation.first_message_at)
        self.assertEqual(self.conversation.messages.get().body, "Hello seller")

    def test_participant_can_poll_new_messages(self):
        message = Message.objects.create(
            conversation=self.conversation, sender=self.seller, body="Hello buyer"
        )
        self.client.login(username="buyer", password="pass12345")
        response = self.client.get(reverse("chat_messages_since", args=[self.conversation.pk]), {"after": 0})
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(len(payload["messages"]), 1)
        self.assertEqual(payload["messages"][0]["id"], message.pk)
        self.assertEqual(payload["messages"][0]["body"], "Hello buyer")

    def test_non_participant_cannot_poll_messages(self):
        self.client.login(username="other", password="pass12345")
        response = self.client.get(reverse("chat_messages_since", args=[self.conversation.pk]))
        self.assertEqual(response.status_code, 404)

    def test_empty_message_is_rejected(self):
        self.client.login(username="buyer", password="pass12345")
        self.client.post(reverse("chat_thread", args=[self.conversation.pk]), {"body": "   "})
        self.assertEqual(Message.objects.count(), 0)

    def test_buyer_can_request_future_appointment(self):
        self.client.login(username="buyer", password="pass12345")
        future = (timezone.localtime(timezone.now() + timedelta(days=2))).strftime("%Y-%m-%dT%H:%M")
        response = self.client.post(reverse("appointment_request", args=[self.conversation.pk]), {
            "scheduled_for": future, "note": "Please call on arrival",
        })
        self.assertEqual(response.status_code, 302)
        appointment = Appointment.objects.get()
        self.assertEqual(appointment.status, Appointment.Status.REQUESTED)
        self.assertEqual(AppointmentEvent.objects.filter(appointment=appointment).count(), 1)

    def test_seller_can_confirm_and_metric_is_computed(self):
        self.conversation.first_message_at = timezone.now() - timedelta(minutes=45)
        self.conversation.save(update_fields=["first_message_at"])
        appointment = Appointment.objects.create(
            conversation=self.conversation, requested_by=self.buyer,
            scheduled_for=timezone.now() + timedelta(days=1),
        )
        self.client.login(username="seller", password="pass12345")
        response = self.client.post(reverse("appointment_update", args=[appointment.pk, "confirm"]))
        self.assertEqual(response.status_code, 302)
        appointment.refresh_from_db()
        self.assertEqual(appointment.status, Appointment.Status.CONFIRMED)
        self.assertIsNotNone(appointment.confirmed_at)
        self.assertGreaterEqual(appointment.time_to_appointment_minutes, 44)

    def test_buyer_cannot_confirm_appointment(self):
        appointment = Appointment.objects.create(
            conversation=self.conversation, requested_by=self.buyer,
            scheduled_for=timezone.now() + timedelta(days=1),
        )
        self.client.login(username="buyer", password="pass12345")
        self.assertEqual(self.client.post(reverse("appointment_update", args=[appointment.pk, "confirm"])).status_code, 404)

    def test_seller_cannot_request_appointment(self):
        self.client.login(username="seller", password="pass12345")
        future = (timezone.localtime(timezone.now() + timedelta(days=2))).strftime("%Y-%m-%dT%H:%M")
        response = self.client.post(reverse("appointment_request", args=[self.conversation.pk]), {"scheduled_for": future})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(Appointment.objects.count(), 0)

    def test_metrics_are_staff_only(self):
        self.client.login(username="buyer", password="pass12345")
        self.assertEqual(self.client.get(reverse("appointment_metrics")).status_code, 404)
        self.seller.is_staff = True
        self.seller.save(update_fields=["is_staff"])
        self.client.login(username="seller", password="pass12345")
        self.assertEqual(self.client.get(reverse("appointment_metrics")).status_code, 200)

    def test_start_conversation_redirects_to_existing_conversation(self):
        self.client.login(username="buyer", password="pass12345")
        response = self.client.get(reverse("chat_start", args=[self.prop.pk]))
        self.assertRedirects(response, reverse("chat_thread", args=[self.conversation.pk]))
        self.assertEqual(Conversation.objects.count(), 1)

    def test_seller_cannot_message_self(self):
        self.client.login(username="seller", password="pass12345")
        response = self.client.get(reverse("chat_start", args=[self.prop.pk]))
        self.assertRedirects(response, reverse("property_detail", args=[self.prop.pk]))
        self.assertEqual(Conversation.objects.count(), 1)
