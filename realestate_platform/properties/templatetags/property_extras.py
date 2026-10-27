from django import template

register = template.Library()


@register.filter
def count_status(properties, status):
    """Used on the My Listings dashboard stat cards — counts without touching the view."""
    return sum(1 for p in properties if p.status == status)


@register.filter
def count_pending(properties):
    return sum(1 for p in properties if not p.predicted_price)


@register.filter
def with_error_class(field):
    """
    Ensures every field renders with Bootstrap's form-control (or keeps an
    existing form-select), and adds is-invalid on error — purely a
    presentation concern, doesn't touch forms.py.
    """
    css_class = field.field.widget.attrs.get("class", "")
    if "form-control" not in css_class and "form-select" not in css_class:
        css_class = f"{css_class} form-control".strip()
    if field.errors:
        css_class = f"{css_class} is-invalid".strip()
    return field.as_widget(attrs={"class": css_class})
