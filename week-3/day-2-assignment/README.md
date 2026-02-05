# 📊 Machine Learning Assignment – Regression & Classification

**Date:** 05-02-2026

---

## 📌 Overview

This repository contains **two end-to-end Machine Learning notebooks** demonstrating:

1. **Regression** – Predicting housing prices using real estate features
2. **Classification** – Detecting spam emails using Logistic Regression

Both projects use **real Kaggle datasets** and follow a complete ML workflow suitable for academic assignments.

---

## 🏠 Project 1: Housing Price Prediction (Regression)

### 📂 Dataset

**Housing Prices in Metropolitan Areas of India**
Source: [https://www.kaggle.com/datasets/ruchi798/housing-prices-in-metropolitan-areas-of-india](https://www.kaggle.com/datasets/ruchi798/housing-prices-in-metropolitan-areas-of-india)

### 🎯 Objective

To predict house prices based on features such as:

* Area / Square Footage
* Number of rooms
* Location (city)
* Other housing attributes

### 🧠 Machine Learning Type

* Supervised Learning
* Regression

### ⚙️ Model Used

* **Linear Regression**

### 🔁 Workflow

1. Data loading and inspection
2. Missing value handling
3. Encoding categorical variables
4. Train-test split
5. Model training
6. Prediction and evaluation
7. Visualization (Actual vs Predicted, Residual analysis)

### 📈 Evaluation Metrics

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R² Score

### 📊 Visualizations

* Actual vs Predicted Prices (Line Plot)
* Residual Plot

### 📌 Outcome

The model learns how housing features influence prices and can reasonably predict prices for unseen data.

---

## 📧 Project 2: Email Spam Classification (Logistic Regression)

### 📂 Dataset

**Spam Assassin Email Classification Dataset**
Source: [https://www.kaggle.com/datasets/ganiyuolalekan/spam-assassin-email-classification-dataset](https://www.kaggle.com/datasets/ganiyuolalekan/spam-assassin-email-classification-dataset)

### 🎯 Objective

To classify emails as:

* **Spam (1)**
* **Not Spam (0)**

### 🧠 Machine Learning Type

* Supervised Learning
* Binary Classification

### ⚙️ Model Used

* **Logistic Regression**

### 🔁 Workflow

1. Dataset loading
2. Text cleaning and preprocessing
3. Text vectorization using TF-IDF
4. Train-test split
5. Logistic Regression training
6. Model evaluation
7. Confusion matrix visualization

### 🔤 Feature Engineering

* TF-IDF Vectorization
* Stopword removal

### 📈 Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

### 📌 Outcome

The model effectively distinguishes spam from legitimate emails using textual patterns.

---

## 🛠️ Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib, Seaborn
* Jupyter Notebook / VS Code

---

## 🏁 Conclusion

This project demonstrates a complete machine learning pipeline for two fundamental problem types. The results show that linear regression and logistic regression are effective baseline models for structured data and text data respectively.

---

