import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(csv_path, text_col="text", target_col="label"):
    df = pd.read_csv(csv_path)

    # Basic checks
    if text_col not in df.columns or target_col not in df.columns:
        raise ValueError(f"CSV must contain '{text_col}' and '{target_col}' columns.")

    # Clean
    df[text_col] = df[text_col].fillna("").astype(str)
    df[target_col] = df[target_col].astype(int)

    return df

def split_data(df, text_col="text", target_col="label", test_size=0.2, random_state=42):
    X = df[text_col]
    y = df[target_col]

    return train_test_split(
        X, y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )