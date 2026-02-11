# Week 4 - day 2 Assignment - Feature Scaling and Model Comparison
**Date:** 11-02-2026  
**Dataset Used:** House Prices and spam dataset
**Problem Type:** Regression  

---

## 🎯 Objective

The objective of this assignment is to:

- Scale numerical features
- Train regression model before scaling
- Train regression model after scaling
- Compare model performance
- Observe changes in evaluation metrics

---

## 📊 Dataset Information

- Source: Kaggle 
-  House Prices Dataset Url: https://www.kaggle.com/datasets?search=housing+
- spam email data set Url: https://www.kaggle.com/datasets/nitishabharathi/email-spam-dataset
- Target Variable: SalePrice
- Type: Supervised Machine Learning (Regression)

---

## 🛠️ Steps Performed

### 1️⃣ Data Preprocessing

- Loaded dataset using pandas
- Handled missing values
- Converted categorical variables using one-hot encoding
- Split dataset into training and testing sets

---

### 2️⃣ Model Training (Without Scaling)

- Used Linear Regression model
- Trained on original features
- Evaluated using:
  - MAE
  - MSE
  - RMSE
  - R² Score

---

### 3️⃣ Feature Scaling

- Applied **StandardScaler**
- Scaled training and test data separately
- Ensured no data leakage

---

### 4️⃣ Model Training (After Scaling)

- Retrained Linear Regression on scaled data
- Evaluated using same metrics
- Compared results

---

## 📈 Evaluation Metrics Used

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R2 Score

---

## 🔍 Observations

- Scaling ensures features are on similar range.
- Linear Regression performance remains similar because it is less sensitive to scaling.
- Scaling is more important for models like:
  - Logistic Regression
  - KNN
  - SVM
  - Gradient Descent models

---

## 🧠 Conclusion

- Successfully applied feature scaling.
- Compared model performance before and after scaling.
- Understood importance of scaling in machine learning.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook
