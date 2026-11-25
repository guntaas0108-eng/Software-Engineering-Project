# Weekly Engineering Journal (Weeks 1 – 11)

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

---

# Week 8 Journal — Sprint 5: ML Model Integration & Regression

## Student
Haneesh — Person 1: ML & Dataset

## Objective
Take greater ownership of the machine-learning work during Sprint 5 by verifying that the trained property-price model is correctly integrated with the Django application and remains independent of the payment workflow.

## Work Done
- Reviewed the current ML prediction path from property-form inputs through feature preparation, model loading, prediction and storage of the predicted price.
- Checked the expected seven model inputs: `area_sqft`, `bedrooms`, `bathrooms`, `age_years`, `category`, `locality` and `city`.
- Reviewed the mapping between the dataset columns (`BuiltUpArea_sqft`, `BHK`, `Bathrooms`, `AgeYears`, `PropertyType`, `Locality` and `City`) and the application feature names.
- Reviewed the local model artifact and Hugging Face loading/fallback arrangement so the application has a defined local-model path when the remote repository cannot be reached.
- Prepared regression cases for different cities, property categories, areas, bedroom counts and property ages.
- Coordinated with Guntaas to keep payment transaction fields separate from property-price and model-training data.

## Outcome
The ML integration and regression scope is documented around the current model interface and application feature mapping. Prediction values and model metrics must be recorded only after the model is loaded and the relevant tests are executed in the project environment.

## Issues / Follow-up
- Confirm the installed scikit-learn version is compatible with the serialized model artifact.
- Execute the ML tests using the current local model and record the actual outputs.
- Verify that model-loading errors are surfaced clearly and are not hidden by a fixed price.
- Check the effect of unknown city/locality values and document the model's training-data limitations.
- Re-run prediction regression tests after backend and payment changes are integrated.

## Learning
I learned that a trained model is only useful in the application when feature names, feature order, preprocessing and library versions remain compatible. New payment functionality should not alter the ML input or output contract.

---

# Week 9 Journal — Sprint 5: ML Validation & Dataset Quality

## Student
Haneesh — Person 1: ML & Dataset

## Objective
Strengthen the reliability of the property-price prediction feature by focusing on input validation, dataset quality, evaluation methodology and clear communication of prediction limitations.

## Work Done
- Reviewed numerical input boundaries for area, bedrooms, bathrooms and property age.
- Reviewed categorical input consistency for property category, locality and city, including whitespace and capitalization differences.
- Examined the training-data column mapping and identified the need to keep training and inference preprocessing consistent.
- Prepared checks for missing values, invalid numerical values, unseen categories and non-positive property areas.
- Reviewed the evaluation measures used for regression, including R², MAE, RMSE and MAPE, and documented that R² must not be described as prediction accuracy.
- Coordinated with Guntaas on backend validation so invalid property details are rejected before being sent to the predictor.

## Outcome
A focused ML data-quality and validation checklist is prepared for the integrated application. No new model-performance claim is made in this journal; metrics must be taken from an executed evaluation using the current dataset and model artifact.

## Issues / Follow-up
- Run the training/evaluation script and preserve the exact train-validation split and random seed.
- Record the number of usable training rows and the handling of missing or extreme values.
- Compare model output for representative properties without assuming that two different inputs must always have a particular price ordering.
- Document cities/localities that are absent or poorly represented in the training data.
- Review whether any benchmark or fallback logic is clearly identified as a benchmark rather than an ML prediction.

## Learning
I learned that data validation is part of model quality, not just form validation. A model should communicate uncertainty and coverage limitations instead of presenting unsupported precision.

---

# Week 10 Journal — Sprint 5: ML Testing & Model Documentation

## Student
Haneesh — Person 1: ML & Dataset

## Objective
Expand the ML regression-test coverage and prepare clear technical documentation so the team can maintain, reproduce and explain the property-price prediction workflow.

## Work Done
- Organized test scenarios for model loading, prediction input validation, unknown categories and offline model availability.
- Reviewed the prediction function's exception handling to distinguish invalid user input, missing model artifacts and prediction-time failures.
- Prepared a reproducibility record covering the dataset source, target column, feature mapping, preprocessing pipeline and model serialization format.
- Documented the distinction between model-generated valuation, seller asking price and any city-level benchmark used for comparison.
- Coordinated with Guntaas to verify that property create/edit operations preserve the expected ML feature fields and do not overwrite transaction-related data.
- Prepared regression checks to be rerun after changes to property models, forms or database migrations.

## Outcome
The ML test and documentation structure is prepared for team review. Test execution, current metric values and any claimed improvement remain pending until they are reproduced in the working environment.

## Issues / Follow-up
- Execute the ML test module and capture the exact pass/fail summary.
- Confirm the model artifact can be loaded from a clean environment after installing the pinned dependencies.
- Verify that the application does not silently replace a failed prediction with a misleading value.
- Keep a versioned record of the model artifact and its training configuration.
- Review documentation with the team before the final demonstration.

## Learning
I learned that reproducibility requires more than saving a model file. The dataset version, feature contract, preprocessing and library versions must also be recorded.

---

# Week 11 Journal — Sprint 5: ML Release Readiness & Monitoring

## Student
Haneesh — Person 1: ML & Dataset

## Objective
Prepare the ML component for the project release by checking its compatibility with the final backend, documenting operational limitations and defining post-release regression checks.

## Work Done
- Reviewed the ML predictor's integration points with property creation, property editing and the buyer-facing valuation display.
- Prepared a release checklist for the local model artifact, Hugging Face repository configuration, dependency compatibility and offline fallback behavior.
- Identified prediction inputs and outputs that should be logged safely for debugging without recording secrets or unnecessary personal information.
- Prepared a small representative regression set for Patiala, Hyderabad and other locations present in the dataset, with expected ranges to be confirmed from actual model runs.
- Coordinated with Guntaas on database migration and property-field stability so ML integration remains compatible with seller listing operations.
- Prepared documentation explaining that model estimates are indicative and are not guaranteed market valuations.

## Outcome
The ML release checklist and monitoring considerations are documented. The model should be marked release-ready only after the artifact loads successfully and the regression tests run against the same dependency versions used by the application.

## Issues / Follow-up
- Run final ML tests in the integrated Django environment and attach the actual output to the testing report.
- Verify local and remote model loading paths separately.
- Confirm that model failures produce a clear error state rather than a fabricated valuation.
- Record the final model artifact version and actual evaluation metrics.
- Re-test ML behavior after the final database and deployment configuration changes.

## Learning
I learned that deployment readiness includes model-file availability, version compatibility, observability and clear communication of limitations—not only successful training.
