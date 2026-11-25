# Week 11 — Sprint 5: Release QA & Deployment Handover

| Student | Roll Number | Course | Evaluator |
| :--- | :--- | :--- | :--- |
| **Atiksh Gupta** | `102303133` | UCS503 / UCS503P | Ms. Anushka |

**Project:** PropertyPulse (Curated Luxury Real Estate Marketplace & AI Valuation Platform)  
**Primary Focus:** Integration, WebSocket Chat, Payments, Testing & CI/CD

---

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
