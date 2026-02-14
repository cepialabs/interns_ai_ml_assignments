# 🏠 House Price Prediction

This Assignment focuses on predicting house prices using machine learning
techniques. It includes feature engineering, categorical encoding, and
feature importance analysis using both linear and tree-based models.

------------------------------------------------------------------------

## 📌 Project Overview

The goal is to build a regression model that predicts house sale prices
based on property characteristics such as size, age, quality, location,
and condition.

Key steps include: - Data preprocessing and feature engineering -
Encoding categorical variables - Training regression models - Analyzing
feature importance

------------------------------------------------------------------------

## ⚙️ Feature Engineering

-   **HouseAge**

        HouseAge = CurrentYear - YearBuilt

-   **PricePerSqFt**

        PricePerSqFt = SalePrice / GrLivArea

------------------------------------------------------------------------

## 🔄 Data Preprocessing

-   Numerical features passed through directly
-   Categorical features encoded using One-Hot Encoding
-   Missing values handled via imputation

------------------------------------------------------------------------

## 🤖 Models Used

### Linear Regression

-   Interpretable coefficients
-   Baseline regression model

### Random Forest Regressor

-   Captures non-linear relationships
-   Provides feature importance scores

------------------------------------------------------------------------

## 📊 Feature Importance

-   Linear Regression: coefficients
-   Random Forest: impurity-based importance

Top features typically include: - Overall quality - Living area - Price
per square foot - Neighborhood - House age

------------------------------------------------------------------------

## 📈 Evaluation

-   Metric: R² score
-   Train-test split used

------------------------------------------------------------------------

## 🛠️ Requirements

    pip install pandas numpy scikit-learn

------------------------------------------------------------------------

## ▶️ Usage

    python train.py

------------------------------------------------------------------------

## 🚀 Future Work

-   Cross-validation
-   SHAP explainability
-   Advanced models (XGBoost, LightGBM)
-   Model deployment

