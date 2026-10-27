from difflib import SequenceMatcher
from .models import Property


def _similar(a: str, b: str) -> float:
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def find_possible_duplicates(property_obj, threshold=0.8):
    """
    Proposal section 4.2, step 2: "lightweight similarity on text/category
    and approximate location" — intentionally NOT a fuzzy-matching ML
    model, just title similarity within the same locality + category.
    Returns a queryset-like list of candidate duplicate Property objects.
    """
    candidates = Property.objects.filter(
        locality__iexact=property_obj.locality,
        category=property_obj.category,
    ).exclude(pk=property_obj.pk)

    return [c for c in candidates if _similar(property_obj.title, c.title) >= threshold]
