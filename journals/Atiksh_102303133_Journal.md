# Weekly Engineering Journal (4 Weeks)

**Student Name:** Atiksh  
**Roll Number:** 102303133  
**Role:** Integration, Testing & DevOps  
**Project:** EstatePulse / PropertyPulse (UCS503P)  

---

# Week 1 – Repository & CI Setup


## Objective
Establish a repeatable development and verification workflow for the PropertyPulse project.

## Work Done
- Worked with the Git/GitHub repository structure.
- Reviewed the Django project setup and application structure.
- Set up the GitHub Actions CI workflow.
- Configured CI to use Python 3.11.
- Configured a PostgreSQL service for CI execution.
- Added dependency installation and `flake8` linting to the workflow.
- Added Django migration and test execution to CI.

## Outcome
The repository had an automated workflow that could check code quality, database migrations and tests after pushes or pull requests.

## Learning
I learned how CI can automatically validate a Django project instead of relying only on manual testing.

---

# Week 2 – Sprint 2 Integration & Testing


## Objective
Integrate the seller/authentication work and verify the existing MVP functionality.

## Work Done
- Integrated the authentication, seller dashboard and property-management changes.
- Tested registration and login flows.
- Tested seller property creation, editing and deletion.
- Tested ownership-based access to seller listings.
- Reviewed duplicate-check behavior and its persisted property flag.
- Ran Django tests and checked the CI workflow for failures.
- Coordinated fixes where changes in one module affected another.

## Outcome
Sprint 2 functionality was integrated and checked before moving to the buyer-side Sprint 3 work.

## Learning
I learned the importance of regression testing after backend changes because a new feature can affect previously working routes.

---

# Week 3 – Sprint 3 Integration & Testing


## Objective
Integrate and test the buyer dashboard, search/filtering and saved-property functionality.

## Work Done
- Integrated the buyer dashboard with the property and saved-property backend.
- Tested property search by title/locality/city.
- Tested category filtering.
- Tested minimum and maximum price filters.
- Tested property-detail navigation.
- Tested save and unsave operations.
- Tested the Saved Properties dashboard.
- Checked that existing seller and authentication flows continued to work after Sprint 3 changes.
- Reviewed automated tests and CI results.

## Outcome
The major Sprint 3 buyer-side flows were integrated with the existing seller, authentication and ML functionality.

## Learning
I learned how end-to-end testing is useful when multiple Django apps and user flows interact with the same database.

---

# Week 4 – UI Integration, Regression Testing & CI


## Objective
Verify the redesigned interface without changing the established backend functionality.

## Work Done
- Integrated the frontend redesign with the existing Django routes and templates.
- Checked navigation across home, listings, details, saved properties and seller pages.
- Performed regression checks for authentication, CRUD, search/filtering and save/unsave functionality.
- Reviewed the logout flow after the Django 5+ POST logout change.
- Checked that the ML prediction flow remained connected to property submission/editing.
- Ran Django tests and CI checks.
- Reported integration issues and verified fixes with the team.

## Outcome
The redesigned UI remained connected to the existing Sprint 3 backend and the main user flows were regression-tested.

## Learning
I learned that frontend changes should be validated against backend behavior rather than tested only visually.

---
