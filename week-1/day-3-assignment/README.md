# 🧹 Customer Churn Dataset – Data Cleaning & ML Preparation

## 📅 Date

**21 January 2026**

---

## 📌 Project Overview

This project focuses on cleaning an **intentionally messy Customer Churn dataset** and preparing it for **machine learning models**.
The dataset contains common real-world data quality issues such as missing values, duplicates, inconsistent categorical formats, and outliers.

The goal is to transform raw data into a **clean, structured, and ML-ready dataset**.

---

## 📂 Dataset Information

* **Dataset Name:** Customer Churn (Messy Data)
* **File:** `customer_churn_messy.csv`
* **Type:** Tabular customer data
* **Target Variable:** `Churn`

---

## ⚠️ Identified Data Issues

The dataset initially contained the following problems:

* ❌ Missing values in the `Age` column
* ❌ Duplicate customer records
* ❌ Inconsistent formats in the `Gender` column
* ❌ Extreme values (outliers) in monetary data
* ❌ Categorical variables not suitable for ML models

---

## 🛠️ Data Cleaning Steps Performed

### 1️⃣ Removed Duplicate Records

Duplicate rows were removed to ensure that each customer is represented only once.

---

### 2️⃣ Handled Missing Age Values

Missing values in the `Age` column were filled using the **median**, which is robust to outliers.

---

### 3️⃣ Standardized & Encoded Gender

* Converted all gender values to lowercase
* Mapped:

  * `male → 0`
  * `female → 1`
* Filled missing values using the **mode**

---

### 4️⃣ Outlier Removal (Salary Equivalent)

The dataset does **not** contain a `Salary` column.
Instead, **`Total Spend`** was used as the monetary feature.

* Outliers were removed using the **Interquartile Range (IQR) method**
* This prevents extreme values from biasing machine learning models

---

### 5️⃣ Target Variable Encoding

The `Churn` column was converted into numeric format:

* `No → 0`
* `Yes → 1`

---

### 6️⃣ One-Hot Encoding for Categorical Features

Multi-category features were encoded using **One-Hot Encoding**:

* `Subscription Type`
* `Contract Length`

Binary columns such as `Gender` were **not one-hot encoded**.

---

### 7️⃣ Feature Scaling

All numeric features were scaled using **StandardScaler** to improve ML model performance.

---

### 8️⃣ Train-Test Split

The dataset was split into:

* **80% Training data**
* **20% Testing data**

Stratified sampling was used to preserve churn distribution.

---

## ✅ Final Dataset Status

After cleaning and preprocessing:

* ✔ No missing values
* ✔ No duplicate records
* ✔ All categorical data encoded
* ✔ Outliers removed
* ✔ Fully compatible with machine learning algorithms

---

## 📊 Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Jupyter Notebook**

---

## 🎯 Outcome

The cleaned dataset is now ready for:

* Logistic Regression
* Decision Tree
* Random Forest
* Any supervised ML classification model

---

## 📌 Conclusion

This project demonstrates a complete **real-world data cleaning pipeline**, handling common data issues and preparing the dataset for reliable machine learning model development.


