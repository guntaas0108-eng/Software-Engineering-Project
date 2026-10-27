# Weekly Engineering Journal (7 Weeks)

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
