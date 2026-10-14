# Week 5 – Sprint 4 ML Integration, Appointment Validation & Access Control

## Objective
Maintain the existing ML/property-listing workflow and take additional responsibility for validating Sprint 4 appointment requests and checking access permissions, in coordination with the backend owner.

## Work Done
- Reviewed the existing property submission and editing flows that use the `PricePredictor`, keeping them in the regression checklist while chat and appointment features are added.
- Reviewed the property fields and listing context required to associate an appointment request with the correct property and its buyer/seller.
- Took responsibility for the appointment-validation logic/checks: required fields, valid date/time input and handling invalid or incomplete requests. Any changes must be verified against the current Sprint 4 code before being marked complete.
- Reviewed authorization checks for appointment and conversation actions so only relevant participants can view or act on their records.
- Prepared checks for ML prediction inputs, predicted-price handling, duplicate-listing checks and behavior when the prediction model is unavailable.
- Coordinated with the backend owner on model relationships and existing API/view behavior rather than replacing the core database design.

## Outcome
Week 5 work connects the existing ML and property workflow with the new appointment feature, with Haneesh taking additional responsibility for appointment validation and access-control verification. Completion of each check depends on successful testing against the current project checkout; no new model-accuracy result is claimed.

## Issues / Follow-up
- Run property submission/edit tests with the model available and unavailable.
- Test missing and invalid appointment inputs and confirm that invalid requests are rejected clearly.
- Verify that a buyer or seller cannot access unrelated users' conversations or appointments.
- Record actual test output before reporting these checks as passed.

## Learning
I learned that appointment validation and authorization are important backend responsibilities even when the core data models are maintained by another team member. These checks also need to preserve the existing property and ML workflow.
