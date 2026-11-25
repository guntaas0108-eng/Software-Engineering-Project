# Week 07 — Sprint 5: Payment Integration (First 50%)

| Student | Roll Number | Course | Evaluator |
| :--- | :--- | :--- | :--- |
| **Guntaas Singh** | `1024030108` | UCS503 / UCS503P | Ms. Anushka |

**Project:** PropertyPulse (Curated Luxury Real Estate Marketplace & AI Valuation Platform)  
**Primary Focus:** Full-Stack Architecture, Frontend & Buyer Experience, Backend & Escrow

---

## Objective
Contribute to the backend and database foundation needed for Sprint 5 payment processing while preserving existing seller and property functionality.

## Work Done
- Reviewed the payment transaction data requirements, including transaction identifiers and payment status.
- Added/covered the payment database model and its initial migration in the Sprint 5 project package.
- Implemented backend order-creation logic intended to support the Razorpay test-payment flow.
- Added payment status and transaction tracking fields/logic.
- Identified seller and property workflows as existing functionality that must remain unaffected.

## Outcome
The project package contains a backend foundation for storing payment information and initiating a payment order. This work still requires local Django checks and sandbox verification.

## Issues / Follow-up
- Run `python manage.py migrate` and `python manage.py check` locally.
- Verify the payment model and order-creation endpoint with valid test configuration.
- Test that existing seller and property CRUD features still work.
- Do not use live payment credentials during development.

## Learning
Payment processing needs persistent transaction records and server-side validation. A database model and order endpoint alone do not complete the buyer checkout experience.
