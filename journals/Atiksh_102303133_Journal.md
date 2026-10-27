# Weekly Engineering Journal (7 Weeks)

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
