# Week 2 – Dataset Preprocessing

**Name:** Haneesh (1024030112)  
**Role:** Machine Learning, Dataset & Authentication/CRUD  

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
