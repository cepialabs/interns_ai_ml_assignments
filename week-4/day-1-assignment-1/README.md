---
# 🏡 House Prices Feature Engineering & Feature Importance

## 📌 Project Overview

This project focuses on **feature engineering** and **feature importance analysis** for a house price dataset.

The goal is to:

* Extract meaningful features from raw data (example: **House Age** from Year Built)
* Create new pricing-based features (example: **Price per Square Foot**)
* Encode categorical variables (example: city, state, property type)
* Train machine learning models and analyze which features influence house prices the most

---

## 📂 Dataset Information

The dataset used in this project is:

✅ **`data.csv`**

### Key Columns Used

| Column         | Description                                  |
| -------------- | -------------------------------------------- |
| `target`       | House price (as string, ex: `$418,000`)      |
| `sqft`         | House size in square feet (ex: `1,947 sqft`) |
| `beds`         | Bedrooms (ex: `3 Beds`)                      |
| `baths`        | Bathrooms (ex: `3 Baths`)                    |
| `homeFacts`    | Contains Year Built information              |
| `city`         | City name                                    |
| `state`        | State name                                   |
| `propertyType` | Type of property                             |

---

## 🎯 Assignment Tasks Completed

### ✅ 1. Extract House Age

Year Built is stored inside the `homeFacts` column as a nested dictionary-like structure.

We extract `YearBuilt` and compute:

HouseAge = CurrentYear - YearBuilt

---

### ✅ 2. Create Price per Square Foot

PricePerSqFt = \frac{Price}{SqFt}

This feature helps normalize prices across houses of different sizes.

---

### ✅ 3. Encode Categorical Features

Categorical features such as:

* `city`
* `state`
* `propertyType`
* `status`
* `fireplace`

are encoded using:

✅ **OneHotEncoder** (from Scikit-learn)

---

### ✅ 4. Feature Importance Analysis

We trained models to identify which features impact house prices the most.

Models used:

* **Ridge Regression** (baseline)
* **Random Forest Regressor** (for feature importance)

Random Forest provides:

✅ `feature_importances_`

---

## 🧠 Machine Learning Workflow

### Steps Followed:

1. Load dataset (`data.csv`)
2. Clean price and sqft columns
3. Extract YearBuilt from `homeFacts`
4. Feature engineering:

   * HouseAge
   * PricePerSqFt
5. Handle missing values
6. Encode categorical columns
7. Train Ridge Regression
8. Train Random Forest
9. Extract and save feature importance

---

## ⚙️ Technologies Used

* Python 3.x
* Pandas
* NumPy
* Scikit-learn

---

## 📌 Installation

Install required libraries:

```bash
pip install pandas numpy scikit-learn
```

---

## ▶️ How to Run the Project

### Option 1: Run Python Script

Make sure `data.csv` is in the same folder.

```bash
python main.py
```

### Option 2: Run in Jupyter Notebook

Open notebook:

```bash
jupyter notebook
```

Then run the cells.

---

## 📊 Output Generated

### ✅ Model Evaluation Metrics

* MAE (Mean Absolute Error)
* R² Score

### ✅ Feature Importance File

A file is generated:

📄 **`feature_importance.csv`**

It contains:

* Feature name
* Importance score

Example:

| Feature  | Importance |
| -------- | ---------- |
| SqFt     | 0.31       |
| HouseAge | 0.19       |
| Beds     | 0.12       |

---

## 🔥 Key Results (Expected)

From feature importance, the most important features generally include:

* `SqFt`
* `HouseAge`
* `Beds`
* `Baths`
* `state`
* `city`
* `propertyType`

---

## 📁 Project Structure

```
House-Price-Feature-Engineering/
│
├── data.csv
├── assignment-1.ipynb
├── feature_importance.csv
├── README.md
└── main.py (optional)
```

---

## ✅ Conclusion

This project successfully demonstrates:

* Feature extraction from raw data (`homeFacts`)
* Creation of new meaningful numerical features
* Encoding of categorical variables
* Model training for prediction
* Feature importance analysis using tree models

---

## 👤 Author

**Krushna Chandra Bindhani**

---
