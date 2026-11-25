# Week 08 — Sprint 5: ML Model Integration & Regression

| Student | Roll Number | Course | Evaluator |
| :--- | :--- | :--- | :--- |
| **Haneesh** | `1024030112` | UCS503 / UCS503P | Ms. Anushka |

**Project:** PropertyPulse (Curated Luxury Real Estate Marketplace & AI Valuation Platform)  
**Primary Focus:** Machine Learning, Dataset Engineering & Authentication/CRUD

---

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
