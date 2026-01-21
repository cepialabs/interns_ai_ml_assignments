📘 DAY 3 ASSIGNMENT 1
Topic: Data Cleaning Techniques

Date: 21-01-2026

📁 Dataset Information

Dataset Name: Telecom Customer Churn Dataset

Source: Kaggle

I downloaded the Telecom Customer Churn dataset from Kaggle, which is largely pre-cleaned, and reused it to practice and demonstrate data cleaning and preprocessing techniques as required by the assignment.

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

As per the assignment requirements, the following techniques were implemented:

Missing data handling

Duplicate record removal

Outlier detection and treatment

Inconsistent text formatting correction

Encoding categorical variables

Scaling numerical features

Basic feature engineering

🔧 Tasks Performed in the Notebook

Although the Kaggle dataset was already relatively clean, I intentionally reapplied all required cleaning steps to match the assignment scenario:

Checked for missing values and handled them using median imputation

Removed duplicate records using the unique customer identifier

Standardized categorical text columns, including gender formatting

Detected and removed salary-like outliers (MonthlyCharges) using the IQR method

Converted categorical variables into numerical form using one-hot encoding

Scaled numerical features using StandardScaler for machine learning readiness

Saved the cleaned dataset for further ML model training
