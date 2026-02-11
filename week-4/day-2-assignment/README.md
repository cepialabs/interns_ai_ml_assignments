# 📊 Feature Scaling 
* **DATE:** 11 February 2026

This repository demonstrates the impact of **feature scaling** on machine learning models using **regression** and **classification** tasks.

Two real-world datasets are used:

* **Ames Housing Dataset** – Regression problem
* **SpamAssassin Email Dataset** – Classification problem


---

## 🏠 Dataset 1: Ames Housing Dataset (Regression)

### 🔹 Data Source

* **Name:** Ames Housing Dataset
* **Provider:** Kaggle
* **Link:** [https://www.kaggle.com/datasets/prevek18/ames-housing-dataset](https://www.kaggle.com/datasets/prevek18/ames-housing-dataset)

### 🔹 Objective

Predict house prices and observe how feature scaling affects regression models.

### 🔹 Features

Only **numerical features** are used (e.g., area, year built, number of rooms).

### 🔹 Models Used

* Linear Regression
* Ridge Regression

### 🔹 Steps Performed

1. Load and clean the dataset
2. Select numerical features
3. Split data into training and testing sets
4. Train regression models **without scaling**
5. Apply **StandardScaler**
6. Retrain models **with scaling**
7. Compare performance using **R² Score** and **RMSE**

### 🔹 Key Observations

* Linear Regression shows minimal change after scaling
* Ridge Regression performs better after scaling
* Scaling stabilizes coefficients and improves regularization

---

## 📧 Dataset 2: SpamAssassin Email Dataset (Classification)

### 🔹 Data Source

* **Name:** SpamAssassin Email Dataset
* **Provider:** Kaggle
* **Link:** [https://www.kaggle.com/datasets/ganiyuolalekan/spam-assassin-email-classification-dataset](https://www.kaggle.com/datasets/ganiyuolalekan/spam-assassin-email-classification-dataset)

### 🔹 Objective

Classify emails as **spam** or **not spam** and analyze the effect of feature scaling.

### 🔹 Dataset Structure

* `text` → email content
* `target` → spam (1) or ham (0)

### 🔹 Models Used

* Logistic Regression
* K-Nearest Neighbors (KNN)

### 🔹 Steps Performed

1. Load the dataset
2. Convert text data to numerical features using **TF-IDF Vectorization**
3. Split data into training and testing sets
4. Train classifiers **without scaling**
5. Apply **StandardScaler (with_mean=False)**
6. Retrain classifiers **with scaling**
7. Compare performance using **Accuracy, Precision, Recall, and F1-score**

### 🔹 Key Observations

* Logistic Regression performs better after scaling
* KNN shows significant improvement after scaling
* Feature scaling is essential for distance-based models

---

## 📈 Overall Conclusion

Feature scaling plays a crucial role in machine learning. While simple linear regression is mostly unaffected, models such as Ridge Regression, Logistic Regression, and KNN benefit significantly from scaling. Scaling ensures equal feature contribution, faster convergence, and improved model performance.

---

## 🛠 Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* Jupyter Notebook

---

✨ This project fulfills the  requirement of analyzing the impact of feature scaling on machine learning models.
