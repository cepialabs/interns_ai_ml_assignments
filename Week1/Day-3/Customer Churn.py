import pandas as pd
import numpy as np
import os

# -----------------------------
# Get script directory
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# CSV path (same folder as this .py file)
csv_path = os.path.join(BASE_DIR, "Customer Churn.csv")

# Load dataset
df = pd.read_csv(csv_path)

print("Initial Shape:", df.shape)

# -----------------------------
# Remove duplicates
# -----------------------------
df.drop_duplicates(inplace=True)

# -----------------------------
# Handle missing Age
# -----------------------------
df['Age'].fillna(df['Age'].median(), inplace=True)

# -----------------------------
# Clean Gender column
# -----------------------------
df['Gender'] = (
    df['Gender']
    .astype(str)
    .str.strip()
    .str.lower()
    .replace({'m': 'male', 'f': 'female'})
    .str.capitalize()
)

# -----------------------------
# Handle Salary outliers (IQR)
# -----------------------------
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df = df[(df['Salary'] >= lower) & (df['Salary'] <= upper)]

# -----------------------------
# Encode categorical columns
# -----------------------------
df = pd.get_dummies(df, drop_first=True)

# -----------------------------
# Save cleaned dataset
# -----------------------------
output_path = os.path.join(BASE_DIR, "customer_churn_cleaned.csv")
df.to_csv(output_path, index=False)

print("✅ DATA CLEANING COMPLETED SUCCESSFULLY")
print("📁 Saved as customer_churn_cleaned.csv")
