import os
from pathlib import Path
import joblib

def ensure_dir(path: Path) -> None:
    os.makedirs(path, exist_ok=True)

def save_model(model, path: Path) -> None:
    ensure_dir(path.parent)
    joblib.dump(model, path)

def load_model(path: Path):
    return joblib.load(path)
    