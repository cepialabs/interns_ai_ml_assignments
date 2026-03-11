"""EDA plotting functions."""

from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

from .config import PLOTS_DIR, TARGET_COLUMN


def run_eda(df):
    """Generate required EDA plots and save to disk."""
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid")

    # Churn distribution
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x=TARGET_COLUMN)
    plt.title("Churn Distribution")
    plt.xlabel("Exited (0=No, 1=Yes)")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(Path(PLOTS_DIR, "churn_distribution.png"), dpi=150)
    plt.close()

    # Age vs Churn
    plt.figure(figsize=(7, 4))
    sns.boxplot(data=df, x=TARGET_COLUMN, y="Age")
    plt.title("Age vs Churn")
    plt.xlabel("Exited (0=No, 1=Yes)")
    plt.ylabel("Age")
    plt.tight_layout()
    plt.savefig(Path(PLOTS_DIR, "age_vs_churn.png"), dpi=150)
    plt.close()

    # Geography vs Churn
    plt.figure(figsize=(8, 4))
    sns.countplot(data=df, x="Geography", hue=TARGET_COLUMN)
    plt.title("Geography vs Churn")
    plt.xlabel("Geography")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(Path(PLOTS_DIR, "geography_vs_churn.png"), dpi=150)
    plt.close()

    # Correlation heatmap
    corr_df = df.copy()
    corr_df["Gender"] = corr_df["Gender"].map({"Female": 0, "Male": 1})
    corr_numeric = corr_df.select_dtypes(include=["number"])

    plt.figure(figsize=(10, 7))
    sns.heatmap(corr_numeric.corr(), cmap="coolwarm", annot=False)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(Path(PLOTS_DIR, "correlation_heatmap.png"), dpi=150)
    plt.close()
