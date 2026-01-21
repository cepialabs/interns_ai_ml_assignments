📘 DAY 3 ASSIGNMENT 1
Topic: Data Cleaning Techniques

📅 Date: 21-01-2026

📁 Dataset Information

Dataset Name: Synthetic Telecom Customer Churn Dataset (Messy)
Source: Self-generated (Inspired by Kaggle Telco Churn Dataset)

For this assignment, instead of using a fully cleaned Kaggle dataset, I worked with a synthetic telecom customer churn dataset that was intentionally made messy to closely match the problem statement provided in the assignment sheet.

The dataset was designed to include real-world data quality issues such as missing values, inconsistent formatting, duplicate records, and numerical outliers.

📌 Assignment Description (From Provided Sheet)

Dataset:
Customer Churn (Intentionally Messy)

Issues Mentioned:

Missing age values

Duplicate rows

Inconsistent gender formats

Salary outliers

Task:

“Clean this dataset so it is ready for machine learning.”

🧹 Data Cleaning Techniques Covered

As required by the assignment, the following data cleaning and preprocessing techniques were applied:

Missing data handling

Duplicate record removal

Outlier detection and treatment

Inconsistent text formatting correction

Encoding categorical variables

Scaling numerical features

Basic feature engineering

🔧 Tasks Performed in the Notebook

The following steps were performed in a step-by-step and structured manner:

Loaded the messy synthetic telecom churn dataset

Checked missing values in numerical and categorical columns

Handled missing numerical values using median imputation

Handled missing categorical values using mode imputation

Removed duplicate records using customerID as a unique identifier

Standardized inconsistent text values (e.g., gender: M, male, Female, f)

Detected and removed salary-like outliers (MonthlyCharges) using the IQR method

Converted categorical variables into numerical form using one-hot encoding

Scaled numerical features using StandardScaler for ML readiness

Saved the final cleaned dataset for machine learning model training

📂 Folder Structure
week-1/
└── day-3-assignment/
    ├── day3assignment.ipynb
    ├── customer_churn.csv
    ├── cleaned_customer_churn.csv


File Description:

customer_churn.csv → Original messy synthetic dataset

day3assignment.ipynb → Data cleaning and preprocessing notebook

cleaned_customer_churn.csv → Final cleaned dataset ready for ML


🎯 Outcome

After applying all required data cleaning techniques:

✔ Missing values were handled

✔ Duplicate records were removed

✔ Inconsistent text formatting was standardized

✔ Outliers were detected and treated

✔ Categorical variables were encoded

✔ Numerical features were scaled

✅ The dataset is now clean, structured, and fully ready for machine learning models.
