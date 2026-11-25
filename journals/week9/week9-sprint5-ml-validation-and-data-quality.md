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
