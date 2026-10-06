# Week 4 – ML/Backend Integration & Authentication

**Name:** Haneesh (1024030112)  
**Role:** Machine Learning, Dataset & Authentication/CRUD  

## Objective
Connect the prediction component with property management and contribute to secure user access.

## Work Done
- Reviewed the property submission flow in `properties/views.py`.
- Connected property input fields to the `PricePredictor` interface.
- Ensured prediction errors do not prevent a property listing from being saved; the prediction can remain pending when the model is unavailable.
- Reviewed the edit-property flow so updated property information can also be sent to the predictor.
- Contributed to registration, login and logout using Django authentication.
- Contributed to authorization/ownership handling so a seller can manage their own listings.
- Contributed to property CRUD operations: Create, Read, Update and Delete.

## Outcome
The ML component was connected to the Django property workflow, while authentication and property-management functionality supported controlled user actions.

## Learning
I learned how ML, authentication and CRUD functionality can work together in one Django application without mixing their responsibilities.
