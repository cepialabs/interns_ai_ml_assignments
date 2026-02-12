
# 🚀 End-to-End Machine Learning: Spam Email Classification and Housing Price Prediction

📅 **Date:** 12 February 2026

## 📌 Project Overview

This project demonstrates the application of **machine learning models** on two different problem types:

1. **Spam Email Classification** (Classification problem)
2. **House Price Prediction** (Regression problem)

The objective is to train **Random Forest models**, compare their performance with baseline models, visualize **feature importance**, and optionally evaluate **XGBoost** models.

---

## 📂 Datasets Used

### 📨 1. SpamAssassin Email Dataset

* **Problem Type:** Classification
* **Target Variable:** `label`

  * `1` → Spam
  * `0` → Not Spam (Ham)
* **Features:** Email text content
* **Evaluation Metric:** **F1-score**

**Dataset Source:**
[https://www.kaggle.com/datasets/ganiyuolalekan/spam-assassin-email-classification-dataset](https://www.kaggle.com/datasets/ganiyuolalekan/spam-assassin-email-classification-dataset)

---

### 🏠 2. Ames Housing Dataset

* **Problem Type:** Regression
* **Target Variable:** `SalePrice`
* **Features:** Numerical and categorical house attributes
* **Evaluation Metric:** **R² Score**

**Dataset Source:**
[https://www.kaggle.com/datasets/prevek18/ames-housing-dataset](https://www.kaggle.com/datasets/prevek18/ames-housing-dataset)

---

## 🧠 Models Implemented

### 🔹 Baseline Models

* **Spam Dataset:** Logistic Regression
* **Housing Dataset:** Linear Regression

### 🌲 Random Forest Models (Primary Models)

* RandomForestClassifier (Spam)
* RandomForestRegressor (Housing)

### 🚀 Optional Advanced Model

* XGBoost Classifier
* XGBoost Regressor

---

## ⚙️ Machine Learning Pipeline

### Spam Email Classification

1. Text preprocessing using **TF-IDF Vectorization**
2. Train-test split
3. Model training (Logistic Regression → Random Forest → XGBoost)
4. Evaluation using **F1-score** and confusion matrix
5. Visualization of top important words

### House Price Prediction

1. Missing value handling using **SimpleImputer**
2. Categorical encoding using **OneHotEncoder**
3. Pipeline creation using **ColumnTransformer**
4. Model training (Linear Regression → Random Forest → XGBoost)
5. Evaluation using **R² score** and RMSE
6. Visualization of feature importance

---

## 📊 Results Summary

| Dataset | Model               | Metric   | Performance |
| ------- | ------------------- | -------- | ----------- |
| Spam    | Logistic Regression | F1-score | Baseline    |
| Spam    | Random Forest       | F1-score | Improved    |
| Spam    | XGBoost             | F1-score | Best        |
| Housing | Linear Regression   | R²       | Baseline    |
| Housing | Random Forest       | R²       | Improved    |
| Housing | XGBoost             | R²       | Best        |


```

## 🎯 Key Learnings

* Random Forest models outperform baseline models by capturing non-linear relationships
* Feature importance helps interpret model predictions
* XGBoost provides further performance improvements
* Proper preprocessing is crucial for real-world datasets

---


