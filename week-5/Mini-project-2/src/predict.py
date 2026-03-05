"""Prediction API for new customer churn scoring."""

import joblib
import pandas as pd

from .config import BEST_MODEL_PATH
from .risk import probability_to_risk_score, risk_category_from_score


GENDER_MAP = {"Female": 0, "Male": 1, "female": 0, "male": 1}


def _prepare_input(customer_data):
    if isinstance(customer_data, dict):
        input_df = pd.DataFrame([customer_data])
    elif isinstance(customer_data, pd.DataFrame):
        input_df = customer_data.copy()
    else:
        raise ValueError("customer_data must be a dict or pandas DataFrame")

    if "Gender" in input_df.columns:
        input_df["Gender"] = input_df["Gender"].apply(
            lambda x: GENDER_MAP.get(x, x)
        )

    return input_df


def predict_customer_churn(customer_data, model_path=BEST_MODEL_PATH):
    """Return churn probability, risk score, and risk category for input data."""
    artifact = joblib.load(model_path)
    model = artifact["model"]

    input_df = _prepare_input(customer_data)

    probability = float(model.predict_proba(input_df)[:, 1][0])
    risk_score = probability_to_risk_score(probability)

    return {
        "churn_probability": probability,
        "risk_score": risk_score,
        "risk_category": risk_category_from_score(risk_score),
    }
