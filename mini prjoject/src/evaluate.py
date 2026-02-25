import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, roc_curve, roc_auc_score

from .config import Config
from .data_prep import load_data, split_data
from .utils import ensure_dir, load_model

def evaluate(model_name="baseline"):
    cfg = Config()
    ensure_dir(cfg.OUTPUT_DIR)

    df = load_data(cfg.DATA_PATH, cfg.TEXT_COL, cfg.TARGET_COL)
    X_train, X_valid, y_train, y_valid = split_data(
        df, cfg.TEXT_COL, cfg.TARGET_COL, cfg.TEST_SIZE, cfg.RANDOM_STATE
    )

    X_valid = X_valid.to_frame(name="text")

    model_path = cfg.MODEL_DIR / f"{model_name}.pkl"
    model = load_model(model_path)

    preds = model.predict(X_valid)

    # Confusion matrix
    cm = confusion_matrix(y_valid, preds)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    plt.title(f"Confusion Matrix - {model_name}")
    plt.savefig(cfg.OUTPUT_DIR / "confusion_matrix.png", bbox_inches="tight")
    plt.close()

    # ROC Curve (if proba exists)
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(X_valid)[:, 1]
        fpr, tpr, _ = roc_curve(y_valid, proba)
        auc = roc_auc_score(y_valid, proba)

        plt.plot(fpr, tpr)
        plt.plot([0, 1], [0, 1])
        plt.title(f"ROC Curve - {model_name} (AUC={auc:.4f})")
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.savefig(cfg.OUTPUT_DIR / "roc_curve.png", bbox_inches="tight")
        plt.close()
    else:
        auc = np.nan

    return cm, auc

if __name__ == "__main__":
    cm, auc = evaluate("baseline")
    print("Saved charts. AUC:", auc)