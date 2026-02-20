
# 🏡 House Price Prediction – Feature Engineering & Feature Importance

## 📌 Project Overview

This project performs **feature engineering** and **feature importance analysis** on a house prices dataset.

The main objective is to improve data quality by creating meaningful new features such as:

* **House Age** (derived from Year Built)
* **Price per Square Foot**
* Encoding categorical features like **city**, **state**, and **property type**

After feature engineering, machine learning models are trained to analyze which features influence house prices the most.

---

## 📂 Dataset Used

Dataset file: `house_data.csv`

### Important Columns

| Column         | Description                               |
| -------------- | ----------------------------------------- |
| `target`       | House price (example: `$418,000`)         |
| `sqft`         | Total square feet (example: `1,947 sqft`) |
| `beds`         | Bedrooms (example: `3 Beds`)              |
| `baths`        | Bathrooms (example: `3 Baths`)            |
| `homeFacts`    | Contains Year Built and other house facts |
| `city`         | City of the house                         |
| `state`        | State of the house                        |
| `propertyType` | Type of property                          |
| `status`       | Listing status                            |

---

## 🎯 Project Objectives

* Load and clean the dataset
* Convert price and sqft columns into numeric values
* Extract `YearBuilt` from `homeFacts`
* Create new engineered features
* Encode categorical features using OneHotEncoding
* Train models and evaluate performance
* Analyze feature importance using a tree-based model

---

## 🧠 Feature Engineering

### 1) House Age

`YearBuilt` is extracted from the `homeFacts` column.

HouseAge is calculated as:

HouseAge = CurrentYear - YearBuilt

---

### 2) Price per Square Foot

PricePerSqFt is calculated as:

PricePerSqFt = Price / SqFt

---

## 🏷️ Categorical Encoding

Categorical columns are converted into numerical form using:

* OneHotEncoder from Scikit-learn

Examples:

* city
* state
* propertyType
* status
* fireplace

---

## 🤖 Machine Learning Models Used

### 1) Ridge Regression

Used as a baseline regression model.

### 2) Random Forest Regressor

Used for:

* Better performance
* Feature importance extraction

---

## 📊 Model Evaluation Metrics

Both models are evaluated using:

* Mean Absolute Error (MAE)
* R² Score

---

## 📌 Feature Importance Output

Feature importance is extracted from Random Forest and saved as:

`feature_importance.csv`

This file contains:

* Feature name
* Importance score

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn

---

## 📁 Project Files

| File                     | Description                                     |
| ------------------------ | ----------------------------------------------- |
| `assignment-1.ipynb`     | Jupyter notebook containing full implementation |
| `house_data.csv`         | Dataset used                                    |
| `feature_importance.csv` | Generated output file                           |
| `README.md`              | Project documentation                           |

---

## 🚀 How to Run the Project

### Step 1: Install Required Libraries

```bash
pip install pandas numpy scikit-learn
```

### Step 2: Run the Notebook

```bash
jupyter notebook
```

Open:
`assignment-1.ipynb`

Run all cells to generate results.

---

## ✅ Expected Results

The most important features usually include:

* SqFt
* HouseAge
* Beds
* Baths
* Location-related columns (city/state)
* Property type

---

## 📌 Author

**Shaik Ansar**
AI/ML Intern @ Cepia Labs
---