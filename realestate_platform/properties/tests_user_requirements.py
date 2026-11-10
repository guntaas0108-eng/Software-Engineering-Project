import hashlib
import hmac
from decimal import Decimal
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings

from accounts.models import UserProfile
from properties.models import Property
from payments.models import Payment
from ml_predictor.predictor import PricePredictor

User = get_user_model()


class BuyerSellerMLAndSecurityFeatureTests(TestCase):
    def setUp(self):
        # Create Seller
        self.seller = User.objects.create_user(username="test_proprietor", password="Password123!")
        self.seller.profile.role = UserProfile.Role.SELLER
        self.seller.profile.save()

        # Create Buyer
        self.buyer = User.objects.create_user(username="test_buyer", password="Password123!")
        self.buyer.profile.role = UserProfile.Role.BUYER
        self.buyer.profile.save()

        # Create Property
        self.property = Property.objects.create(
            seller=self.seller,
            title="The Grand Penthouse",
            description="Luxury panoramic residence.",
            area_sqft=3200,
            bedrooms=4,
            bathrooms=4,
            age_years=2,
            category=Property.Category.RESIDENTIAL,
            locality="Model Town",
            city="Ludhiana",
            listed_price=Decimal("15000000"),
            status=Property.Status.ACTIVE,
        )

        self.client = Client()

    def test_ml_timing_prediction_engine(self):
        """Verify the ML prediction engine produces buy now/future timing, milestones, and barometer score."""
        predictor = PricePredictor()
        analysis = predictor.analyze_timing(self.property)
        self.assertIn("verdict", analysis)
        self.assertIn(analysis["verdict"], ["BUY NOW", "MONITOR & NEGOTIATE", "WAIT — BUY IN FUTURE"])
        self.assertIn("timing_emoji", analysis)
        self.assertIn("timing_badge", analysis)
        self.assertIn("projections", analysis)
        self.assertEqual(len(analysis["projections"]), 5)  # Today, 6M, 1Y, 2Y, 3Y
        self.assertIn("cost_of_delay_1yr", analysis)
        self.assertIn("barometer_score", analysis)
        self.assertGreaterEqual(analysis["barometer_score"], 0)
        self.assertLessEqual(analysis["barometer_score"], 100)

    def test_ml_visible_to_buyer_side_only(self):
        """Verify ML buyer intelligence is rendered for buyers and hidden from sellers/proprietors."""
        # 1. Unauthenticated buyer/guest
        resp_guest = self.client.get(reverse("property_detail", args=[self.property.pk]))
        self.assertEqual(resp_guest.status_code, 200)
        self.assertTrue(resp_guest.context["show_ml_buyer_intel"])
        self.assertContains(resp_guest, "Purchase Timing &amp; Future Valuation Horizon")
        self.assertContains(resp_guest, "Buyer Barometer Gauge Index")
        self.assertContains(resp_guest, "timingChart")

        # 2. Authenticated buyer
        self.client.login(username="test_buyer", password="Password123!")
        resp_buyer = self.client.get(reverse("property_detail", args=[self.property.pk]))
        self.assertEqual(resp_buyer.status_code, 200)
        self.assertTrue(resp_buyer.context["show_ml_buyer_intel"])
        self.assertContains(resp_buyer, "Purchase Timing &amp; Future Valuation Horizon")
        self.assertContains(resp_buyer, "Place Escrow Token Deposit")

        # 3. Seller (the proprietor of this property)
        self.client.login(username="test_proprietor", password="Password123!")
        resp_seller = self.client.get(reverse("property_detail", args=[self.property.pk]))
        self.assertEqual(resp_seller.status_code, 200)
        self.assertFalse(resp_seller.context["show_ml_buyer_intel"])
        self.assertTrue(resp_seller.context["is_proprietor"])
        self.assertNotContains(resp_seller, "timingChart")
        self.assertContains(resp_seller, "Registered Proprietor Controls")
        self.assertContains(resp_seller, "Estate Custody &amp; Dossier Management")
        self.assertContains(resp_seller, "Mark Estate as Sold Out")

    def test_sold_property_display_and_restrictions(self):
        """Verify sold property shows SOLD OUT badge, disables escrow reservation, and warns buyer."""
        self.property.status = Property.Status.SOLD
        self.property.save()

        # Detail page check
        self.client.login(username="test_buyer", password="Password123!")
        resp = self.client.get(reverse("property_detail", args=[self.property.pk]))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "ESTATE SOLD OUT / ACQUIRED")
        self.assertContains(resp, "Acquisition Finalized &middot; Sold Out")
        self.assertNotContains(resp, "Place Escrow Token Deposit &rarr;")

        # Card listing check (grayscale styling & sold out badge)
        resp_list = self.client.get(reverse("property_list"))
        self.assertEqual(resp_list.status_code, 200)
        self.assertContains(resp_list, "pp-card-sold")
        self.assertContains(resp_list, "grayscale")
        self.assertContains(resp_list, "SOLD OUT")

    def test_security_prevent_buying_sold_property(self):
        """Verify checkout is blocked if property is already sold."""
        self.property.status = Property.Status.SOLD
        self.property.save()

        self.client.login(username="test_buyer", password="Password123!")
        resp = self.client.get(reverse("payment_checkout_property", args=[self.property.pk]))
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse("property_detail", args=[self.property.pk]))

    def test_security_prevent_self_dealing(self):
        """Verify sellers cannot place escrow reservations on their own listings."""
        self.client.login(username="test_proprietor", password="Password123!")
        resp = self.client.get(reverse("payment_checkout_property", args=[self.property.pk]))
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse("property_detail", args=[self.property.pk]))

    def test_security_payment_completes_and_marks_estate_sold(self):
        """Verify successful escrow payment marks estate as SOLD with tamper-evident HMAC signature."""
        self.client.login(username="test_buyer", password="Password123!")
        
        # Load checkout to generate session idempotency token
        chk_resp = self.client.get(reverse("payment_checkout_property", args=[self.property.pk]))
        idem_token = chk_resp.context["idempotency_key"]

        post_data = {
            "property_id": self.property.pk,
            "payment_type": Payment.PaymentType.ESCROW_DEPOSIT,
            "payment_method": Payment.Method.CARD,
            "amount": "50000",
            "agree_terms": "on",
            "idempotency_key": idem_token,
        }

        resp = self.client.post(reverse("payment_process"), post_data)
        self.assertEqual(resp.status_code, 302)

        # Refresh property from database
        self.property.refresh_from_db()
        self.assertEqual(self.property.status, Property.Status.SOLD)

        # Check Payment record security attributes
        payment = Payment.objects.filter(estate=self.property).latest("created_at")
        self.assertEqual(payment.status, Payment.Status.PAID)
        self.assertIn("HMAC-SHA256:", payment.notes)
        self.assertIn(idem_token, payment.notes)

    def test_security_idempotency_and_rate_limiting(self):
        """Verify order-app security: rate limiting on rapid submit + idempotency deduplication."""
        import time
        self.client.login(username="test_buyer", password="Password123!")
        
        chk_resp = self.client.get(reverse("payment_checkout_property", args=[self.property.pk]))
        idem_token = chk_resp.context["idempotency_key"]

        post_data = {
            "property_id": self.property.pk,
            "payment_type": Payment.PaymentType.ESCROW_DEPOSIT,
            "payment_method": Payment.Method.CARD,
            "amount": "50000",
            "agree_terms": "on",
            "idempotency_key": idem_token,
        }

        # 1. First request succeeds
        resp1 = self.client.post(reverse("payment_process"), post_data)
        self.assertEqual(resp1.status_code, 302)
        initial_count = Payment.objects.filter(estate=self.property).count()
        self.assertEqual(initial_count, 1)

        # 2. Immediate rapid duplicate request within 2s is blocked by OrderRateLimitMiddleware (429)
        rapid_resp = self.client.post(reverse("payment_process"), post_data)
        self.assertEqual(rapid_resp.status_code, 429)

        # 3. Request after rate limit window is deduplicated via Idempotency Token without double charging
        time.sleep(2.1)
        replay_resp = self.client.post(reverse("payment_process"), post_data)
        self.assertEqual(replay_resp.status_code, 302)
        self.assertEqual(Payment.objects.filter(estate=self.property).count(), 1)

    def test_seller_features_strictly_hidden_and_restricted_from_buyer(self):
        """Verify Buyers cannot access seller features (submit, my_listings, seller_analytics) and links are hidden."""
        self.client.login(username="test_buyer", password="Password123!")

        # 1. Navigating to submit_property redirects with restriction error
        resp_submit = self.client.get(reverse("submit_property"), follow=True)
        self.assertRedirects(resp_submit, reverse("buyer_dashboard"))
        self.assertContains(resp_submit, "Access Restricted: Estate listing is reserved exclusively for registered Sellers")

        # 2. Navigating to seller_analytics redirects to buyer_dashboard
        resp_analytics = self.client.get(reverse("seller_analytics"), follow=True)
        self.assertRedirects(resp_analytics, reverse("buyer_dashboard"))
        self.assertContains(resp_analytics, "Access Restricted: Proprietor Analytics is reserved exclusively for registered Sellers")

        # 3. Navigating to my_listings redirects to buyer_dashboard
        resp_listings = self.client.get(reverse("my_listings"), follow=True)
        self.assertRedirects(resp_listings, reverse("buyer_dashboard"))
        self.assertContains(resp_listings, "Access Restricted: Proprietor Listings dashboard is reserved exclusively for registered Sellers")

        # 4. In the home page / base template, + List Estate is NOT present for Buyer
        resp_home = self.client.get(reverse("home"))
        self.assertEqual(resp_home.context["is_buyer"], True)
        self.assertEqual(resp_home.context["is_seller"], False)
        self.assertEqual(resp_home.context["bot_mode"], "buyer")
        self.assertEqual(resp_home.context["bot_name"], "Estate Concierge AI")
        self.assertNotContains(resp_home, "+ List Estate")
        self.assertNotContains(resp_home, "+ List an Estate")

        # 5. User role remains BUYER
        self.buyer.refresh_from_db()
        self.assertEqual(self.buyer.profile.role, UserProfile.Role.BUYER)
