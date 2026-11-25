# Week 08 — Sprint 5: Buyer Checkout Interface

| Student | Roll Number | Course | Evaluator |
| :--- | :--- | :--- | :--- |
| **Dhruv Rajput** | `1024030538` | UCS503 / UCS503P | Ms. Anushka |

**Project:** PropertyPulse (Curated Luxury Real Estate Marketplace & AI Valuation Platform)  
**Primary Focus:** Database Architecture, Backend CRUD & Buyer Barometer UI

---

## Objective
Move the buyer-facing payment interface from planning into implementation by connecting the checkout experience to the payment backend while preserving the existing property discovery and Buyer Barometer experience.

## Work Done
- Reviewed the buyer journey from property details to a payment action and identified the information required before checkout.
- Prepared the checkout interface states for a pending order, payment initiation, successful verification, failed payment and user cancellation.
- Reviewed how property title, buyer-facing amount, payment type and transaction status should be presented.
- Coordinated with Guntaas to align the checkout form with the server-side payment and property identifiers.
- Coordinated with Atiksh to ensure the UI displays success only after the backend confirms the verified payment status.
- Kept search, property details, saved properties and Buyer Barometer pages in the regression checklist.

## Outcome
The buyer checkout interface requirements and backend integration points are defined for implementation. The browser flow must not be considered complete until it is tested with Razorpay test credentials and server-verified status.

## Issues / Follow-up
- Connect the checkout button to the order-creation endpoint.
- Display clear pending, success, failure and cancellation messages.
- Avoid trusting client-submitted amounts or payment-success flags.
- Test checkout navigation on desktop and mobile-sized screens.
- Re-test existing buyer browsing, filtering and saved-property pages.

## Learning
I learned that a payment UI must clearly communicate the payment state while relying on the backend as the source of truth.
