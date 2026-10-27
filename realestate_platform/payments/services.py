import razorpay
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def razorpay_client():
    key_id = getattr(settings, "RAZORPAY_KEY_ID", "")
    key_secret = getattr(settings, "RAZORPAY_KEY_SECRET", "")
    if not key_id or not key_secret:
        raise ImproperlyConfigured("Set RAZORPAY_KEY_ID and RAZORPAY_KEY_SECRET in the environment.")
    return razorpay.Client(auth=(key_id, key_secret))
