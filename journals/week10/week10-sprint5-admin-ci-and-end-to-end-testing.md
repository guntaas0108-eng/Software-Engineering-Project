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
