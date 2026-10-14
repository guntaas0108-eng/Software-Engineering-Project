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
