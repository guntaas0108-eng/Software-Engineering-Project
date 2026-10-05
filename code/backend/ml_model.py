import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
import os

class RealEstatePricePredictor:
    """
    Multiple Linear Regression Model for Real Estate Valuation.
    Implements:
       y_hat = beta_0 + beta_1*x_1 + ... + beta_n*x_n
       MSE = (1/n) * sum((y_i - y_hat_i)^2)
    """

    CATEGORIES = ["Residential", "Commercial", "Apartment", "Villa", "Entertainment"]
    CITIES = ["Patiala", "Chandigarh", "Mohali", "Delhi NCR", "Bangalore", "Mumbai"]
    FURNISHING = ["Unfurnished", "Semi-Furnished", "Fully-Furnished"]

    # Base market weights for synthetic generation / reference
    CITY_MULTIPLIERS = {
        "Patiala": 1.0,
        "Chandigarh": 1.45,
        "Mohali": 1.25,
        "Delhi NCR": 1.75,
        "Bangalore": 1.85,
        "Mumbai": 2.30
    }

    CATEGORY_BASE_PSF = {
        "Residential": 4500,
        "Commercial": 7200,
        "Apartment": 5200,
        "Villa": 6800,
        "Entertainment": 6000
    }

    def __init__(self):
        self.model = LinearRegression()
        self.feature_names = []
        self.metrics = {
            "mse": 0.0,
            "mae": 0.0,
            "r2_score": 0.0,
            "training_samples": 0
        }
        self.is_trained = False

    def _extract_feature_vector(self, item):
        """Convert a property dictionary into a numeric vector matching self.feature_names."""
        area = float(item.get("area_sqft", 1000))
        beds = float(item.get("bedrooms", 2))
        baths = float(item.get("bathrooms", 2))
        age = float(item.get("property_age", 5))
        parking = 1.0 if item.get("has_parking") in [1, True, "1", "true", "True"] else 0.0

        vec = [area, beds, baths, age, parking]

        # One-hot encode property_type
        ptype = item.get("property_type", "Residential")
        for cat in self.CATEGORIES:
            vec.append(1.0 if ptype == cat else 0.0)

        # One-hot encode city
        city = item.get("city", "Patiala")
        for c in self.CITIES:
            vec.append(1.0 if city == c else 0.0)

        # One-hot encode furnishing
        furn = item.get("furnishing", "Semi-Furnished")
        for f in self.FURNISHING:
            vec.append(1.0 if furn == f else 0.0)

        return vec

    def _build_feature_names(self):
        names = ["area_sqft", "bedrooms", "bathrooms", "property_age", "has_parking"]
        for cat in self.CATEGORIES:
            names.append(f"type_{cat}")
        for c in self.CITIES:
            names.append(f"city_{c}")
        for f in self.FURNISHING:
            names.append(f"furnishing_{f}")
        return names

    def generate_seed_dataset(self, n_samples=300, random_seed=42):
        """Generate a realistic training dataset for educational demonstration."""
        rng = np.random.default_rng(random_seed)
        data = []

        for _ in range(n_samples):
            cat = rng.choice(self.CATEGORIES)
            city = rng.choice(self.CITIES)
            furn = rng.choice(self.FURNISHING)
            has_park = rng.choice([0, 1])

            if cat == "Apartment":
                area = rng.integers(550, 2400)
                beds = int(rng.choice([1, 2, 3, 4]))
                baths = max(1, beds - rng.choice([0, 1]))
            elif cat == "Villa":
                area = rng.integers(1800, 5500)
                beds = int(rng.choice([3, 4, 5, 6]))
                baths = beds
            elif cat == "Commercial":
                area = rng.integers(800, 6000)
                beds = 0
                baths = int(rng.choice([1, 2, 3]))
            elif cat == "Entertainment":
                area = rng.integers(1200, 7000)
                beds = 0
                baths = int(rng.choice([2, 4, 6]))
            else:  # Residential
                area = rng.integers(800, 3200)
                beds = int(rng.choice([2, 3, 4]))
                baths = max(1, beds - rng.choice([0, 1]))

            age = int(rng.integers(0, 25))

            # Base valuation formula + market dynamics + realistic random noise
            base_psf = self.CATEGORY_BASE_PSF.get(cat, 5000)
            city_mult = self.CITY_MULTIPLIERS.get(city, 1.0)
            furn_bonus = 300000 if furn == "Fully-Furnished" else (150000 if furn == "Semi-Furnished" else 0)
            park_bonus = 200000 if has_park else 0
            age_deprec = max(0.65, 1.0 - (age * 0.015))

            raw_price = (area * base_psf * city_mult * age_deprec) + (beds * 180000) + furn_bonus + park_bonus
            noise = rng.normal(0, raw_price * 0.06)
            final_price = round(max(500000, raw_price + noise), -4)

            data.append({
                "area_sqft": area,
                "bedrooms": beds,
                "bathrooms": baths,
                "property_age": age,
                "has_parking": has_park,
                "property_type": cat,
                "city": city,
                "furnishing": furn,
                "actual_price": float(final_price)
            })

        return data

    def train(self, dataset=None):
        """Train the multiple linear regression model and compute evaluation metrics."""
        if dataset is None or len(dataset) == 0:
            dataset = self.generate_seed_dataset()

        self.feature_names = self._build_feature_names()
        X = [self._extract_feature_vector(row) for row in dataset]
        y = [row["actual_price"] for row in dataset]

        X_arr = np.array(X)
        y_arr = np.array(y)

        self.model.fit(X_arr, y_arr)
        preds = self.model.predict(X_arr)

        mse = float(mean_squared_error(y_arr, preds))
        mae = float(mean_absolute_error(y_arr, preds))
        r2 = float(r2_score(y_arr, preds))

        self.metrics = {
            "mse": round(mse, 2),
            "mae": round(mae, 2),
            "rmse": round(float(np.sqrt(mse)), 2),
            "r2_score": round(r2, 4),
            "training_samples": len(dataset),
            "intercept": round(float(self.model.intercept_), 2)
        }
        self.is_trained = True
        return self.metrics

    def predict(self, property_dict):
        """
        Predict property price and evaluate Buyer Barometer indicators.
        """
        if not self.is_trained:
            self.train()

        vec = self._extract_feature_vector(property_dict)
        pred_val = float(self.model.predict([vec])[0])
        pred_val = max(300000.0, round(pred_val, -3))

        listed_price = float(property_dict.get("price") or property_dict.get("actual_price") or pred_val)

        # Buyer Barometer logic
        # diff% = ((listed_price - predicted_price) / predicted_price) * 100
        diff_pct = round(((listed_price - pred_val) / pred_val) * 100.0, 1)

        # Normalized Barometer Score: 0 (most overpriced) to 100 (best bargain)
        # 50 = fair value, 80+ = great deal, < 30 = overpriced
        barometer_score = max(5, min(98, int(50 - (diff_pct * 1.8))))

        if diff_pct <= -10.0:
            verdict = "Great Deal"
            badge_class = "barometer-good"
            advice = "Priced below estimated market value. High buyer value!"
        elif diff_pct <= 10.0:
            verdict = "Fair Market Price"
            badge_class = "barometer-fair"
            advice = "Accurately aligned with current market expectations."
        else:
            verdict = "Premium / High"
            badge_class = "barometer-high"
            advice = "Listed at a premium. Recommended to negotiate during chat."

        return {
            "predicted_price": pred_val,
            "listed_price": listed_price,
            "difference_percentage": diff_pct,
            "barometer_score": barometer_score,
            "barometer_verdict": verdict,
            "badge_class": badge_class,
            "advice": advice
        }
