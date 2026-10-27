from django.conf import settings
from django.db import models


class Property(models.Model):
    """
    Core listing entity. `listed_price` is what the seller asks for;
    `predicted_price` is filled in by ml_predictor at submission time.
    The Buyer Barometer (proposal section 4.1) compares the two.
    """

    class Category(models.TextChoices):
        RESIDENTIAL = "RES", "Residential"
        COMMERCIAL = "COM", "Commercial"
        ENTERTAINMENT = "ENT", "Entertainment"
        INDUSTRIAL = "IND", "Industrial"
        LAND = "LAND", "Land / Plot"

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        NEGOTIATING = "NEGOTIATING", "Under Negotiation"
        SOLD = "SOLD", "Sold"
        INACTIVE = "INACTIVE", "Inactive"

    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="properties"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=10, choices=Category.choices, default=Category.RESIDENTIAL)
    locality = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    area_sqft = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveSmallIntegerField(null=True, blank=True)
    bathrooms = models.PositiveSmallIntegerField(null=True, blank=True)
    age_years = models.PositiveSmallIntegerField(default=0)

    listed_price = models.DecimalField(max_digits=14, decimal_places=2)
    predicted_price = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)

    status = models.CharField(max_length=15, choices=Status.choices, default=Status.ACTIVE)

    # Sprint 2: persists the duplicate-check result (properties/duplicate_check.py)
    # instead of only surfacing it as a one-time flash message on submit.
    possible_duplicate_of = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )

    # Sprint 1 seed for the "Time-to-appointment" metric (proposal 6.1) —
    # first_message_at / appointment_confirmed_at get added properly in
    # Sprint 4 once the chat/appointment models exist.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} ({self.locality})"

    def barometer_key(self):
        """Machine-friendly key — matches the CSS classes in base.html."""
        if not self.predicted_price:
            return "pending"
        ratio = float(self.listed_price) / float(self.predicted_price)
        if ratio <= 0.95:
            return "great"
        elif ratio <= 1.05:
            return "fair"
        return "above"

    def barometer_label(self):
        """Human-friendly label shown on the Buyer Barometer badge."""
        return {
            "great": "Great Deal",
            "fair": "Fair Price",
            "above": "Above Market",
            "pending": "Pending Analysis",
        }[self.barometer_key()]


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="property_images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.property.title}"


class SavedProperty(models.Model):
    """
    Sprint 3 (Person 3): backs the buyer dashboard — a buyer "saves" a
    listing they're interested in. Modeled as its own entity (not a plain
    M2M) since it carries its own timestamp.
    """
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="saved_properties")
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="saved_by")
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("buyer", "property")
        ordering = ["-saved_at"]

    def __str__(self):
        return f"{self.buyer.username} saved {self.property.title}"
