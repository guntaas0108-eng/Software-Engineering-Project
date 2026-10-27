from django import forms
from .models import Property

BOOTSTRAP_INPUT = "form-control"
BOOTSTRAP_SELECT = "form-select"


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            "title", "description", "category", "locality", "city",
            "area_sqft", "bedrooms", "bathrooms", "age_years", "listed_price",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": BOOTSTRAP_INPUT}),
            "description": forms.Textarea(attrs={"class": BOOTSTRAP_INPUT, "rows": 4}),
            "category": forms.Select(attrs={"class": BOOTSTRAP_SELECT}),
            "locality": forms.TextInput(attrs={"class": BOOTSTRAP_INPUT}),
            "city": forms.TextInput(attrs={"class": BOOTSTRAP_INPUT}),
            "area_sqft": forms.NumberInput(attrs={"class": BOOTSTRAP_INPUT}),
            "bedrooms": forms.NumberInput(attrs={"class": BOOTSTRAP_INPUT}),
            "bathrooms": forms.NumberInput(attrs={"class": BOOTSTRAP_INPUT}),
            "age_years": forms.NumberInput(attrs={"class": BOOTSTRAP_INPUT}),
            "listed_price": forms.NumberInput(attrs={"class": BOOTSTRAP_INPUT}),
        }
