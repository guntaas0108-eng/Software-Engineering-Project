# Week 08 — Sprint 5: Payment Backend & Seller Integration

| Student | Roll Number | Course | Evaluator |
| :--- | :--- | :--- | :--- |
| **Guntaas Singh** | `1024030108` | UCS503 / UCS503P | Ms. Anushka |

**Project:** PropertyPulse (Curated Luxury Real Estate Marketplace & AI Valuation Platform)  
**Primary Focus:** Full-Stack Architecture, Frontend & Buyer Experience, Backend & Escrow

---

## Objective
Take a larger backend ownership role in Sprint 5 by connecting the payment foundation with existing property and seller records while preserving seller-side listing operations and ownership rules.

## Work Done
- Reviewed the `Payment` model and its relationships with the buyer, property/estate and appointment records.
- Reviewed the payment status lifecycle (`CREATED`, `PAID`, `FAILED`, `CANCELLED` and `REFUNDED`) and the provider order/payment identifiers stored for reconciliation.
- Examined how payment records should be associated with the correct authenticated buyer and the relevant property or appointment.
- Reviewed seller property creation, editing, deletion and listing-status operations to identify regression risks from payment integration.
- Prepared backend checks to prevent a buyer from creating a payment against a property they do not have permission to access.
- Coordinated with Atiksh on the order-creation and verification service boundaries, and with Dhruv on the data required by buyer checkout screens.

## Outcome
The backend integration responsibilities and data relationships between payments, buyers, properties and appointments are documented for Sprint 5. The complete checkout lifecycle still requires local Django and Razorpay sandbox verification.

## Issues / Follow-up
- Verify payment migrations on a clean database and on a database containing existing property records.
- Confirm that the amount and currency are calculated and validated on the server.
- Test seller property CRUD after payment migrations are applied.
- Ensure payment status changes cannot be made by an ordinary seller or buyer through an unprotected endpoint.
- Review deletion behavior so payment history is retained appropriately when a property or appointment changes.

## Learning
I learned that payment records must be linked to trusted database objects and authenticated users. Backend ownership checks are essential because the browser must not decide which property or amount is being paid for.
