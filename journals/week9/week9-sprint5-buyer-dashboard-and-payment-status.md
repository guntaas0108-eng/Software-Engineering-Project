# Week 9 Journal — Sprint 5: Buyer Dashboard & Payment Status

## Student
Dhruv Rajput — Person 3: Frontend, Buyer & Buyer Barometer

## Objective
Improve the buyer dashboard so users can understand their saved properties, appointment requests and payment history without confusing pending payments with completed transactions.

## Work Done
- Reviewed the buyer dashboard sections that display saved listings, appointments and property-related actions.
- Prepared a consistent payment-status presentation for pending, paid, failed, cancelled and refunded transactions.
- Reviewed the information required on a payment result/receipt view, including reference number, amount, currency, property or appointment context and date.
- Coordinated with Guntaas on the buyer-specific records returned by the backend.
- Coordinated with Atiksh on the status values and receipt access rules so the frontend uses the server's verified payment state.
- Included regression checks for the Buyer Barometer labels and the property detail valuation display.

## Outcome
The buyer-facing status and dashboard requirements are documented for integration. Receipt and transaction displays remain subject to backend permissions and actual payment verification.

## Issues / Follow-up
- Connect dashboard cards to real buyer-specific database records.
- Ensure failed or cancelled attempts are not displayed as successful payments.
- Test that one buyer cannot view another buyer's receipt or appointment details.
- Verify empty states when the buyer has no saved properties, appointments or payments.
- Confirm that displayed valuation and payment amounts use consistent currency formatting.

## Learning
I learned that dashboards should represent the true state of backend records and handle empty or failed states as carefully as successful ones.
