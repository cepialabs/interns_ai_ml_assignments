# Customer Churn Data Cleaning & Preparation 📊

## 📌 Project Overview

This repository contains a **data cleaning and preprocessing project** using a **Customer Churn dataset** that was intentionally made messy.
The goal of this assignment is to **clean the dataset and prepare it for machine learning** by handling missing values, duplicates, inconsistent categorical formats, and numerical outliers.

The entire workflow is implemented using **Python**, **Pandas**, and **Matplotlib** in a Jupyter Notebook.

---

## 📁 Dataset

The dataset used for this assignment is a **Customer Churn dataset** containing customer-related attributes such as usage behavior, subscription details, and churn status.

### Key Columns:

* **CustomerID**
* **Age**
* **Gender**
* **Tenure**
* **Usage Frequency**
* **Support Calls**
* **Payment Delay**
* **Subscription Type**
* **Contract Length**
* **Total Spend**
* **Last Interaction**
* **Churn** (Target Variable)

⚠️ The dataset contains intentional data quality issues for learning purposes.

---

## 🎯 Objectives

This project addresses the following data quality problems:

1. **Missing Age Values**
   Handle missing values in the `Age` column.

2. **Duplicate Rows**
   Identify and remove duplicate customer records.

3. **Inconsistent Gender Formats**
   Standardize inconsistent gender values such as `M`, `Male`, `female`, `F`.

4. **Salary / Spending Outliers**
   Detect and treat outliers using the `Total Spend` column as a numerical feature.

5. **Machine Learning Readiness**
   Encode categorical variables and prepare a clean, numeric dataset suitable for ML models.

---

## 📂 Folder Structure

```
INT2026-3908/
└── week-1/
    ├── day-2-assignment-1/
        ├── customer_churn_cleaning.ipynb
        ├── customer_churn_dataset.csv
        ├── clean_customer_churn.csv
        └── README.md
```

---

## 🛠 Tools & Libraries

The following tools and libraries were used:

* Python 3.x
* Pandas
* NumPy
* Matplotlib
* Jupyter Notebook

---

## 🔍 Data Cleaning Steps Performed

* **Duplicate Removal:**
  Removed duplicate rows to avoid biased learning.

* **Missing Value Handling:**
  Filled missing `Age` values using the median for robustness.

* **Gender Standardization:**
  Converted inconsistent gender formats into standardized values.

* **Outlier Detection & Removal:**
  Used boxplot visualization and the IQR method on `Total Spend` to detect and remove outliers.

* **Categorical Encoding:**
  Converted categorical features into numeric form using one-hot encoding.

---

## 📊 Visualizations

* Boxplot used to visualize outliers in `Total Spend`
* Summary statistics to validate cleaned data

> 📈 These visualizations help ensure data quality before machine learning.

---

## 📌 How to Run the Notebook

1. Clone the repository:

```bash
git clone https://github.com/cepialabs/interns_ai_ml_assignments.git
```

2. Navigate to the assignment folder:

```bash
cd interns_ai_ml_assignments/week-1/day-2-assignment-1
```

3. Open Jupyter Notebook:

```bash
jupyter notebook customer_churn_cleaning.ipynb
```

4. Run all cells to generate the cleaned dataset.

---

## 🧠 What You Will Learn

* How to clean real-world messy datasets
* Handling missing values and duplicates
* Standardizing categorical variables
* Detecting and treating outliers
* Preparing data for machine learning pipelines

---

## ✨ Future Enhancements

Possible extensions of this project include:

* Exploratory Data Analysis (EDA)
* Churn prediction using ML models
* Feature scaling and normalization
* Model evaluation and performance metrics
* Interactive dashboards (Streamlit / Power BI)

---

## 📌 Author

**Swati M Patil**
AI/ML Intern @ Cepia Labs

