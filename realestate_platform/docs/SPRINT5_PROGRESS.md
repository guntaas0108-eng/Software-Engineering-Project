# PropertyPulse — Sprint 5 partial implementation (about 50%)

## Included in this hand-off

1. Payment persistence: payment attempt, buyer, appointment, amount in paise, provider IDs, status, timestamps and unique non-empty provider payment ID.
2. Server-created Razorpay orders: the server chooses the configured fee; client-submitted amounts are not accepted. Only the buyer attached to a confirmed appointment can create an order.
3. Server-side signature verification before a payment is marked PAID. A client success callback alone does not mark the payment successful.
4. Staff-only operations dashboard with payment counts, verified revenue, appointment counts and recent payment attempts.
5. Django admin registration and environment-variable placeholders.

## Not completed yet

- Buyer-facing checkout UI and success/failure/cancel pages.
- Webhook endpoint and reconciliation for delayed payment status updates.
- Refunds, duplicate/replay edge-case tests, and end-to-end sandbox test.
- Full admin controls for users/listings/appointments.
- Automated Django test run in this environment (Django is not installed here).

## Setup

1. Merge these files into the existing Sprint 4 project; do not replace the project with an empty folder.
2. Install requirements in the project's virtual environment: `python -m pip install -r requirements.txt`.
3. Copy `.env.example` to `.env` if needed and fill in Razorpay **test-mode** credentials. Keep secrets out of Git.
4. Set `APPOINTMENT_FEE_PAISE` (default 50000 = ₹500.00) to the intended booking fee.
5. Run `python manage.py migrate` and `python manage.py check`.
6. Create a staff user with `python manage.py createsuperuser`.
7. Visit `/payments/admin-dashboard/` as a staff user. Non-staff users should receive a 404.

## Important

This is a partial Sprint 5 implementation, not a production-ready payment system. Test using Razorpay test credentials only. Do not accept real payments until the checkout UI, webhook/reconciliation, automated tests, deployment settings and end-to-end verification are complete.
