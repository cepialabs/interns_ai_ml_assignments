import sys
import pandas as pd
from pathlib import Path
from .config import Config
from .utils import load_model

def main():
    if len(sys.argv) < 2:
        print('Usage: python -m src.predict "your email text here"')
        sys.exit(1)

    text = sys.argv[1]
    cfg = Config()

    candidates = [
        cfg.MODEL_DIR / "baseline.pkl",
        cfg.MODEL_DIR / "rf.pkl",
        cfg.MODEL_DIR / "xgb.pkl",
        cfg.MODEL_DIR / "baseline_logreg.pkl",
        cfg.MODEL_DIR / "random_forest.pkl",
        cfg.MODEL_DIR / "xgboost.pkl",
    ]

    model_path = next((p for p in candidates if p.exists() and p.stat().st_size > 0), None)
    if model_path is None:
        raise FileNotFoundError(f"No non-empty model found in {cfg.MODEL_DIR}. Run: python -m src.train")

    model = load_model(model_path)
    X = pd.DataFrame({"text": [text]})

    pred = model.predict(X)[0]
    proba = model.predict_proba(X)[0, 1] if hasattr(model, "predict_proba") else None

    label = "SPAM" if pred == 1 else "NOT SPAM"
    if proba is not None:
        print(f"Loaded: {model_path.name}")
        print(f"Prediction: {label} | spam_probability={proba:.4f}")
    else:
        print(f"Loaded: {model_path.name}")
        print(f"Prediction: {label}")

if __name__ == "__main__":
    main()