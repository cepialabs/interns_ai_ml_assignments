import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import f1_score
from pathlib import Path
import joblib

DATA = Path("data/raw/spam.csv")
MODEL_OUT = Path("models/baseline.pkl")

def main():
    df = pd.read_csv(DATA)

    # auto-handle common Kaggle SMS dataset columns
    if "v1" in df.columns and "v2" in df.columns:
        df = df.rename(columns={"v2": "text", "v1": "label"})
        df["label"] = df["label"].map({"ham": 0, "spam": 1})

    if "text" not in df.columns or "label" not in df.columns:
        raise ValueError(f"Your CSV must have columns text,label. Found: {list(df.columns)}")

    df["text"] = df["text"].fillna("").astype(str)
    df["label"] = df["label"].astype(int)

    X_train, X_valid, y_train, y_valid = train_test_split(
        df["text"], df["label"], test_size=0.2, random_state=42, stratify=df["label"]
    )

    model = Pipeline([
        ("tfidf", TfidfVectorizer(stop_words="english", ngram_range=(1,2), max_features=20000)),
        ("clf", LogisticRegression(max_iter=3000))
    ])

    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    f1 = f1_score(y_valid, preds)

    MODEL_OUT.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_OUT)

    print(f"✅ Saved model: {MODEL_OUT} ({MODEL_OUT.stat().st_size} bytes)")
    print(f"F1 score: {f1:.4f}")

if __name__ == "__main__":
    main()