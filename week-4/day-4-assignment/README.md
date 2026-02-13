
# 📧 Logistic Regression and Random Forest for Spam Email Classification

**📅 Date:** 13 February 2026

---

## 📌 Project Overview

This project focuses on building and evaluating **spam email classification models** using **Logistic Regression** and **Random Forest**.
The models are compared using **5-fold and 10-fold Cross-Validation** to analyze **performance, stability, and generalization**.

---

## 📊 Dataset

* **Dataset Name:** Spam Assassin Email Classification Dataset
* **Source:** Kaggle
* **Dataset Link:**
  👉 [https://www.kaggle.com/datasets/ganiyuolalekan/spam-assassin-email-classification-dataset](https://www.kaggle.com/datasets/ganiyuolalekan/spam-assassin-email-classification-dataset)

### Dataset Description

* `text` → Email content

* `target` → Label

  * `0` = Ham (Not Spam)
  * `1` = Spam

* **Problem Type:** Binary Classification

* **Data Type:** Text data (emails)

---

## ⚙️ Technologies Used

* **Programming Language:** Python
* **Libraries:**

  * pandas
  * numpy
  * scikit-learn
  * matplotlib

---

## 🔄 Methodology

### 1️⃣ Data Preprocessing

* Removed rows with missing values
* Ensured correct data types
* Converted email text into numerical features using **TF-IDF**

### 2️⃣ Models Implemented

* **Logistic Regression** – baseline linear classifier
* **Random Forest Classifier** – ensemble-based non-linear model

### 3️⃣ Cross-Validation Strategy

* **5-Fold Stratified Cross-Validation**
* **10-Fold Stratified Cross-Validation**
* Stratification ensures balanced spam/ham distribution in each fold

### 4️⃣ Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-score

---

## 📈 Results & Analysis

### 🔹 Performance Comparison

* Random Forest achieved higher overall performance
* Logistic Regression provided strong baseline results

### 🔹 Model Stability

* Logistic Regression showed lower variance across folds
* Random Forest variance decreased with 10-fold cross-validation

### 🔹 Generalization

* 10-fold CV produced more reliable performance estimates
* Random Forest benefited more from increased training data

---

## 📊 Visualization

* Bar chart comparing **F1-score standard deviation**
* Used to analyze **model stability and consistency**

---

## ✅ Conclusion

* **Best Performing Model:** Random Forest
* **Most Stable Model:** Logistic Regression
* **Best Evaluation Strategy:** 10-Fold Cross-Validation

Random Forest with 10-fold cross-validation offers the best balance between performance and generalization, while Logistic Regression serves as a strong and interpretable baseline.


---

