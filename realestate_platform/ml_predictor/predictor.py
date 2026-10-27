import pandas as pd
from .model_loader import load_model


class PricePredictor:
    """Thin wrapper so views.py never touches joblib/HF details directly."""

    def predict(self, features: dict) -> float:
        bundle = load_model()
        model = bundle["model"]
        encoders = bundle.get("encoders", {})
        feature_order = bundle["feature_order"]

        row = {}
        for col in feature_order:
            val = features.get(col)
            if col in encoders:
                val = encoders[col].transform([str(val)])[0] if val is not None else 0
            row[col] = val

        df = pd.DataFrame([row], columns=feature_order)
        prediction = model.predict(df)[0]
        return round(float(prediction), 2)
