# Week 9 Journal — Sprint 5: Backend Integrity & Appointment Linking

## Student
Guntaas Singh — Person 2: Backend, Database & Seller Module

## Objective
Strengthen database integrity across property listings, appointments and payment records, with additional responsibility for seller-side appointment and inquiry workflows.

## Work Done
- Reviewed the relationships between `Property`, buyer/seller accounts, conversations, appointments and payment records.
- Examined appointment status transitions and the event-history records used to retain a history of status changes.
- Prepared validation checks for appointment ownership, property ownership, future appointment dates and permitted status transitions.
- Reviewed how appointment-related payments should reference the correct appointment and buyer without creating duplicate or orphaned records.
- Checked seller dashboard requirements for incoming inquiries, appointment requests and property-specific activity.
- Coordinated with Haneesh on validation of property input fields used by the ML predictor, so invalid area or property attributes are rejected before prediction.
- Coordinated with Atiksh on transaction-state updates and the need for server-side verification before a payment is marked successful.

## Outcome
The database-integrity and seller/appointment integration scope is defined. The relationships and state transitions require verification through migrations and tests in the running Django application.

## Issues / Follow-up
- Test buyer-to-seller appointment creation and seller confirmation/rejection using separate accounts.
- Verify that unrelated users cannot view or change another user's appointment or payment.
- Check duplicate appointment and duplicate payment handling under repeated requests.
- Confirm database constraints and transaction handling for concurrent checkout or appointment updates.
- Record migration and test output rather than assuming that schema changes are applied.

## Learning
I learned that related workflows need consistent ownership and state rules. A payment, appointment and property must remain linked to the correct users and records throughout their lifecycle.
