# Week 06 — Sprint 4 Chat Auto-Sync, Appointment Integration & CI Verification

| Student | Roll Number | Course | Evaluator |
| :--- | :--- | :--- | :--- |
| **Atiksh Gupta** | `102303133` | UCS503 / UCS503P | Ms. Anushka |

**Project:** PropertyPulse (Curated Luxury Real Estate Marketplace & AI Valuation Platform)  
**Primary Focus:** Integration, WebSocket Chat, Payments, Testing & CI/CD

---

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
