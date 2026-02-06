

# 📧 Spam Email Classification using KNN & Decision Tree

**Date:** 06-02-2026

## 📌 Project Overview

This project focuses on **classifying spam and non-spam emails** using supervised machine learning techniques.
Two algorithms are implemented and compared:

* **K-Nearest Neighbors (KNN)**
* **Decision Tree (Entropy criterion)**

The objective is to understand algorithm behavior on a **high-dimensional, word-count-based dataset** and evaluate their performance.

---

## 📊 Dataset Description

* **Type:** Spam Email Dataset (pre-processed)
* **Features:** Word frequency counts (≈ 3000 features)
* **Target Column:** `Prediction`

  * `1` → Spam
  * `0` → Not Spam
* **Notes:**

  * Dataset is already vectorized (Bag-of-Words)
  * No text preprocessing or TF-IDF required
  * Identifier column `Email No.` was removed

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Jupyter Notebook

---

## 🧠 Machine Learning Models

### 🔹 K-Nearest Neighbors (KNN)

* Feature scaling applied using **StandardScaler**
* Distance-based classification
* Sensitive to feature scale

### 🔹 Decision Tree

* Splitting criterion: **Entropy (Information Gain)**
* Tree depth limited to prevent overfitting
* Provides feature importance for interpretability

---

## 🔬 Methodology

1. Load dataset and remove non-informative columns
2. Separate features (`X`) and target (`y`)
3. Split data into training and testing sets
4. Apply feature scaling for KNN
5. Train and evaluate KNN model
6. Train and evaluate Decision Tree model
7. Compare model performance using evaluation metrics

---

## 📈 Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-Score

These metrics help assess how effectively each model classifies spam emails.

---

## 🏆 Key Observations

* Decision Tree performed better in interpretability due to feature importance
* KNN required feature scaling for optimal performance
* Entropy criterion provided clear information-based splits
* Decision Trees are more suitable for explaining results in real-world spam detection

---


## ✅ Conclusion

This project demonstrates the effectiveness of Decision Trees and KNN for spam email classification.
Decision Trees using entropy are particularly useful for understanding which words contribute most to spam detection, making them a strong choice for interpretable machine learning models.

---



