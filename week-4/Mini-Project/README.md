# 📊 Customer Churn Prediction Using Machine Learning

## 📌 Project Objective

Apply advanced machine learning techniques to predict customer churn and maximize model performance on a real-world dataset.  
This project demonstrates a full ML pipeline including data understanding, feature engineering, preprocessing, ensemble modeling, evaluation, visualization, and business recommendations.

---

## 🧠 Problem Statement

Customer churn directly impacts revenue.  
The goal is to build a classification model that predicts whether a customer will churn (1) or not (0), and extract insights to help reduce churn.

---

## 🗂 Dataset Overview

The dataset contains customer-level information:

- Demographics: age, gender  
- Account details: tenure, contract type, payment method  
- Usage behavior: monthly charges, support tickets  
- Financial metrics: total charges, lifetime value  
- Target variable: **churn**

Total records: 200

Missing values were found in the `internet_service` column.

---

## 🔄 Project Workflow

### 1️⃣ Dataset Understanding

- Identified target variable (`churn`)
- Checked data types and missing values
- Separated categorical and numerical features
- Performed statistical analysis using `.describe()` and `.info()`

---

### 2️⃣ Feature Engineering

Created new features:

- `avg_monthly_spend_ratio`  
  = total_charges / (tenure_months + 1)

- `high_support_usage`  
  = 1 if support_tickets ≥ 3, else 0

These features capture customer spending behavior and service dependency.

---

### 3️⃣ Data Preprocessing

- Numerical columns:
  - Median imputation
  - Standard scaling

- Categorical columns:
  - Most frequent imputation
  - One-hot encoding

Used `Pipeline` and `ColumnTransformer` to automate preprocessing.

---

### 4️⃣ Train-Test Split

- 80% training / 20% testing
- Stratified by churn to preserve class balance

---

### 5️⃣ Model Building

Trained three models:

- Logistic Regression (baseline)
- Random Forest Classifier
- XGBoost Classifier

Purpose:

- Baseline model provides reference performance
- Ensemble models capture non-linear patterns and feature interactions

---

### 6️⃣ Model Evaluation

Metrics used:

- Accuracy
- F1 Score
- 5-Fold Cross Validation

All models achieved strong performance on this dataset.

---

### 7️⃣ Visualization & Interpretation

- Confusion Matrix for classification performance
- Feature Importance plot from XGBoost

Top contributing features:

- Lifetime value  
- Support tickets  
- Monthly charges  
- High support usage  
- Tenure months  

---

## 🧠 Key Insights

- Customers with high support ticket volume are much more likely to churn  
- Month-to-month contracts have higher churn risk  
- Longer tenure significantly reduces churn probability  
- Higher lifetime value customers tend to stay longer  

---

## ✅ Business Recommendations

- Encourage long-term contracts using discounts or loyalty programs  
- Proactively engage customers with high support usage  
- Offer retention incentives after 6–12 months of tenure  
- Monitor customers with rising monthly charges  

---

## 🛠 Technologies Used

- Python  
- Pandas & NumPy  
- Scikit-learn  
- XGBoost  
- Matplotlib & Seaborn  

---

## ▶ How to Run This Project

### 1. Clone Repository

git clone https://github.com/cepialabs/interns_ai_ml_assignments


### 2. Install Dependencies

pip install pandas numpy scikit-learn xgboost matplotlib seaborn

### 3. Run Notebook

Open Jupyter Notebook and execute:

customer_churn_ml.ipynb

---

## 📁 Project Structure


├── customer_churn_ml.csv
├── customer_churn_ml.ipynb
├── README.md

---

## 🎤 Interview Summary (How to Explain)

“I started by understanding the dataset and identifying missing values and feature types.  
Then I performed feature engineering and built preprocessing pipelines for numerical and categorical data.  
I trained a baseline Logistic Regression model followed by Random Forest and XGBoost.  
Models were evaluated using F1 score and cross-validation.  
I visualized feature importance and confusion matrices to interpret results.  
Finally, I derived business insights and provided actionable churn reduction strategies.”

---

## ✍ Author

**Swati M Patil**  
Machine Learning / Data Analytics Project

---

## 📌 Final Summary

This project demonstrates an end-to-end machine learning workflow including preprocessing, feature engineering, ensemble modeling, evaluation, visualization, and business-driven recommendations for customer churn prediction.