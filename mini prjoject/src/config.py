from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Config:
    PROJECT_ROOT: Path = Path(__file__).resolve().parents[1]
    DATA_PATH: Path = PROJECT_ROOT / "data" / "raw" / "spam.csv"
    OUTPUT_DIR: Path = PROJECT_ROOT / "outputs"
    MODEL_DIR: Path = PROJECT_ROOT / "models"

    TARGET_COL: str = "label"
    TEXT_COL: str = "text"

    RANDOM_STATE: int = 42
    TEST_SIZE: float = 0.2