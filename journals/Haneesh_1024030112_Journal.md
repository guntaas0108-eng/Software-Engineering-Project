# Weekly Engineering Journal (7 Weeks)

**Student Name:** Haneesh  
**Roll Number:** 1024030112  
**Role:** Machine Learning, Dataset & Authentication/CRUD  
**Project:** EstatePulse / PropertyPulse (UCS503P)  

---

# Week 1 – Project Setup & ML Planning


## Objective
Understand the PropertyPulse requirements and prepare the foundation for the property price prediction component.

## Work Done
- Studied the overall real-estate marketplace workflow.
- Identified property price as the target for the ML component.
- Identified useful property features such as area, bedrooms, bathrooms, property type, locality, city and property age.
- Reviewed the Django project structure and planned how the `ml_predictor` component would connect with the property-submission workflow.
- Prepared the initial training-pipeline structure using Multiple Linear Regression.
- Discussed the ML/backend interface with the team so that prediction could be integrated without coupling the model directly to the UI.

## Outcome
The project had a clear ML component structure and a defined set of inputs for property price prediction.

## Learning
I learned how an ML component can be structured separately inside a Django project and later connected to a web request flow.

---

# Week 2 – Dataset Preprocessing


## Objective
Understand and clean the property training data before model training.

## Work Done
- Loaded `train_part1.csv` and `train_part2.csv` using Pandas.
- Combined the two training files into one training dataset.
- Checked the dataset shape, columns, data types and numerical statistics.
- Checked missing values column by column.
- Checked duplicate records.
- Separated numerical and categorical columns.
- Used median imputation for missing numerical values.
- Used mode imputation for missing categorical values.
- Verified the processed data and saved the result as `preprocessed_train.csv`.

## Outcome
A combined and initially cleaned training dataset was prepared for the ML pipeline.

## Learning
I learned why data quality checks are required before training and why numerical and categorical missing values are handled differently.

---

# Week 3 – ML Pipeline Development


## Objective
Prepare the complete baseline ML training and prediction pipeline.

## Work Done
- Selected the main input features required by the price predictor.
- Prepared categorical encoding using `LabelEncoder` for category, locality and city.
- Implemented an 80:20 train-test split with a fixed random state.
- Prepared Multiple Linear Regression as the baseline model.
- Added evaluation using MSE, RMSE and R².
- Added model serialization using `joblib`, storing the model together with encoders and feature order.
- Worked on `predictor.py` for converting property inputs into the format expected by the trained model.
- Worked on `model_loader.py` so the Django application can obtain the trained model from the configured Hugging Face repository.

## Outcome
The ML component was structured for training, evaluation and prediction and was ready to be connected to the Django property flow.

## Learning
I understood the difference between preparing a training pipeline and having a final refined model. I also learned why the same encoders used during training must be retained for prediction.

---

# Week 4 – ML/Backend Integration & Authentication


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

---

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

---

# Week 6 – Sprint 4 ML Regression & Integration Verification

## Objective
Preserve the existing ML/property-listing workflow while supporting Sprint 4 stabilization, especially verification that chat and appointment changes do not break property valuation.

## Work Done
- Reviewed the existing property submission and editing flows that use the `PricePredictor` and kept them in the regression checklist for the Sprint 4 update.
- Identified checks for the ML prediction inputs, predicted-price handling and behavior when the model is unavailable.
- Coordinated with the team to keep ML integration separate from the chat auto-sync changes and avoid replacing existing prediction behavior.
- Prepared a regression sequence to repeat property listing and price-prediction checks after the updated project is run.
- Recorded that prediction behavior and any test outcomes must be confirmed against the current project checkout before being marked as passed.

## Outcome
The ML regression scope for Sprint 4 stabilization is documented. No new model-accuracy result or successful regression-test result is claimed until the updated project is executed and the checks are observed.

## Issues / Follow-up
- Run property submission/edit tests with the model available and unavailable.
- Verify that prediction inputs and outputs remain compatible with the current property workflow.
- Run the regression checks after the chat auto-sync changes and record actual results.
- Coordinate with the team if any existing ML or property-listing behavior changes.

## Learning
I learned that changes to chat and appointments must be checked against existing features as part of regression testing, even when the ML module itself is not being changed.

---

# Week 7 – Sprint 5: Payment Integration (First 50%)

## Student
Haneesh — Person 1: ML & Dataset

## Objective
Support Sprint 5 by checking that the existing ML prediction feature remains compatible with the payment-related changes and identifying any regression risks.

## Work Done
- Reviewed the Sprint 5 scope and identified the ML prediction feature as an existing feature that must continue working after payment changes.
- Listed prediction functionality as part of regression checks for the wider PropertyPulse application.
- Kept the existing dataset and prediction workflow separate from payment transaction data.
- Recorded that model performance and prediction outputs must not be reported as verified without running the relevant tests.

## Outcome
The ML component remains a separate part of the project, and regression verification has been identified as necessary while Sprint 5 is developed.

## Issues / Follow-up
- Run the existing ML prediction tests against the integrated project.
- Confirm the prediction page still works after the Sprint 5 changes.
- Record evaluation metrics only after running the model evaluation.

## Learning
Existing features should be regression-tested whenever a new module is added. Payment records and ML prediction data should have clearly separated responsibilities.

---
