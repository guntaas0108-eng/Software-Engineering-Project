# Week 3 – ML Pipeline Development

**Name:** Haneesh (1024030112)  
**Role:** Machine Learning, Dataset & Authentication/CRUD  

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
