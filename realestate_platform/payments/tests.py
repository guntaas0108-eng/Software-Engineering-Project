from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class PaymentAccessTests(TestCase):
    """Focused authorization/dashboard tests; gateway integration needs sandbox tests."""
    def setUp(self):
        User = get_user_model()
        self.buyer = User.objects.create_user(username="buyer_test", password="Test-pass-12345")
        self.seller = User.objects.create_user(username="seller_test", password="Test-pass-12345")
        self.staff = User.objects.create_user(username="staff_test", password="Test-pass-12345", is_staff=True)
        # Property fields are project-specific, so dashboard access tests don't need one.
        self.client = Client()

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse("payments_admin_dashboard"))
        self.assertIn(response.status_code, (302, 301))

    def test_dashboard_rejects_non_staff(self):
        self.client.login(username="buyer_test", password="Test-pass-12345")
        response = self.client.get(reverse("payments_admin_dashboard"))
        self.assertEqual(response.status_code, 404)

    def test_dashboard_available_to_staff(self):
        self.client.login(username="staff_test", password="Test-pass-12345")
        response = self.client.get(reverse("payments_admin_dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Operations dashboard")
