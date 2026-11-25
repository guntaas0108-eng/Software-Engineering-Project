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
