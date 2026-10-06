# Week 2 – Property Models & Migrations

**Name:** Dhruv Rajput (1024030538)  
**Role:** Database Architecture & Backend CRUD  

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
