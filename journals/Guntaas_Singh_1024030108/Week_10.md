# Week 10 — Sprint 5: Database, Admin & Seller Operations

| Student | Roll Number | Course | Evaluator |
| :--- | :--- | :--- | :--- |
| **Guntaas Singh** | `1024030108` | UCS503 / UCS503P | Ms. Anushka |

**Project:** PropertyPulse (Curated Luxury Real Estate Marketplace & AI Valuation Platform)  
**Primary Focus:** Full-Stack Architecture, Frontend & Buyer Experience, Backend & Escrow

---

## Objective
Take a larger role in backend quality by reviewing database constraints, seller operations, admin data visibility and the reliability of payment-related records.

## Work Done
- Reviewed the database schema and migrations for accounts, properties, chat/appointments and payments.
- Checked important relationships, deletion behavior, nullable references and uniqueness requirements for transaction identifiers.
- Reviewed seller-facing property operations to ensure that only the listing owner or an authorized administrator can edit, archive or delete a listing.
- Examined the data needed by admin screens to review users, properties, appointments and payment status.
- Prepared checks for consistent payment amount storage in paise and display conversion to rupees.
- Coordinated with Atiksh on which payment fields should be read-only in admin and which status changes must be performed only through verified backend workflows.
- Coordinated with Haneesh to ensure database changes do not alter the model feature names or stored predicted-price field.

## Outcome
A database and seller-operations review checklist is prepared for the final Sprint 5 integration. Admin visibility and record integrity should be considered complete only after role-based access and CRUD behavior are tested.

## Issues / Follow-up
- Run `makemigrations --check`, `migrate` and the relevant Django tests.
- Verify that payment identifiers cannot be duplicated where uniqueness is required.
- Test seller ownership restrictions and admin permissions with separate user roles.
- Confirm that payment history remains auditable after a listing is marked sold or archived.
- Check query behavior for seller dashboards and avoid unnecessary repeated database queries.

## Learning
I learned that database integrity and admin permissions are part of the business logic. A correct-looking dashboard is not sufficient unless the underlying records and allowed state transitions are protected.
