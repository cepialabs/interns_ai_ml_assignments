import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("customer_churn.csv")

print("Original dataset shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()
print("After removing duplicates:", df.shape)

#  Handle missing values, Fill missing numeric with median
num_cols = df.select_dtypes(include=np.number).columns
for col in num_cols:
    df[col].fillna(df[col].median(), inplace=True)

# Fill categorical missing with mode
cat_cols = df.select_dtypes(include='object').columns
for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

#  Standardize inconsistent gender formats (if column exists)
if "Gender" in df.columns:
    df["Gender"] = df["Gender"].str.strip().str.lower()
    df["Gender"] = df["Gender"].replace({'male': 'Male', 'female': 'Female'})

print("After cleaning gender unique values:", df["Gender"].unique() if "Gender" in df.columns else "No Gender column")

# Remove salary outliers if column exists
if "MonthlyIncome" in df.columns:
    Q1 = df["MonthlyIncome"].quantile(0.25)
    Q3 = df["MonthlyIncome"].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df = df[(df["MonthlyIncome"] >= lower) & (df["MonthlyIncome"] <= upper)]
    print("After removing income outliers:", df.shape)

# Save cleaned data
df.to_csv("cleaned_customer_churn.csv", index=False)
print("\nCleaned dataset saved as cleaned_customer_churn.csv")
