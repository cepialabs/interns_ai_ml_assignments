"""Common constants for the churn project."""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "Churn_Modelling.csv"
MODELS_DIR = BASE_DIR / "models"
PLOTS_DIR = MODELS_DIR / "plots"
BEST_MODEL_PATH = MODELS_DIR / "best_model.joblib"
RF_MODEL_PATH = MODELS_DIR / "random_forest_model.joblib"
METRICS_PATH = MODELS_DIR / "model_metrics.csv"
RISK_SCORES_PATH = MODELS_DIR / "test_risk_scores.csv"

DROP_COLUMNS = ["RowNumber", "CustomerId", "Surname"]
TARGET_COLUMN = "Exited"
GEOGRAPHY_COLUMN = "Geography"
GENDER_COLUMN = "Gender"

RANDOM_STATE = 42
TEST_SIZE = 0.2
