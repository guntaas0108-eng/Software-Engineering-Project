"""
Sprint 1 — Person 1 (ML & Dataset)

Trains a baseline Multiple Linear Regression model (per the proposal,
section 5.1: y_hat = b0 + b1*x1 + ... + bn*xn) and evaluates it with MSE
(proposal section 5.1 / 6.2 — target: within 10% variance of actual
local prices).

Run this locally or in Google Colab — it is NOT part of the Django app's
runtime. Once you're happy with the metrics, run push_to_hf.py to publish
model.joblib to the Hub, then point the Django app at it (see README.md,
"Adding your trained Hugging Face model").

Expected input CSV columns (adjust FEATURE_COLUMNS below to match your
actual dataset if the names differ):
    area_sqft, bedrooms, bathrooms, age_years, category, locality, city, price

Usage:
    pip install -r requirements-train.txt
    python train_model.py --data properties.csv --out model.joblib
"""
import argparse

import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

FEATURE_COLUMNS = ["area_sqft", "bedrooms", "bathrooms", "age_years", "category", "locality", "city"]
CATEGORICAL_COLUMNS = ["category", "locality", "city"]
TARGET_COLUMN = "price"


def load_data(path):
    df = pd.read_csv(path)
    df = df.dropna(subset=[TARGET_COLUMN])
    missing = [c for c in FEATURE_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Dataset is missing expected column(s): {missing}")
    return df


def build_encoders(df):
    encoders = {}
    for col in CATEGORICAL_COLUMNS:
        df[col] = df[col].astype(str)
        le = LabelEncoder()
        le.fit(df[col])
        df[col] = le.transform(df[col])
        encoders[col] = le
    return df, encoders


def main(data_path, output_path):
    df = load_data(data_path)
    df, encoders = build_encoders(df)

    X = df[FEATURE_COLUMNS].fillna(0)
    y = df[TARGET_COLUMN]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    variance_pct = (rmse / y_test.mean()) * 100

    print(f"MSE:  {mse:,.2f}")
    print(f"RMSE: {rmse:,.2f}")
    print(f"R^2:  {r2:.4f}")
    print(f"Approx. variance vs mean price: {variance_pct:.2f}% (proposal target: <= 10%)")

    bundle = {"model": model, "encoders": encoders, "feature_order": FEATURE_COLUMNS}
    joblib.dump(bundle, output_path)
    print(f"Saved model bundle -> {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="properties.csv")
    parser.add_argument("--out", default="model.joblib")
    args = parser.parse_args()
    main(args.data, args.out)
