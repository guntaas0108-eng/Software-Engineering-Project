# Weekly Engineering Journal (Weeks 1 – 11)

**Student Name:** Guntaas Singh  
**Roll Number:** 1024030108  
**Role:** Frontend & Buyer Experience  
**Project:** EstatePulse / PropertyPulse (UCS503P)  

---

# Week 1 – UI Planning


## Objective
Plan the frontend structure for the PropertyPulse marketplace.

## Work Done
- Studied the overall seller and buyer workflows.
- Planned the main pages required for property discovery and listing.
- Identified the navigation flow between home, property listings, property details and seller/property forms.
- Planned reusable property-card components so the same property information can be displayed consistently.
- Coordinated with the backend members on the template data required by the frontend.

## Outcome
A basic frontend structure was established around the Django templates.

## Learning
I learned how Django templates can be used to render backend data while keeping presentation separate from the application logic.

---

# Week 2 – Property Browsing UI


## Objective
Build the initial interface for viewing and managing property information.

## Work Done
- Worked on property listing templates.
- Developed the initial property-card presentation.
- Added interfaces for property search and filtering.
- Worked on property-detail presentation.
- Coordinated with backend work so the UI uses existing property fields and routes rather than hardcoded data.
- Maintained consistent navigation across the property pages.

## Outcome
Users could browse property listings and move from a listing to its details using the Django frontend.

## Learning
I learned how GET-based search/filter parameters can be represented in a user-friendly interface while remaining connected to backend filtering.

---

# Week 3 – Buyer Dashboard & Saved Properties


## Objective
Develop the buyer-side discovery and saved-property experience.

## Work Done
- Worked on the buyer dashboard interface.
- Added the saved-property presentation.
- Updated property cards and property-detail pages to show the current saved state.
- Worked on the save/unsave controls while coordinating with the backend implementation.
- Improved navigation between property listings, property details and saved properties.
- Ensured the buyer interface remained consistent with the existing Django routes.

## Outcome
The buyer-side interface supported property discovery and access to saved listings.

## Learning
I learned how a frontend component can reflect a user-specific database state, such as whether a buyer has saved a particular property.

---

# Week 4 – Frontend Redesign & Responsive UI


## Objective
Improve the visual quality of the PropertyPulse prototype without changing backend functionality.

## Work Done
- Redesigned the main PropertyPulse landing page.
- Improved the navigation bar and overall page layout.
- Redesigned property cards with clearer visual hierarchy.
- Improved the property details, listing, saved-properties and seller-facing pages.
- Improved login and signup page presentation.
- Added reusable styling and frontend helper/template improvements.
- Improved spacing, typography, buttons, cards and responsive layouts.
- Kept existing URLs and backend functionality unchanged during the redesign.

## Outcome
The application received a more polished real-estate marketplace interface while retaining the existing Sprint 3 functionality.

## Learning
I learned the importance of improving UI/UX without breaking existing backend routes, models and workflows.

---

# Week 5 – Sprint 4 Buyer Dashboard, Chat & Appointment UI

## Objective
Lead the buyer-facing interface work for Sprint 4, focusing on the chat and site-visit experience while keeping the existing property browsing and saved-property features usable.

## Work Done
- Worked on the buyer chat inbox and conversation-thread interface for property-related buyer–seller communication.
- Worked on the appointment booking form/panel so a buyer can request a site visit and see the appointment status returned by the backend.
- Reviewed the buyer dashboard flow and its links to property details, saved properties, conversations and appointments.
- Added or planned clear validation and feedback states for incomplete forms, loading, successful actions, empty lists and failed requests, to be verified in the running application.
- Kept existing search/filter, property detail and saved-property functionality in the UI regression checklist.
- Coordinated with the backend owner so the interface uses the actual appointment and conversation routes/statuses rather than assuming responses.

## Outcome
The frontend contribution centers on the two user-facing Sprint 4 additions—messaging and appointment management—with dashboard continuity and clearer user feedback. End-to-end behavior must be verified on the current project checkout.

## Issues / Follow-up
- Verify chat and appointment routes on the current checkout.
- Test with separate authenticated buyer and seller accounts.
- Confirm that appointment status shown in the UI matches the backend response.
- Check responsive layout and loading, empty, success and error states in the browser.

## Learning
I learned that chat and appointment interfaces need clear state feedback and must be tested against real authenticated sessions and backend responses, not only by rendering templates.

---

# Week 6 – Sprint 4 Buyer Chat Auto-Sync & Appointment UI Verification

## Objective
Improve and verify the buyer-facing chat and site-visit experience, with focus on showing new messages and appointment status changes without requiring a manual page refresh.

## Work Done
- Reproduced the reported issue in which a message sent from one browser appeared in the other browser only after refreshing.
- Reviewed the buyer-facing chat flow and the requirement to update the conversation view without reloading the entire page.
- Prepared a browser test using separate authenticated buyer and seller sessions in Brave and Chrome.
- Identified checks for duplicate messages, message ordering and clear display of appointment status changes.
- Kept existing property search/filter, property details and saved-property features in the UI regression checklist.

## Outcome
The frontend acceptance criteria for automatic message synchronization and appointment-status display are documented. The fix is not considered verified until messages appear in both directions without refreshing in the running application.

## Issues / Follow-up
- Test the updated chat interface with separate buyer and seller accounts.
- Confirm that messages appear without manually refreshing either browser.
- Confirm that appointment status shown to the buyer matches the backend state.
- Check loading, empty, success and error states in the browser and record actual results.

## Learning
I learned that a chat interface needs to update its visible state after new messages arrive; a successful send action alone does not prove that recipient-side synchronization works.

---

# Week 7 – Sprint 5: Payment Integration (First 50%)

## Student
Guntaas Singh — Person 2: Backend, Database & Seller Module

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

---

---

# Week 8 Journal — Sprint 5: Payment Backend & Seller Integration

## Student
Guntaas Singh — Person 2: Backend, Database & Seller Module

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

---

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

---

# Week 10 Journal — Sprint 5: Database, Admin & Seller Operations

## Student
Guntaas Singh — Person 2: Backend, Database & Seller Module

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

---

# Week 11 Journal — Sprint 5: Backend Release & Deployment Readiness

## Student
Guntaas Singh — Person 2: Backend, Database & Seller Module

## Objective
Prepare the backend and database layer for the final project release by consolidating seller, property, appointment and payment integration checks and documenting the remaining deployment requirements.

## Work Done
- Reviewed the backend setup instructions and the required environment variables for local and production execution.
- Prepared a final migration review covering all Django applications and the order in which schema changes should be applied.
- Reviewed production database configuration and identified the need to use environment-based database credentials rather than committing secrets.
- Checked that seller and property operations remain compatible with the payment and appointment relationships.
- Prepared a backend smoke-test sequence covering registration/login, seller listing CRUD, buyer property browsing, appointment creation and payment-record access.
- Coordinated with Haneesh on the final ML feature contract and with Atiksh on test evidence, payment verification and release documentation.

## Outcome
The backend release checklist and local smoke-test sequence are prepared. Deployment readiness remains conditional on successful migration, runtime, authorization and integration tests in the target environment.

## Issues / Follow-up
- Apply migrations and run Django checks in the release environment.
- Verify PostgreSQL configuration if PostgreSQL is selected for production.
- Confirm media uploads and static files are configured separately.
- Test buyer/seller role permissions and payment/appointment access restrictions.
- Record actual CI and runtime test results before signing off the backend.

## Learning
I learned that a release-ready backend needs repeatable migrations, environment-based configuration, consistent authorization and evidence from integrated tests.
