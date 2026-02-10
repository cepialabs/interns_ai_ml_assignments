# 🏠 House Price Feature Engineering & Feature Importance Analysis
📅 Date: 10 Feb 2026

## 📌 Project Overview
This project analyzes house prices using the **King County House Sales dataset**.  
The goal is to perform **feature engineering**, encode categorical variables, and analyze **feature importance** using regression and tree-based models.

---

## 📂 Dataset
**Name:** King County House Sales  
**Source:** Kaggle  
**Link:** https://www.kaggle.com/datasets/harlfoxem/housesalesprediction  

The dataset contains house sale prices along with structural, temporal, and location-related features.

---

## ⚙️ Feature Engineering

The following new features were created to improve interpretability and model performance:

### 1️⃣ House Age
```text
house_age = current_year − year_built
Older houses generally have lower market value due to depreciation.

### 2️⃣ Price per Square Foot
Computed to normalize house prices:
This allows fair comparison across houses of different sizes.

---

##  Categorical Feature Encoding
Categorical variables were converted into numerical form using **One-Hot Encoding**:
- `zipcode`
- `condition`

This step is required for machine learning models to process categorical data.

---

## 🤖 Models Used

### 🔹 Linear Regression
- Simple and interpretable model
- Useful for understanding linear relationships between features and house prices

### 🔹 Decision Tree Regressor
- Captures non-linear relationships
- Automatically handles feature interactions

---

## 📊 Feature Importance Analysis

### Linear Regression Feature Importance
- Importance is measured using coefficient values
- Features with larger absolute coefficients have stronger influence on price

**Key observations:**
- Living area (`sqft_living`) has the strongest impact on price
- House age negatively affects house value
- Location (`zipcode`) plays a significant role

---

### Decision Tree Feature Importance
- Importance is based on how frequently a feature is used in decision splits

**Key observations:**
- Living area remains the most influential feature
- Location-based features strongly affect pricing
- Non-linear effects of house age and condition are better captured

---

## 🧠 Key Insights
- House size and location are the most important price determinants
- Older houses tend to be priced lower
- Feature engineering improves model interpretability
- Tree-based models reveal complex pricing patterns

---

---

## ✅ Conclusion
This project demonstrates how feature engineering and feature importance analysis help identify key drivers of house prices.  
Both linear regression and decision tree models confirm that **house size, location, and age** are the primary factors influencing property value.

---


