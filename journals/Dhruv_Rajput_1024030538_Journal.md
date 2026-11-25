# Weekly Engineering Journal (Weeks 1 – 11)

**Student Name:** Dhruv Rajput  
**Roll Number:** 1024030538  
**Role:** Database Architecture & Backend CRUD  
**Project:** EstatePulse / PropertyPulse (UCS503P)  

---

# Week 1 – Database Design


## Objective
Design the database structure required by the PropertyPulse marketplace.

## Work Done
- Studied the project requirements and identified the core property data that must be stored.
- Planned the `Property` entity and its relationship with the authenticated seller.
- Planned storage for property images.
- Planned the buyer-to-property saved relationship required for the buyer dashboard.
- Reviewed how predicted price and listing information would be stored with a property.
- Chose Django models and the Django ORM as the main database-access approach.

## Outcome
The project had a clear database structure for property listings, users, images and saved properties.

## Learning
I learned how application requirements are converted into database entities and relationships before implementation.

---

# Week 2 – Property Models & Migrations


## Objective
Implement the core database structure using Django models.

## Work Done
- Implemented the `Property` model for listing information.
- Included fields for title, category, locality, city, area, bedrooms, bathrooms, age, listed price, predicted price, seller, status and timestamps.
- Worked with `PropertyImage` for storing images associated with listings.
- Implemented the `SavedProperty` model for the buyer-property relationship.
- Added a timestamp to saved-property records.
- Added a uniqueness constraint so the same buyer cannot create duplicate saved records for the same property.
- Created and applied migrations for the database changes.
- Verified database operations through Django ORM.

## Outcome
The main property and saved-property database structures were available to the application.

## Learning
I learned how Django models map to database tables and how migrations keep the database schema synchronized with the code.

---

# Week 3 – Backend CRUD & Ownership


## Objective
Implement and verify backend property-management operations.

## Work Done
- Worked on Create, Read, Update and Delete operations for property listings.
- Connected newly created properties with the authenticated seller.
- Added ownership-based lookups for editing and deleting properties.
- Worked on retrieving individual property details.
- Supported image storage through `PropertyImage`.
- Worked with the duplicate-check result stored against a property.
- Coordinated with the ML component so predicted price can be stored with the property record.

## Outcome
Seller property management was backed by the database and ownership rules.

## Learning
I learned how backend ownership checks can prevent a logged-in seller from editing or deleting another seller's listing.

---

# Week 4 – Search & Saved-Property Integration


## Objective
Support buyer discovery and saved-property data through backend queries.

## Work Done
- Worked on property-list retrieval using Django ORM queries.
- Supported search across title, locality and city.
- Supported category filtering.
- Supported minimum and maximum listed-price filtering.
- Worked with the `SavedProperty` relationship for buyer-specific saved listings.
- Supported save/unsave operations through database create/delete operations.
- Verified that the buyer dashboard retrieves properties saved by the current user.
- Coordinated with the frontend member to ensure the database-backed results were displayed correctly.

## Outcome
The backend and database supported the Sprint 3 buyer discovery and saved-property workflow.

## Learning
I learned how Django ORM queries can combine filtering and user-specific relationships without requiring raw SQL for the normal application flow.

---

# Week 5 – Sprint 4 Core Conversation & Appointment Backend

## Objective
Maintain ownership of the core backend and database structures for Sprint 4 messaging and site-visit appointments, coordinating with Haneesh on validation and authorization checks.

## Work Done
- Focused on the core conversation, message and appointment model relationships needed to associate the buyer, seller and property.
- Reviewed persistence requirements for message content, timestamps/read tracking and appointment status transitions.
- Maintained responsibility for the core database schema, migrations and backend routes/views associated with these workflows.
- Coordinated with Haneesh, who is taking additional responsibility for appointment-input validation and participant access-control verification.
- Kept existing property CRUD, ownership checks, search/filter and `SavedProperty` behavior in the regression checklist.

## Outcome
The backend/database work defines the core data and route responsibilities for chat and appointments, while validation and permission checks are shared with Haneesh. Migration and workflow correctness must be confirmed on the current checkout before being reported as complete.

## Issues / Follow-up
- Apply migrations on a clean database and verify the schema.
- Test message persistence, participant permissions and appointment status changes.
- Confirm that buyer requests and seller responses store the expected timestamps.
- Coordinate validation and access-control tests with Haneesh and record actual results.

## Learning
I learned the importance of keeping clear ownership of the core data model while coordinating validation and permission checks across the team.

---

# Week 6 – Sprint 4 Message Synchronization & Backend Verification

## Objective
Stabilize the Django backend for Sprint 4 messaging and appointments by verifying message retrieval, conversation permissions, database consistency and appointment status handling.

## Work Done
- Reviewed the reported message-sync issue where the recipient's browser displayed new messages only after a manual refresh.
- Identified backend checks for retrieving newly created messages while ensuring that only conversation participants can access them.
- Reviewed the need to preserve message timestamps/read tracking and appointment status transitions during the synchronization update.
- Prepared to verify database migrations and Django system checks before accepting the updated Sprint 4 changes.
- Kept existing property CRUD, ownership checks, search/filter and saved-property behavior in the regression checklist.

## Outcome
Backend verification points for the chat synchronization fix and appointment workflow are documented. Migration correctness, permission behavior and automated test results remain pending until run against the updated project.

## Issues / Follow-up
- Run Django system checks and verify migrations on the current project checkout.
- Test message persistence, participant permissions and retrieval of newly created messages.
- Confirm that buyer requests and seller responses preserve the expected appointment status and timestamps.
- Run the automated test suite and record the actual output, including any remaining failures.

## Learning
I learned that reliable messaging depends on both the backend data/access rules and the way the frontend retrieves updates. Automatic synchronization must not weaken conversation permissions or duplicate stored messages.

---

# Week 7 – Sprint 5: Payment Integration (First 50%)

## Student
Dhruv Rajput — Person 3: Frontend, Buyer & Buyer Barometer

## Objective
Plan the buyer-facing interface required to connect the existing buyer experience to the new payment backend.

## Work Done
- Identified the buyer checkout page as a remaining Sprint 5 requirement.
- Listed the UI states required for the payment flow: checkout, successful payment, failed payment, and cancellation.
- Identified the need to show the buyer clear payment status and relevant appointment/payment details.
- Kept the existing buyer property browsing and Buyer Barometer features in scope for regression testing.

## Outcome
The buyer-facing payment UI requirements have been outlined. The checkout and payment result screens are still pending and should not be treated as completed.

## Issues / Follow-up
- Build the buyer checkout page and connect it to the backend order-creation flow.
- Display success, failure, and cancellation states clearly.
- Test the buyer flow in a separate browser session and verify that existing buyer pages still work.
- Ensure the interface never treats a payment as successful based only on a client-side message.

## Learning
A payment interface must communicate each possible result clearly and rely on server-verified payment status rather than trusting the browser alone.

---

---

# Week 8 Journal — Sprint 5: Buyer Checkout Interface

## Student
Dhruv Rajput — Person 3: Frontend, Buyer & Buyer Barometer

## Objective
Move the buyer-facing payment interface from planning into implementation by connecting the checkout experience to the payment backend while preserving the existing property discovery and Buyer Barometer experience.

## Work Done
- Reviewed the buyer journey from property details to a payment action and identified the information required before checkout.
- Prepared the checkout interface states for a pending order, payment initiation, successful verification, failed payment and user cancellation.
- Reviewed how property title, buyer-facing amount, payment type and transaction status should be presented.
- Coordinated with Guntaas to align the checkout form with the server-side payment and property identifiers.
- Coordinated with Atiksh to ensure the UI displays success only after the backend confirms the verified payment status.
- Kept search, property details, saved properties and Buyer Barometer pages in the regression checklist.

## Outcome
The buyer checkout interface requirements and backend integration points are defined for implementation. The browser flow must not be considered complete until it is tested with Razorpay test credentials and server-verified status.

## Issues / Follow-up
- Connect the checkout button to the order-creation endpoint.
- Display clear pending, success, failure and cancellation messages.
- Avoid trusting client-submitted amounts or payment-success flags.
- Test checkout navigation on desktop and mobile-sized screens.
- Re-test existing buyer browsing, filtering and saved-property pages.

## Learning
I learned that a payment UI must clearly communicate the payment state while relying on the backend as the source of truth.

---

# Week 9 Journal — Sprint 5: Buyer Dashboard & Payment Status

## Student
Dhruv Rajput — Person 3: Frontend, Buyer & Buyer Barometer

## Objective
Improve the buyer dashboard so users can understand their saved properties, appointment requests and payment history without confusing pending payments with completed transactions.

## Work Done
- Reviewed the buyer dashboard sections that display saved listings, appointments and property-related actions.
- Prepared a consistent payment-status presentation for pending, paid, failed, cancelled and refunded transactions.
- Reviewed the information required on a payment result/receipt view, including reference number, amount, currency, property or appointment context and date.
- Coordinated with Guntaas on the buyer-specific records returned by the backend.
- Coordinated with Atiksh on the status values and receipt access rules so the frontend uses the server's verified payment state.
- Included regression checks for the Buyer Barometer labels and the property detail valuation display.

## Outcome
The buyer-facing status and dashboard requirements are documented for integration. Receipt and transaction displays remain subject to backend permissions and actual payment verification.

## Issues / Follow-up
- Connect dashboard cards to real buyer-specific database records.
- Ensure failed or cancelled attempts are not displayed as successful payments.
- Test that one buyer cannot view another buyer's receipt or appointment details.
- Verify empty states when the buyer has no saved properties, appointments or payments.
- Confirm that displayed valuation and payment amounts use consistent currency formatting.

## Learning
I learned that dashboards should represent the true state of backend records and handle empty or failed states as carefully as successful ones.

---

# Week 10 Journal — Sprint 5: Buyer Barometer & Responsive Regression

## Student
Dhruv Rajput — Person 3: Frontend, Buyer & Buyer Barometer

## Objective
Take additional responsibility for buyer experience regression testing while completing the buyer-facing payment and property information screens.

## Work Done
- Reviewed Buyer Barometer states for Great Deal, Fair Price, Above Market and Pending Analysis.
- Checked that the displayed comparison uses the property's listed price and available predicted price rather than a hardcoded frontend value.
- Reviewed responsive layouts for property cards, property details, saved properties, checkout and payment result screens.
- Prepared UI checks for long locality names, missing property images, unavailable predicted valuations and empty search results.
- Coordinated with Haneesh to keep the ML valuation explanation consistent with the model's actual output and documented limitations.
- Coordinated with Guntaas to verify that buyer pages consume the correct property, appointment and payment records.

## Outcome
The buyer-facing regression checklist covers the main discovery, valuation and payment states. Visual and functional acceptance still requires browser testing against the running application.

## Issues / Follow-up
- Test the buyer flow at desktop and mobile viewport sizes.
- Confirm that missing ML predictions display a pending/unavailable state rather than a fabricated price.
- Check search and filter combinations, saved-property actions and navigation back to property details.
- Verify that payment result screens refresh from backend status.
- Record screenshots or test evidence only after the actual browser checks are performed.

## Learning
I learned that frontend quality depends on correct data states as much as visual layout. A clear unavailable state is better than displaying a misleading value.

---

# Week 11 Journal — Sprint 5: Buyer Release Acceptance

## Student
Dhruv Rajput — Person 3: Frontend, Buyer & Buyer Barometer

## Objective
Prepare the buyer-facing portion of PropertyPulse for the final demonstration by reviewing the complete buyer journey and documenting release acceptance checks.

## Work Done
- Prepared an end-to-end buyer journey covering registration/login, property search, property details, saved listings, seller contact, appointment request and checkout.
- Reviewed the payment result and receipt presentation for clarity and consistency with backend status.
- Checked that Buyer Barometer explanations do not describe R² or other regression metrics as a percentage accuracy claim.
- Prepared acceptance checks for empty states, validation messages, failed requests and unauthorized access responses.
- Coordinated with Guntaas and Atiksh on buyer-to-backend integration and with Haneesh on the displayed ML valuation and model limitations.
- Documented remaining browser checks that require the integrated local application and test payment credentials.

## Outcome
The buyer release acceptance sequence is documented. The buyer module should be signed off only after the complete flow is exercised with a real test buyer account and the resulting backend records are checked.

## Issues / Follow-up
- Execute the full buyer journey using a separate buyer account.
- Verify checkout and receipt states using Razorpay test mode.
- Confirm that saved-property and appointment data remain private to the logged-in buyer.
- Re-test responsive layout and major navigation links.
- Report any remaining UI defects with the page, steps and observed result.

## Learning
I learned that acceptance testing should follow the user's complete journey rather than checking each page in isolation.
