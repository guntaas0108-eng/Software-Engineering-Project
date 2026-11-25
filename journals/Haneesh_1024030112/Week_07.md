# Week 07 — Sprint 5: Payment Integration (First 50%)

| Student | Roll Number | Course | Evaluator |
| :--- | :--- | :--- | :--- |
| **Haneesh** | `1024030112` | UCS503 / UCS503P | Ms. Anushka |

**Project:** PropertyPulse (Curated Luxury Real Estate Marketplace & AI Valuation Platform)  
**Primary Focus:** Machine Learning, Dataset Engineering & Authentication/CRUD

---

## Objective
Support Sprint 5 by checking that the existing ML prediction feature remains compatible with the payment-related changes and identifying any regression risks.

## Work Done
- Reviewed the Sprint 5 scope and identified the ML prediction feature as an existing feature that must continue working after payment changes.
- Listed prediction functionality as part of regression checks for the wider PropertyPulse application.
- Kept the existing dataset and prediction workflow separate from payment transaction data.
- Recorded that model performance and prediction outputs must not be reported as verified without running the relevant tests.

## Outcome
The ML component remains a separate part of the project, and regression verification has been identified as necessary while Sprint 5 is developed.

## Issues / Follow-up
- Run the existing ML prediction tests against the integrated project.
- Confirm the prediction page still works after the Sprint 5 changes.
- Record evaluation metrics only after running the model evaluation.

## Learning
Existing features should be regression-tested whenever a new module is added. Payment records and ML prediction data should have clearly separated responsibilities.
