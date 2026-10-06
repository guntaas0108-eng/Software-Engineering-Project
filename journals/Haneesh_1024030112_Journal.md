# Weekly Engineering Journal (4 Weeks)

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
