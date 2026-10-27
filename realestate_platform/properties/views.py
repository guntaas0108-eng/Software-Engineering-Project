from decimal import Decimal, InvalidOperation

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST

from .models import Property, PropertyImage, SavedProperty
from .forms import PropertyForm
from .duplicate_check import find_possible_duplicates
from ml_predictor.predictor import PricePredictor

predictor = PricePredictor()


def _to_decimal(value):
    """Safely parse a price filter param — bad input is ignored, not a 500."""
    try:
        return Decimal(value)
    except (InvalidOperation, TypeError, ValueError):
        return None


def home(request):
    """
    UI pass (frontend redesign): marketing landing page at the site root.
    Purely presentational — read-only, reuses the same "what has this buyer
    saved" logic as property_list/buyer_dashboard, just capped to a preview
    of the newest active listings. No new write paths, no changed URLs for
    any existing view.
    """
    featured = Property.objects.filter(status=Property.Status.ACTIVE).prefetch_related("images")[:6]
    saved_ids = set()
    if request.user.is_authenticated:
        saved_ids = set(
            SavedProperty.objects.filter(buyer=request.user).values_list("property_id", flat=True)
        )
    return render(request, "properties/home.html", {
        "featured": featured, "saved_ids": saved_ids, "categories": Property.Category.choices,
    })


@login_required
def submit_property(request):
    if request.method == "POST":
        form = PropertyForm(request.POST)
        if form.is_valid():
            property_obj = form.save(commit=False)
            property_obj.seller = request.user

            # --- ML price prediction (Person 1's model, via Hugging Face) ---
            try:
                property_obj.predicted_price = predictor.predict({
                    "area_sqft": float(property_obj.area_sqft),
                    "bedrooms": property_obj.bedrooms or 0,
                    "bathrooms": property_obj.bathrooms or 0,
                    "age_years": property_obj.age_years,
                    "category": property_obj.category,
                    "locality": property_obj.locality,
                    "city": property_obj.city,
                })
            except Exception:
                # No model configured yet, or the Hub call failed — don't
                # block the listing, just leave the Barometer "Pending".
                property_obj.predicted_price = None

            property_obj.save()

            for f in request.FILES.getlist("images"):
                PropertyImage.objects.create(property=property_obj, image=f)

            duplicates = find_possible_duplicates(property_obj)
            if duplicates:
                property_obj.possible_duplicate_of = duplicates[0]
                property_obj.save(update_fields=["possible_duplicate_of"])
                messages.warning(
                    request,
                    f"Heads up: {len(duplicates)} similar listing(s) already exist nearby."
                )

            return redirect("property_detail", pk=property_obj.pk)
    else:
        form = PropertyForm()
    return render(request, "properties/submit.html", {"form": form})


def property_list(request):
    """
    Sprint 3 (Person 3): buyer-facing discovery — search + filter by
    locality/title, category, and price range (proposal: "Property search
    and filtering"). Filters are read from GET so the URL stays
    bookmarkable/shareable.
    """
    properties = Property.objects.filter(status=Property.Status.ACTIVE).prefetch_related("images")

    query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()
    min_price = request.GET.get("min_price", "").strip()
    max_price = request.GET.get("max_price", "").strip()

    if query:
        properties = properties.filter(
            Q(title__icontains=query) | Q(locality__icontains=query) | Q(city__icontains=query)
        )
    if category:
        properties = properties.filter(category=category)

    min_price_val = _to_decimal(min_price)
    if min_price_val is not None:
        properties = properties.filter(listed_price__gte=min_price_val)

    max_price_val = _to_decimal(max_price)
    if max_price_val is not None:
        properties = properties.filter(listed_price__lte=max_price_val)

    saved_ids = set()
    if request.user.is_authenticated:
        saved_ids = set(
            SavedProperty.objects.filter(buyer=request.user).values_list("property_id", flat=True)
        )

    context = {
        "properties": properties,
        "saved_ids": saved_ids,
        "categories": Property.Category.choices,
        "filters": {"q": query, "category": category, "min_price": min_price, "max_price": max_price},
    }
    return render(request, "properties/listing.html", context)


def property_detail(request, pk):
    property_obj = get_object_or_404(Property, pk=pk)
    is_saved = False
    if request.user.is_authenticated:
        is_saved = SavedProperty.objects.filter(buyer=request.user, property=property_obj).exists()
    return render(request, "properties/detail.html", {"property": property_obj, "is_saved": is_saved})


@login_required
def my_listings(request):
    """Sprint 2 (Person 2): seller dashboard — every listing owned by this user, any status."""
    properties = Property.objects.filter(seller=request.user)
    return render(request, "properties/my_listings.html", {"properties": properties})


@login_required
def edit_property(request, pk):
    """
    Ownership is enforced by filtering on seller=request.user in the lookup
    itself, so another user's listing 404s instead of leaking a 403 that
    would confirm the listing exists.
    """
    property_obj = get_object_or_404(Property, pk=pk, seller=request.user)

    if request.method == "POST":
        form = PropertyForm(request.POST, instance=property_obj)
        if form.is_valid():
            updated = form.save(commit=False)
            try:
                updated.predicted_price = predictor.predict({
                    "area_sqft": float(updated.area_sqft),
                    "bedrooms": updated.bedrooms or 0,
                    "bathrooms": updated.bathrooms or 0,
                    "age_years": updated.age_years,
                    "category": updated.category,
                    "locality": updated.locality,
                    "city": updated.city,
                })
            except Exception:
                pass  # keep the existing predicted_price if the model call fails
            updated.save()

            for f in request.FILES.getlist("images"):
                PropertyImage.objects.create(property=updated, image=f)

            messages.success(request, "Listing updated.")
            return redirect("property_detail", pk=updated.pk)
    else:
        form = PropertyForm(instance=property_obj)
    return render(request, "properties/edit.html", {"form": form, "property": property_obj})


@login_required
def delete_property(request, pk):
    property_obj = get_object_or_404(Property, pk=pk, seller=request.user)
    if request.method == "POST":
        property_obj.delete()
        messages.success(request, "Listing deleted.")
        return redirect("my_listings")
    return render(request, "properties/delete_confirm.html", {"property": property_obj})


@login_required
def buyer_dashboard(request):
    """Sprint 3 (Person 3): the buyer's own view — everything they've saved."""
    properties = Property.objects.filter(saved_by__buyer=request.user).prefetch_related("images")
    saved_ids = set(properties.values_list("pk", flat=True))
    return render(request, "properties/buyer_dashboard.html", {"properties": properties, "saved_ids": saved_ids})


@login_required
@require_POST
def toggle_save_property(request, pk):
    property_obj = get_object_or_404(Property, pk=pk)
    saved, created = SavedProperty.objects.get_or_create(buyer=request.user, property=property_obj)
    if not created:
        saved.delete()
        messages.info(request, "Removed from your saved properties.")
    else:
        messages.success(request, "Saved to your dashboard.")

    next_url = request.POST.get("next") or reverse("property_detail", args=[pk])
    return redirect(next_url)
