import numpy as np
import pandas as pd
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


# -----------------------------
# Regression Evaluation
# -----------------------------
def evaluate_regression(y_true, y_pred):
    """
    Returns regression metrics as a dictionary.
    """
    r2 = r2_score(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))

    return {
        "R2": r2,
        "MAE": mae,
        "RMSE": rmse
    }


# -----------------------------
# Classification Evaluation
# -----------------------------
def evaluate_classification(y_true, y_pred):
    """
    Returns classification metrics as a dictionary.
    """
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)

    return {
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1
    }


# -----------------------------
# Cross Validation Summary
# -----------------------------
def print_cv_results(model_name, cv_results, scoring_metrics):
    """
    Prints formatted cross-validation results.
    """
    print(f"\n===== {model_name} Cross Validation Results =====")

    for metric in scoring_metrics:
        scores = cv_results[f"test_{metric}"]
        print(f"{metric.upper()} Scores: {np.round(scores, 4)}")
        print(f"Mean {metric.upper()}: {scores.mean():.4f}")
        print(f"Std Dev {metric.upper()}: {scores.std():.4f}")
        print("-" * 40)


# -----------------------------
# Save Results to File
# -----------------------------
def save_results_to_file(filepath, content):
    """
    Saves string content to a text file.
    """
    with open(filepath, "w") as f:
        f.write(content)