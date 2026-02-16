# 📊 Medical Insurance Cost Prediction using Machine Learning

## 📌 Project Overview
This mini project focuses on predicting **medical insurance charges** based on an individual’s demographic and health-related attributes.  
The goal is to build and compare multiple **regression models** and identify the most effective one using appropriate evaluation metrics.

---

## 🎯 Problem Statement
Insurance companies need to estimate medical insurance costs accurately to manage risk and pricing.  
This project aims to predict insurance charges using machine learning techniques based on customer attributes such as age, BMI, smoking status, and region.

---

## 📂 Dataset Information
- **Dataset Name:** Medical Insurance Cost Dataset  
- **Source:** Kaggle  
- **Link:** https://www.kaggle.com/datasets/mirichoi0218/insurance  
- **Rows:** 1,338  
- **Columns:** 7  

### Features Description
| Feature | Description |
|------|-------------|
| age | Age of the primary beneficiary |
| sex | Gender (male/female) |
| bmi | Body Mass Index |
| children | Number of dependents |
| smoker | Smoking status (yes/no) |
| region | Residential region |
| charges | Medical insurance cost (Target variable) |

---

## 🧪 Project Workflow
1. Dataset Understanding  
2. Exploratory Data Analysis (EDA)  
3. Feature Encoding  
4. Feature Scaling  
5. Model Training  
6. Model Evaluation  
7. Model Comparison  
8. Insights & Conclusions  

---

## ⚙️ Technologies & Libraries Used
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn  
- XGBoost  

---

## 🤖 Machine Learning Models
The following regression models were implemented and compared:

- **Linear Regression** (Baseline Model)  
- **Random Forest Regressor**  
- **XGBoost Regressor**

---

## 📈 Evaluation Metrics
Models were evaluated using:
- **RMSE (Root Mean Squared Error)**
- **MAE (Mean Absolute Error)**
- **R² Score**

Cross-validation (5-fold) was used for robust performance estimation.

---

## 📊 Results Summary

| Model | RMSE | R² Score |
|------|------|----------|
| Linear Regression | Baseline | Moderate |
| Random Forest | Improved | High |
| XGBoost | Best | Highest |

✅ **XGBoost Regressor achieved the best overall performance.**

---

## 🔍 Key Insights
- Smoking status is the most influential factor in predicting insurance charges.
- Ensemble models significantly outperform linear regression.
- XGBoost provides better generalization and lower prediction error.
- The model can support insurance companies in risk-based premium estimation.

---

## ✅ Conclusion
This project demonstrates a complete machine learning workflow for a real-world regression problem.  
The comparison of multiple models highlights the effectiveness of ensemble techniques in predictive analytics.

