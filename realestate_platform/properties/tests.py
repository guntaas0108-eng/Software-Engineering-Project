from decimal import Decimal
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Property, SavedProperty

User = get_user_model()


class PropertyModelTests(TestCase):
    def setUp(self):
        self.seller = User.objects.create_user(username="seller1", password="testpass123")

    def _make_property(self, listed_price, predicted_price):
        return Property.objects.create(
            seller=self.seller,
            title="Test Villa",
            locality="Model Town",
            city="Patiala",
            area_sqft=Decimal("1200"),
            listed_price=Decimal(listed_price),
            predicted_price=Decimal(predicted_price) if predicted_price else None,
        )

    def test_barometer_great_deal(self):
        p = self._make_property("4000000", "4500000")
        self.assertEqual(p.barometer_key(), "great")
        self.assertEqual(p.barometer_label(), "Great Deal")

    def test_barometer_fair_price(self):
        p = self._make_property("4400000", "4300000")
        self.assertEqual(p.barometer_key(), "fair")
        self.assertEqual(p.barometer_label(), "Fair Price")

    def test_barometer_above_market(self):
        p = self._make_property("5500000", "4500000")
        self.assertEqual(p.barometer_key(), "above")
        self.assertEqual(p.barometer_label(), "Above Market")

    def test_barometer_pending_without_prediction(self):
        p = self._make_property("4000000", None)
        self.assertEqual(p.barometer_key(), "pending")
        self.assertEqual(p.barometer_label(), "Pending Analysis")


class PropertyListViewTests(TestCase):
    def test_listing_page_loads(self):
        response = self.client.get(reverse("property_list"))
        self.assertEqual(response.status_code, 200)

    def test_listing_page_shows_active_property(self):
        seller = User.objects.create_user(username="seller2", password="testpass123")
        Property.objects.create(
            seller=seller, title="Visible Flat", locality="Urban Estate", city="Patiala",
            area_sqft=Decimal("900"), listed_price=Decimal("2500000"),
        )
        response = self.client.get(reverse("property_list"))
        self.assertContains(response, "Visible Flat")


class PropertySubmitViewTests(TestCase):
    def test_submit_requires_login(self):
        response = self.client.get(reverse("submit_property"))
        self.assertEqual(response.status_code, 302)  # redirected to login


class SellerDashboardTests(TestCase):
    """Sprint 2: my_listings, edit_property, delete_property."""

    def setUp(self):
        self.owner = User.objects.create_user(username="owner", password="testpass123")
        self.other = User.objects.create_user(username="other", password="testpass123")
        self.prop = Property.objects.create(
            seller=self.owner, title="Owner Flat", locality="Model Town", city="Patiala",
            area_sqft=Decimal("1000"), listed_price=Decimal("3000000"),
        )

    def test_my_listings_requires_login(self):
        response = self.client.get(reverse("my_listings"))
        self.assertEqual(response.status_code, 302)

    def test_my_listings_shows_only_own_properties(self):
        self.client.login(username="owner", password="testpass123")
        response = self.client.get(reverse("my_listings"))
        self.assertContains(response, "Owner Flat")

    def test_other_user_cannot_view_edit_form(self):
        self.client.login(username="other", password="testpass123")
        response = self.client.get(reverse("edit_property", args=[self.prop.pk]))
        self.assertEqual(response.status_code, 404)

    def test_owner_can_edit(self):
        self.client.login(username="owner", password="testpass123")
        self.client.post(reverse("edit_property", args=[self.prop.pk]), {
            "title": "Owner Flat Updated", "category": "RES", "locality": "Model Town",
            "city": "Patiala", "area_sqft": "1000", "age_years": "0", "listed_price": "3200000",
            "description": "",
        })
        self.prop.refresh_from_db()
        self.assertEqual(self.prop.title, "Owner Flat Updated")

    def test_other_user_cannot_delete(self):
        self.client.login(username="other", password="testpass123")
        response = self.client.post(reverse("delete_property", args=[self.prop.pk]))
        self.assertEqual(response.status_code, 404)
        self.assertTrue(Property.objects.filter(pk=self.prop.pk).exists())

    def test_owner_can_delete(self):
        self.client.login(username="owner", password="testpass123")
        self.client.post(reverse("delete_property", args=[self.prop.pk]))
        self.assertFalse(Property.objects.filter(pk=self.prop.pk).exists())


class DuplicateFlagTests(TestCase):
    """Sprint 2: duplicate_check result is now persisted, not just flashed."""

    def test_duplicate_flag_set_on_submit(self):
        seller = User.objects.create_user(username="dupuser", password="testpass123")
        original = Property.objects.create(
            seller=seller, title="Sunrise Villa", locality="Model Town", city="Patiala",
            category="RES", area_sqft=Decimal("1200"), listed_price=Decimal("4000000"),
        )
        self.client.login(username="dupuser", password="testpass123")
        self.client.post(reverse("submit_property"), {
            "title": "Sunrise Villa", "category": "RES", "locality": "Model Town",
            "city": "Patiala", "area_sqft": "1200", "age_years": "0", "listed_price": "4100000",
            "description": "",
        })
        newest = Property.objects.filter(seller=seller).exclude(pk=original.pk).first()
        self.assertIsNotNone(newest)
        self.assertEqual(newest.possible_duplicate_of_id, original.pk)


class SearchFilterTests(TestCase):
    """Sprint 3: property_list search/filter (proposal: locality, category, price)."""

    def setUp(self):
        seller = User.objects.create_user(username="s3seller", password="testpass123")
        self.villa = Property.objects.create(
            seller=seller, title="Sunset Villa", locality="Sarabha Nagar", city="Ludhiana",
            category="RES", area_sqft=Decimal("1500"), listed_price=Decimal("5000000"),
        )
        self.office = Property.objects.create(
            seller=seller, title="Downtown Office", locality="Model Town", city="Patiala",
            category="COM", area_sqft=Decimal("800"), listed_price=Decimal("2000000"),
        )

    def test_search_by_query_matches_title_or_locality(self):
        response = self.client.get(reverse("property_list"), {"q": "Sunset"})
        self.assertContains(response, "Sunset Villa")
        self.assertNotContains(response, "Downtown Office")

    def test_filter_by_category(self):
        response = self.client.get(reverse("property_list"), {"category": "COM"})
        self.assertContains(response, "Downtown Office")
        self.assertNotContains(response, "Sunset Villa")

    def test_filter_by_price_range(self):
        response = self.client.get(reverse("property_list"), {"max_price": "3000000"})
        self.assertContains(response, "Downtown Office")
        self.assertNotContains(response, "Sunset Villa")

    def test_invalid_price_filter_does_not_crash(self):
        response = self.client.get(reverse("property_list"), {"min_price": "not-a-number"})
        self.assertEqual(response.status_code, 200)


class SavedPropertyTests(TestCase):
    """Sprint 3: buyer dashboard and the save/unsave toggle."""

    def setUp(self):
        seller = User.objects.create_user(username="s3seller2", password="testpass123")
        self.buyer = User.objects.create_user(username="s3buyer", password="testpass123")
        self.prop = Property.objects.create(
            seller=seller, title="Lakeview Flat", locality="Model Town", city="Patiala",
            area_sqft=Decimal("1100"), listed_price=Decimal("3500000"),
        )

    def test_save_requires_login(self):
        response = self.client.post(reverse("toggle_save_property", args=[self.prop.pk]))
        self.assertEqual(response.status_code, 302)

    def test_save_requires_post_not_get(self):
        self.client.login(username="s3buyer", password="testpass123")
        response = self.client.get(reverse("toggle_save_property", args=[self.prop.pk]))
        self.assertEqual(response.status_code, 405)

    def test_buyer_dashboard_requires_login(self):
        response = self.client.get(reverse("buyer_dashboard"))
        self.assertEqual(response.status_code, 302)

    def test_toggle_save_then_unsave(self):
        self.client.login(username="s3buyer", password="testpass123")
        self.client.post(reverse("toggle_save_property", args=[self.prop.pk]))
        self.assertTrue(SavedProperty.objects.filter(buyer=self.buyer, property=self.prop).exists())

        self.client.post(reverse("toggle_save_property", args=[self.prop.pk]))
        self.assertFalse(SavedProperty.objects.filter(buyer=self.buyer, property=self.prop).exists())

    def test_saved_property_appears_on_dashboard(self):
        self.client.login(username="s3buyer", password="testpass123")
        self.client.post(reverse("toggle_save_property", args=[self.prop.pk]))
        response = self.client.get(reverse("buyer_dashboard"))
        self.assertContains(response, "Lakeview Flat")


class FrontendStaticRegressionTests(TestCase):
    """Regression tests for the redesigned frontend static asset path."""

    def test_static_url_is_root_relative(self):
        from django.conf import settings
        self.assertTrue(settings.STATIC_URL.startswith("/"))

    def test_listing_references_redesigned_stylesheet(self):
        response = self.client.get(reverse("property_list"))
        self.assertContains(response, '/static/css/style.css?v=frontend-redesign-v1')
