# Week 06 — Sprint 4 Buyer Chat Auto-Sync & Appointment UI Verification

| Student | Roll Number | Course | Evaluator |
| :--- | :--- | :--- | :--- |
| **Guntaas Singh** | `1024030108` | UCS503 / UCS503P | Ms. Anushka |

**Project:** PropertyPulse (Curated Luxury Real Estate Marketplace & AI Valuation Platform)  
**Primary Focus:** Full-Stack Architecture, Frontend & Buyer Experience, Backend & Escrow

---

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
