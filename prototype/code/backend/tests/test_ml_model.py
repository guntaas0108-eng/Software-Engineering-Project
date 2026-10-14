import pytest
import os
import sys

# Ensure backend folder is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ml_model import RealEstatePricePredictor

def test_ml_model_initialization_and_training():
    predictor = RealEstatePricePredictor()
    metrics = predictor.train()

    assert predictor.is_trained is True
    assert "mse" in metrics
    assert "mae" in metrics
    assert "r2_score" in metrics
    assert metrics["mse"] > 0
    assert metrics["r2_score"] > 0.5  # High explanatory power for synthetic realistic market data

def test_ml_model_prediction():
    predictor = RealEstatePricePredictor()
    predictor.train()

    prop = {
        "title": "Test 3BHK",
        "property_type": "Apartment",
        "city": "Chandigarh",
        "area_sqft": 1500,
        "bedrooms": 3,
        "bathrooms": 3,
        "property_age": 2,
        "has_parking": 1,
        "furnishing": "Semi-Furnished",
        "price": 10000000
    }

    result = predictor.predict(prop)

    assert "predicted_price" in result
    assert result["predicted_price"] > 1000000
    assert "barometer_score" in result
    assert "barometer_verdict" in result
    assert result["barometer_verdict"] in ["Great Deal", "Fair Market Price", "Premium / High"]

def test_buyer_barometer_discount_logic():
    predictor = RealEstatePricePredictor()
    predictor.train()

    # Price deliberately below fair value
    cheap_prop = {
        "property_type": "Villa",
        "city": "Chandigarh",
        "area_sqft": 3000,
        "bedrooms": 4,
        "bathrooms": 4,
        "property_age": 1,
        "has_parking": 1,
        "furnishing": "Fully-Furnished",
        "price": 2000000  # Extremely low
    }
    cheap_res = predictor.predict(cheap_prop)
    assert cheap_res["barometer_verdict"] == "Great Deal"
    assert cheap_res["barometer_score"] > 60

    # Price deliberately high
    expensive_prop = {
        **cheap_prop,
        "price": 90000000  # Extremely high
    }
    expensive_res = predictor.predict(expensive_prop)
    assert expensive_res["barometer_verdict"] == "Premium / High"
