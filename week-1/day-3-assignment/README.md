# 📊 DAY 3 ASSIGNMENT 1 
**Topic:** Data Cleaning Techniques  
**Date:** 21-01-2026  

---

## 📁 Dataset  
**Name:** Telecom Customer Churn Dataset  
**Source:** Kaggle  

> I downloaded the already cleaned version of the Telecom Churn dataset from Kaggle and used it for this assignment to practice data cleaning and preprocessing techniques.

---

## 🧹 Data Cleaning Techniques Covered (as per assignment)

- Missing data handling  
- Duplicate removal  
- Outlier detection  
- Inconsistent formatting  
- Encoding categorical variables  
- Scaling numerical features  
- Feature engineering basics  

---

## 📌 Assignment (from provided sheet)

**Dataset:** Customer Churn *(intentionally messy)*  

### Issues mentioned:
- Missing age values  
- Duplicate rows  
- Inconsistent gender formats  
- Salary outliers  

### Task:
> **“Clean this dataset so it is ready for machine learning.”**

---

## 🔧 Tasks I Performed in Notebook

Even though the Kaggle dataset was mostly clean, I re-applied the required steps:

1. Checked for missing values  
2. Removed duplicate records  
3. Standardized text columns (gender, category fields)  
4. Detected and removed salary outliers using IQR  
5. Encoded categorical columns using one-hot encoding  
6. Scaled numerical features using StandardScaler  
7. Saved the cleaned dataset for ML use  

---

## 📂 Files in this Folder

- `telecom_churn.csv` → Original dataset from Kaggle  
- `data_cleaning_day3.ipynb` → Python notebook  
- `cleaned_telecom_churn.csv` → Final cleaned dataset  
- `README.md` → Project documentation  

---

## 🎯 Outcome

The dataset is now:
- Free from duplicates  
- Free from missing values  
- Free from extreme outliers  
- Properly encoded and scaled  

This cleaned dataset is **ready for machine learning models**.
