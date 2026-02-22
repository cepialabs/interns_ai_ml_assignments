import pandas as pd
from sklearn.model_selection import cross_validate, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Load dataset
df = pd.read_csv("data/spam_emails.csv")

X = df.drop("label", axis=1)
y = df["label"]

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

rf = RandomForestClassifier(random_state=42)

lr_pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=1000))
])

scoring = ["accuracy", "precision", "recall", "f1"]

rf_scores = cross_validate(rf, X, y, cv=skf, scoring=scoring)
lr_scores = cross_validate(lr_pipeline, X, y, cv=skf, scoring=scoring)

print("Random Forest Accuracy:", rf_scores["test_accuracy"].mean())
print("Logistic Regression Accuracy:", lr_scores["test_accuracy"].mean())

print("Random Forest F1:", rf_scores["test_f1"].mean())
print("Logistic Regression F1:", lr_scores["test_f1"].mean())