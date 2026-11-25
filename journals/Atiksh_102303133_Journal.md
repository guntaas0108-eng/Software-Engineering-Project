# Weekly Engineering Journal (Weeks 1 – 11)

**Student Name:** Atiksh  
**Roll Number:** 102303133  
**Role:** Integration, Testing & DevOps  
**Project:** EstatePulse / PropertyPulse (UCS503P)  

---

# Week 1 – Repository & CI Setup


## Objective
Establish a repeatable development and verification workflow for the PropertyPulse project.

## Work Done
- Worked with the Git/GitHub repository structure.
- Reviewed the Django project setup and application structure.
- Set up the GitHub Actions CI workflow.
- Configured CI to use Python 3.11.
- Configured a PostgreSQL service for CI execution.
- Added dependency installation and `flake8` linting to the workflow.
- Added Django migration and test execution to CI.

## Outcome
The repository had an automated workflow that could check code quality, database migrations and tests after pushes or pull requests.

## Learning
I learned how CI can automatically validate a Django project instead of relying only on manual testing.

---

# Week 2 – Sprint 2 Integration & Testing


## Objective
Integrate the seller/authentication work and verify the existing MVP functionality.

## Work Done
- Integrated the authentication, seller dashboard and property-management changes.
- Tested registration and login flows.
- Tested seller property creation, editing and deletion.
- Tested ownership-based access to seller listings.
- Reviewed duplicate-check behavior and its persisted property flag.
- Ran Django tests and checked the CI workflow for failures.
- Coordinated fixes where changes in one module affected another.

## Outcome
Sprint 2 functionality was integrated and checked before moving to the buyer-side Sprint 3 work.

## Learning
I learned the importance of regression testing after backend changes because a new feature can affect previously working routes.

---

# Week 3 – Sprint 3 Integration & Testing


## Objective
Integrate and test the buyer dashboard, search/filtering and saved-property functionality.

## Work Done
- Integrated the buyer dashboard with the property and saved-property backend.
- Tested property search by title/locality/city.
- Tested category filtering.
- Tested minimum and maximum price filters.
- Tested property-detail navigation.
- Tested save and unsave operations.
- Tested the Saved Properties dashboard.
- Checked that existing seller and authentication flows continued to work after Sprint 3 changes.
- Reviewed automated tests and CI results.

## Outcome
The major Sprint 3 buyer-side flows were integrated with the existing seller, authentication and ML functionality.

## Learning
I learned how end-to-end testing is useful when multiple Django apps and user flows interact with the same database.

---

# Week 4 – UI Integration, Regression Testing & CI


## Objective
Verify the redesigned interface without changing the established backend functionality.

## Work Done
- Integrated the frontend redesign with the existing Django routes and templates.
- Checked navigation across home, listings, details, saved properties and seller pages.
- Performed regression checks for authentication, CRUD, search/filtering and save/unsave functionality.
- Reviewed the logout flow after the Django 5+ POST logout change.
- Checked that the ML prediction flow remained connected to property submission/editing.
- Ran Django tests and CI checks.
- Reported integration issues and verified fixes with the team.

## Outcome
The redesigned UI remained connected to the existing Sprint 3 backend and the main user flows were regression-tested.

## Learning
I learned that frontend changes should be validated against backend behavior rather than tested only visually.

---

# Week 5 – Sprint 4 Targeted Integration & CI Checks

## Objective
Provide focused integration and CI support for the Sprint 4 chat and appointment workflows, complementing the main feature implementation performed by the frontend and backend owners.

## Work Done
- Reviewed the Django Channels/WebSocket configuration used by the chat flow.
- Helped coordinate a concise end-to-end test sequence across buyer login, seller login, property-linked chat and an appointment request/response.
- Reviewed automated test and CI status, noting that any outstanding errors must be resolved before reporting a clean run.
- Included regression checks for existing property browsing, saved properties and ML prediction in the test checklist.

## Outcome
Integration checks were scoped to confirm that the new features work with authentication, property context and existing functionality. Real-time delivery and a clean test suite are not considered verified until successful test evidence is available.

## Issues / Follow-up
- Resolve remaining test errors and rerun the relevant suite.
- Test real-time messaging in separate buyer and seller sessions with the configured ASGI/channel-layer setup.
- Verify the appointment flow end to end and record actual results.
- Report only test counts and CI status observed after the run.

## Learning
I learned that targeted integration checks help detect cross-module problems, and that test results should be reported from actual runs rather than assumptions.

---

# Week 6 – Sprint 4 Chat Auto-Sync, Appointment Integration & CI Verification

## Objective
Stabilize Sprint 4 chat and appointment workflows by verifying automatic message synchronization, checking end-to-end behavior and preparing the changes for integration testing and CI.

## Work Done
- Investigated the reported chat behavior in which messages appeared in the recipient's browser only after a manual refresh.
- Prepared an updated project package intended to add automatic message synchronization as a fallback when WebSocket delivery is unavailable.
- Defined an end-to-end test sequence for buyer and seller sessions, bidirectional messaging, appointment requests and seller confirmation or decline.
- Recorded the need to run the full Django test suite and resolve any errors before declaring Sprint 4 complete.
- Identified CI and acceptance evidence required before moving to the next sprint.

## Outcome
An updated chat auto-sync package was prepared for local verification. Its behavior has not yet been confirmed on the team's machine; Sprint 4 remains pending successful automated tests and live two-browser testing.

## Issues / Follow-up
- Run Django checks and the full automated test suite, then record actual pass/fail results.
- Test that messages appear in separate buyer and seller sessions without manual refresh.
- Verify appointment requests, status changes and access restrictions end to end.
- Confirm the GitHub Actions workflow result and report only status observed after the run.

## Learning
I learned that WebSocket delivery and fallback synchronization need separate verification. Integration work should preserve authorization, prevent duplicate messages and use actual test evidence before a sprint is marked complete.

---

# Week 7 – Sprint 5: Payment Integration (First 50%)

## Student
Atiksh Gupta — Person 4: Chat, Appointments, Payments & Admin, CI/CD and Testing

## Objective
Implement the initial payment-management and admin foundation for Sprint 5, while tracking what remains before the feature is ready for demonstration.

## Work Done
- Added the initial payment-processing foundation using Razorpay-oriented order creation and signature-verification logic.
- Added payment status/transaction tracking and an initial payment migration.
- Added a basic admin payment dashboard intended to show payment information and summary statistics.
- Integrated payment records with Django admin.
- Added basic admin-access tests and identified the need for a full local test run.

## Outcome
The Sprint 5 package contains an initial payment backend and admin dashboard. The code has not yet been verified end-to-end against Razorpay's sandbox, so the payment feature is still in progress.

## Issues / Follow-up
- Configure test credentials locally without committing secrets.
- Run Django system checks, migrations, and the test suite.
- Build and integrate the buyer-facing checkout and result screens.
- Add webhook/reconciliation handling and broader admin management for users, listings, and appointments.
- Complete end-to-end sandbox testing before marking Sprint 5 complete.

## Learning
Admin visibility is useful for monitoring transactions, but a complete payment feature also requires a buyer checkout flow, server-side verification, failure handling, and end-to-end tests.

---

---

# Week 8 Journal — Sprint 5: Payment Checkout & Verification Integration

## Student
Atiksh Gupta — Person 4: Chat, Appointments, Payments, Admin, CI/CD and Testing

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

---

# Week 9 Journal — Sprint 5: Webhooks, Admin & Payment Reconciliation

## Student
Atiksh Gupta — Person 4: Chat, Appointments, Payments, Admin, CI/CD and Testing

## Objective
Extend payment operations beyond checkout by defining webhook processing, reconciliation and useful admin visibility for payment support.

## Work Done
- Reviewed the need to reconcile browser verification results with provider-side payment events.
- Prepared webhook validation requirements, including raw request-body signature verification and safe handling of repeated events.
- Reviewed payment status transitions and the need to prevent an older or duplicate event from incorrectly overwriting a final status.
- Reviewed the payment admin dashboard fields needed for operational inspection and support.
- Coordinated with Guntaas on transaction identifiers and database constraints, and with Dhruv on buyer-visible payment result states.
- Prepared test cases for valid webhook signatures, invalid signatures, duplicate event delivery and unknown payment references.

## Outcome
Webhook and reconciliation requirements are documented for the payment workflow. They should not be described as operational until the endpoint is implemented, configured and tested with Razorpay test-mode events.

## Issues / Follow-up
- Implement or verify webhook endpoint and secret configuration.
- Make webhook processing idempotent.
- Confirm that webhook events are linked to the correct local payment record.
- Test payment status reconciliation and admin visibility.
- Ensure logs do not expose secrets or sensitive payment data.

## Learning
I learned that payment systems need a reliable server-to-server reconciliation path because a user may close the browser or lose connectivity after completing checkout.

---

# Week 10 Journal — Sprint 5: Admin, CI & End-to-End Testing

## Student
Atiksh Gupta — Person 4: Chat, Appointments, Payments, Admin, CI/CD and Testing

## Objective
Increase integration and QA ownership by preparing a repeatable test plan for payment, appointment, chat and admin workflows and reviewing automated CI coverage.

## Work Done
- Reviewed Django admin registrations and the information required to inspect users, properties, conversations, appointments and payments.
- Prepared role-based access tests for staff dashboards and protected payment receipts.
- Reviewed the CI workflow steps for dependency installation, Django system checks, migration checks and test execution.
- Prepared an end-to-end scenario using separate buyer and seller accounts: property inquiry, chat, appointment request, seller response and payment attempt.
- Coordinated with Guntaas on database integrity and with Haneesh on ML regression checks after backend changes.
- Distinguished tests that are written from tests that have actually been executed, so the report does not overstate completion.

## Outcome
The integration test plan and CI review scope are prepared. CI and end-to-end status remain pending until the workflow and local tests are run and their output is recorded.

## Issues / Follow-up
- Execute the CI workflow and fix actual failures.
- Run migrations and the complete Django test suite on a clean test database.
- Test chat and appointment permissions with multiple user roles.
- Test Razorpay sandbox success, failure, cancellation and webhook scenarios.
- Record test counts, failures and environment versions from the actual run.

## Learning
I learned that a test plan, a test case and a passing test result are different things. Release reporting must be based on executed evidence.

---

# Week 11 Journal — Sprint 5: Release QA & Deployment Handover

## Student
Atiksh Gupta — Person 4: Chat, Appointments, Payments, Admin, CI/CD and Testing

## Objective
Consolidate Sprint 5 testing, release documentation and deployment handover requirements for the integrated PropertyPulse application.

## Work Done
- Prepared a final QA checklist covering authentication, property discovery, seller CRUD, ML prediction, chat, appointments, payments and admin.
- Reviewed production configuration requirements for secret keys, allowed hosts, HTTPS, database credentials, static files and media storage.
- Reviewed the need to keep Razorpay test credentials separate from production credentials and never commit `.env` files.
- Prepared a deployment handover checklist covering environment setup, migrations, static collection, health checks and rollback considerations.
- Coordinated with Guntaas on database migration and backend readiness, Haneesh on model artifact compatibility and Dhruv on buyer-facing acceptance.
- Updated the release evidence requirements so unexecuted sandbox, browser or CI tests remain explicitly marked as pending.

## Outcome
The release QA and deployment handover checklist is prepared. The project should be marked ready only after the integrated application passes its runtime checks and the deployment environment is configured and verified.

## Issues / Follow-up
- Run the full test suite and attach the exact output.
- Verify the production database and media-storage configuration.
- Perform a Razorpay sandbox transaction and verify the resulting local payment record.
- Run deployment checks and health endpoint probes in the target environment.
- Do not report a live deployment unless a real deployed URL has been tested.

## Learning
I learned that release readiness is an evidence-based decision. Secure configuration, repeatable deployment steps and verified end-to-end behavior are all required before handover.
