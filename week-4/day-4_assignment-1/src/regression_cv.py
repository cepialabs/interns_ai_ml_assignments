import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score, KFold
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Load dataset
df = pd.read_csv("data/house_prices.csv")

# Example feature selection
X = df.drop("price", axis=1)
y = df["price"]

# 5-Fold CV
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Random Forest
rf_model = RandomForestRegressor(random_state=42)
rf_scores = cross_val_score(rf_model, X, y, cv=kf, scoring="r2")

# Linear Regression with Scaling
lr_pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
])

lr_scores = cross_val_score(lr_pipeline, X, y, cv=kf, scoring="r2")

print("Random Forest R2:", rf_scores.mean())
print("Linear Regression R2:", lr_scores.mean())