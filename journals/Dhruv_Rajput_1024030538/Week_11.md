# Week 11 — Sprint 5: Buyer Release Acceptance

| Student | Roll Number | Course | Evaluator |
| :--- | :--- | :--- | :--- |
| **Dhruv Rajput** | `1024030538` | UCS503 / UCS503P | Ms. Anushka |

**Project:** PropertyPulse (Curated Luxury Real Estate Marketplace & AI Valuation Platform)  
**Primary Focus:** Database Architecture, Backend CRUD & Buyer Barometer UI

---

## Objective
Prepare the buyer-facing portion of PropertyPulse for the final demonstration by reviewing the complete buyer journey and documenting release acceptance checks.

## Work Done
- Prepared an end-to-end buyer journey covering registration/login, property search, property details, saved listings, seller contact, appointment request and checkout.
- Reviewed the payment result and receipt presentation for clarity and consistency with backend status.
- Checked that Buyer Barometer explanations do not describe R² or other regression metrics as a percentage accuracy claim.
- Prepared acceptance checks for empty states, validation messages, failed requests and unauthorized access responses.
- Coordinated with Guntaas and Atiksh on buyer-to-backend integration and with Haneesh on the displayed ML valuation and model limitations.
- Documented remaining browser checks that require the integrated local application and test payment credentials.

## Outcome
The buyer release acceptance sequence is documented. The buyer module should be signed off only after the complete flow is exercised with a real test buyer account and the resulting backend records are checked.

## Issues / Follow-up
- Execute the full buyer journey using a separate buyer account.
- Verify checkout and receipt states using Razorpay test mode.
- Confirm that saved-property and appointment data remain private to the logged-in buyer.
- Re-test responsive layout and major navigation links.
- Report any remaining UI defects with the page, steps and observed result.

## Learning
I learned that acceptance testing should follow the user's complete journey rather than checking each page in isolation.
