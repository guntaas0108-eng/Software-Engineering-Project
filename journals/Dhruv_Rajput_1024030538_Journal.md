# Weekly Engineering Journal (5 Weeks)

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
