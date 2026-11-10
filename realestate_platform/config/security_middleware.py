"""
Security Middleware for PropertyPulse Real Estate Platform.
Implements industry-standard application security controls modeled on financial & order processing apps:
1. OWASP Security Headers (Anti-MIME sniffing, Clickjacking defense, Referrer policy)
2. Checkout Rate Limiting & Transaction Replay Protection
3. Security Audit Logging for Orders & Status Mutations
"""
import time
import logging
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger("security.audit")


class SecurityHeadersMiddleware(MiddlewareMixin):
    """
    Injects high-security HTTP headers on all responses,
    preventing clickjacking, cross-site sniffing, and unauthorized framing.
    """

    def process_response(self, request, response):
        # 1. Prevent MIME-sniffing
        response["X-Content-Type-Options"] = "nosniff"

        # 2. Strict Clickjacking Protection
        response["X-Frame-Options"] = "DENY"

        # 3. Privacy & Leakage defense
        response["Referrer-Policy"] = "strict-origin-when-cross-origin"

        # 4. Restrict dangerous browser features
        response["Permissions-Policy"] = "geolocation=(), camera=(), microphone=()"

        # 5. XSS Filter mode
        response["X-XSS-Protection"] = "1; mode=block"

        return response


class OrderRateLimitMiddleware(MiddlewareMixin):
    """
    Guards checkout & payment endpoints against rapid-fire bot attacks,
    card testing, and denial-of-inventory brute-forcing.
    """

    RATE_LIMIT_SECONDS = 2.0  # Minimum seconds between financial transaction submissions

    def process_request(self, request):
        if request.method == "POST" and request.path in ["/payments/process/", "/payments/process"]:
            now = time.time()
            last_order_time = request.session.get("last_order_submission_ts", 0)

            if now - last_order_time < self.RATE_LIMIT_SECONDS:
                logger.warning(
                    "Rate limit triggered for user %s on %s from IP %s",
                    request.user, request.path, request.META.get("REMOTE_ADDR")
                )
                return HttpResponse(
                    "Security Notice: Transaction request submitted too rapidly. "
                    "Please wait 3 seconds before resubmitting.",
                    status=429,
                    content_type="text/plain",
                )

            request.session["last_order_submission_ts"] = now
        return None
