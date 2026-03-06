"""Data loading and preprocessing utilities."""

import pandas as pd

from .config import DROP_COLUMNS, GENDER_COLUMN, TARGET_COLUMN


GENDER_MAP = {"Female": 0, "Male": 1}
COLUMN_ALIASES = {
    "rownumber": "RowNumber",
    "row_number": "RowNumber",
    "customerid": "CustomerId",
    "customer_id": "CustomerId",
    "surname": "Surname",
    "creditscore": "CreditScore",
    "credit_score": "CreditScore",
    "geography": "Geography",
    "country": "Geography",
    "gender": "Gender",
    "age": "Age",
    "tenure": "Tenure",
    "balance": "Balance",
    "numofproducts": "NumOfProducts",
    "products_number": "NumOfProducts",
    "hascrcard": "HasCrCard",
    "credit_card": "HasCrCard",
    "isactivemember": "IsActiveMember",
    "active_member": "IsActiveMember",
    "estimatedsalary": "EstimatedSalary",
    "estimated_salary": "EstimatedSalary",
    "exited": "Exited",
    "churn": "Exited",
}


def load_dataset(file_path: str) -> pd.DataFrame:
    """Load churn dataset from CSV."""
    return pd.read_csv(file_path)


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Map common header variants to expected project column names."""
    renamed_columns = {}
    for col in df.columns:
        normalized = str(col).strip().replace(" ", "").replace("-", "_").lower()
        normalized = normalized.replace("__", "_")
        renamed_columns[col] = COLUMN_ALIASES.get(normalized, str(col).strip())
    return df.rename(columns=renamed_columns)


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Drop unnecessary columns and handle gender label encoding."""
    clean_df = normalize_columns(df).drop(columns=DROP_COLUMNS, errors="ignore").copy()

    if GENDER_COLUMN in clean_df.columns:
        clean_df[GENDER_COLUMN] = clean_df[GENDER_COLUMN].map(GENDER_MAP)

    return clean_df


def split_features_target(df: pd.DataFrame):
    """Split dataframe into features and target."""
    X = df.drop(columns=[TARGET_COLUMN])
    y = df[TARGET_COLUMN]
    return X, y
