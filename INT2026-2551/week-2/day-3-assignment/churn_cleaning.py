import pandas as pd
import numpy as np

# creating a dataset
data = {
    "customer_id": [1, 2, 3, 3, 4, 5, 6, 7, 8, 9],
    "age": [25, np.nan, 45, 45, 130, 38, np.nan, 29, 27, 300],
    "gender": ["Male", "F", "female", "Female", "M", "male", "FEMALE", "Male", "m", "f"],
    "salary": [50000, 60000, 55000, 55000, 1000000, 62000, 58000, 61000, 59000, 9999999],
    "churn": [0, 1, 0, 0, 1, 0, 1, 0, 0, 1]
}

df = pd.DataFrame(data)

print("Original dataset shape:", df.shape)

df = df.drop_duplicates()

# Removing duplicate rows

print("After removing duplicates:", df.shape)

#Handling missing rows and fixing inconsistent gender formats

df["age"] = df["age"].fillna(df["age"].median())

df["gender"] = df["gender"].str.lower()

df["gender"] = df["gender"].replace({
    "m": "male",
    "f": "female"
})


Q1 = df["salary"].quantile(0.25)
Q3 = df["salary"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df = df[(df["salary"] >= lower) & (df["salary"] <= upper)]

print("After removing outliers:", df.shape)


print("\nCleaned dataset:")
print(df)

# Save cleaned dataset
df.to_csv("cleaned_customer_churn.csv", index=False)
print("\n✅ Cleaned dataset saved as cleaned_customer_churn.csv")
