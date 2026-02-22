import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("house_prices.csv")

print("Original Dataset:")
print(df.head())

 
# House age from year built
current_year = 2025
df["house_age"] = current_year - df["year_built"]

# Price per square foot
df["price_per_sqft"] = df["price"] / df["square_feet"]

# ----------------------------------------

le_neighborhood = LabelEncoder()
le_condition = LabelEncoder()

df["neighborhood_encoded"] = le_neighborhood.fit_transform(df["neighborhood"])
df["condition_encoded"] = le_condition.fit_transform(df["condition"])

print("\nAfter Feature Engineering:")
print(df.head())



features = [
    "square_feet",
    "bedrooms",
    "bathrooms",
    "house_age",
    "neighborhood_encoded",
    "condition_encoded"
]

X = df[features]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


lr = LinearRegression()
lr.fit(X_train, y_train)

print("\nLinear Regression Feature Importance:")
for feature, coef in zip(features, lr.coef_):
    print(f"{feature}: {coef:.2f}")


tree = DecisionTreeRegressor(random_state=42)
tree.fit(X_train, y_train)

print("\nDecision Tree Feature Importance:")
for feature, importance in zip(features, tree.feature_importances_):
    print(f"{feature}: {importance:.4f}")
