# Week 08 — Sprint 5: Payment Checkout & Verification Integration

| Student | Roll Number | Course | Evaluator |
| :--- | :--- | :--- | :--- |
| **Atiksh Gupta** | `102303133` | UCS503 / UCS503P | Ms. Anushka |

**Project:** PropertyPulse (Curated Luxury Real Estate Marketplace & AI Valuation Platform)  
**Primary Focus:** Integration, WebSocket Chat, Payments, Testing & CI/CD

---

## Objective
Continue the Sprint 5 payment foundation by integrating the buyer checkout with the Razorpay-oriented backend and strengthening verification and failure handling.

## Work Done
- Reviewed the order-creation and payment-verification endpoints and their expected request/response contracts.
- Coordinated the buyer checkout states with Dhruv and the payment/property relationships with Guntaas.
- Reviewed server-side signature verification requirements and the rule that a browser callback alone must not mark a payment as paid.
- Prepared test scenarios for missing credentials, order-creation errors, invalid signatures, valid signatures and repeated checkout attempts.
- Reviewed admin visibility requirements for payment status, provider order ID, provider payment ID and timestamps.
- Kept the existing chat and appointment workflows in the regression checklist.

## Outcome
The payment integration and verification scenarios are documented for implementation and sandbox testing. Razorpay test-mode completion must be supported by actual callback and database evidence.

## Issues / Follow-up
- Configure test keys through local environment variables only.
- Verify order amount and currency on the server.
- Test valid and invalid signature paths.
- Add or verify webhook handling and idempotent event processing.
- Run Django tests and record actual results.

## Learning
I learned that payment verification must be performed on the server and that retries, failures and duplicate callbacks need explicit handling.
