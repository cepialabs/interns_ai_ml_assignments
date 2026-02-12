# Week 4 - Day 3 Assignment  
## Random Forest Model and Feature Importance  
**Date:** 12-02-2026  
**Dataset:** Spam Email Classifier / House Prices  
**Problem Type:** Supervised Machine Learning  

---

## 🎯 Objective  

The objective of this assignment is to:

- Train a Random Forest model  
- Compare performance with previous models  
- Evaluate using F1 Score (Spam) or R² Score (Housing)  
- Visualize feature importance  
- Optionally train XGBoost and compare results  

---

## 📊 Dataset Information  

**Source:** Kaggle  

- House Prices Dataset:  
  https://www.kaggle.com/datasets?search=housing+  

- Spam Email Dataset:  
  https://www.kaggle.com/datasets/nitishabharathi/email-spam-dataset  

---

## 🛠️ Technologies Used  

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Jupyter Notebook  

---

## 🧩 Steps Performed  

### 1️⃣ Data Preprocessing  

- Loaded dataset using Pandas  
- Handled missing values  
- Converted categorical variables using one-hot encoding  
- Converted spam labels to numeric  
- Vectorized text data using TF-IDF (for spam)  
- Split dataset into training and testing sets  

---

### 2️⃣ Model Training  

- Trained Random Forest model  
- Used:
  - RandomForestRegressor for Housing  
  - RandomForestClassifier for Spam  

---

### 3️⃣ Model Evaluation  

- For Housing:
  - R² Score  

- For Spam:
  - F1 Score  
  - Accuracy  

---

### 4️⃣ Feature Importance Visualization  

- Extracted feature importance from Random Forest  
- Plotted top important features using Matplotlib  

---

### 5️⃣ Optional: XGBoost  

- Trained simple XGBoost model  
- Compared performance with Random Forest  
- Observed improvement in prediction accuracy  

---

## 📈 Evaluation Metrics  

| Dataset | Metric Used |
|--------|-------------|
| Housing | R² Score |
| Spam | F1 Score, Accuracy |

---

## 🔍 Observations  

- Random Forest performed better than Linear Regression.  
- Feature importance helps understand which variables influence predictions.  
- Ensemble models like Random Forest are more powerful than single models.  
- XGBoost showed slightly better performance than Random Forest.  

---

## 🧠 Conclusion  

This assignment demonstrates the use of ensemble learning techniques such as Random Forest and XGBoost. These models provide better performance and interpretability through feature importance.

Key learnings:
- Random Forest improves model accuracy  
- Feature importance adds explainability  
- Ensemble models outperform basic models  

---

## 📌 Final Note  

This assignment strengthened understanding of ensemble learning, model evaluation, and interpretability using feature importance.
