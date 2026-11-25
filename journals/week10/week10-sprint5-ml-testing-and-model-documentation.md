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
