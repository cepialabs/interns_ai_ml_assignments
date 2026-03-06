"""Training pipeline for churn prediction."""

from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from .config import (
    DATA_PATH,
    GEOGRAPHY_COLUMN,
    METRICS_PATH,
    MODELS_DIR,
    PLOTS_DIR,
    RANDOM_STATE,
    RF_MODEL_PATH,
    RISK_SCORES_PATH,
    TEST_SIZE,
    BEST_MODEL_PATH,
)
from .data_preprocessing import (
    clean_dataset,
    load_dataset,
    normalize_columns,
    split_features_target,
)
from .eda import run_eda
from .risk import probability_to_risk_score, risk_category_from_score


def build_preprocessor(X_train: pd.DataFrame) -> ColumnTransformer:
    """Build preprocessing transformer with imputation, scaling and encoding."""
    numeric_features = [col for col in X_train.columns if col != GEOGRAPHY_COLUMN]
    categorical_features = [GEOGRAPHY_COLUMN]

    numeric_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )

    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    return ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )


def evaluate_model(model, X_test, y_test) -> dict:
    """Evaluate classifier and return required metrics."""
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    return {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred, zero_division=0),
        "recall": recall_score(y_test, y_pred, zero_division=0),
        "f1_score": f1_score(y_test, y_pred, zero_division=0),
        "roc_auc": roc_auc_score(y_test, y_prob),
        "confusion_matrix": confusion_matrix(y_test, y_pred).tolist(),
        "y_prob": y_prob,
    }


def select_best_model(results: dict) -> str:
    """Select best model prioritizing Recall, then ROC-AUC."""
    sorted_models = sorted(
        results.items(),
        key=lambda item: (item[1]["recall"], item[1]["roc_auc"]),
        reverse=True,
    )
    return sorted_models[0][0]


def save_feature_importance(rf_pipeline: Pipeline):
    """Save Random Forest feature importance plot."""
    preprocessor = rf_pipeline.named_steps["preprocessor"]
    classifier = rf_pipeline.named_steps["classifier"]

    feature_names = preprocessor.get_feature_names_out()
    importances = classifier.feature_importances_

    importance_df = pd.DataFrame(
        {"feature": feature_names, "importance": importances}
    ).sort_values("importance", ascending=False)

    top_n = importance_df.head(15)

    plt.figure(figsize=(9, 6))
    plt.barh(top_n["feature"], top_n["importance"])
    plt.gca().invert_yaxis()
    plt.title("Top 15 Random Forest Feature Importances")
    plt.xlabel("Importance")
    plt.tight_layout()
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    plt.savefig(Path(PLOTS_DIR, "rf_feature_importance.png"), dpi=150)
    plt.close()


def generate_risk_scores(model, X_test: pd.DataFrame, y_test: pd.Series):
    """Generate churn probabilities and mapped risk categories for test data."""
    probabilities = model.predict_proba(X_test)[:, 1]

    output = X_test.copy()
    output["ActualExited"] = y_test.values
    output["ChurnProbability"] = probabilities
    output["RiskScore"] = output["ChurnProbability"].apply(probability_to_risk_score)
    output["RiskCategory"] = output["RiskScore"].apply(risk_category_from_score)

    output.to_csv(RISK_SCORES_PATH, index=False)


def main():
    MODELS_DIR.mkdir(parents=True, exist_ok=True)

    raw_df = load_dataset(str(DATA_PATH))
    normalized_df = normalize_columns(raw_df)

    # EDA on normalized data (with original categorical values preserved)
    run_eda(normalized_df)

    df = clean_dataset(normalized_df)
    X, y = split_features_target(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y,
    )

    preprocessor = build_preprocessor(X_train)

    models = {
        "LogisticRegression": Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                (
                    "classifier",
                    LogisticRegression(max_iter=1000, random_state=RANDOM_STATE),
                ),
            ]
        ),
        "RandomForest": Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                (
                    "classifier",
                    RandomForestClassifier(
                        n_estimators=300,
                        random_state=RANDOM_STATE,
                        class_weight="balanced",
                    ),
                ),
            ]
        ),
    }

    metrics_results = {}
    trained_models = {}

    for name, pipeline in models.items():
        pipeline.fit(X_train, y_train)
        eval_result = evaluate_model(pipeline, X_test, y_test)
        metrics_results[name] = eval_result
        trained_models[name] = pipeline

    metrics_table = []
    for model_name, metric in metrics_results.items():
        metrics_table.append(
            {
                "model": model_name,
                "accuracy": metric["accuracy"],
                "precision": metric["precision"],
                "recall": metric["recall"],
                "f1_score": metric["f1_score"],
                "roc_auc": metric["roc_auc"],
                "confusion_matrix": str(metric["confusion_matrix"]),
            }
        )

    metrics_df = pd.DataFrame(metrics_table)
    metrics_df.to_csv(METRICS_PATH, index=False)

    best_model_name = select_best_model(metrics_results)
    best_model = trained_models[best_model_name]

    artifact = {
        "model": best_model,
        "model_name": best_model_name,
        "feature_columns": list(X.columns),
    }

    joblib.dump(artifact, BEST_MODEL_PATH)
    joblib.dump(trained_models["RandomForest"], RF_MODEL_PATH)

    save_feature_importance(trained_models["RandomForest"])
    generate_risk_scores(best_model, X_test, y_test)

    print("Training complete.")
    print(f"Best model: {best_model_name}")
    print(metrics_df.to_string(index=False))


if __name__ == "__main__":
    main()
