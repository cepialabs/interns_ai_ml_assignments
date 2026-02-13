# 🏠 House Price Prediction & Model Comparison

---

## 📌 Project Overview

This project focuses on building and comparing regression models for predicting house prices.  
It demonstrates how ensemble learning methods like Random Forest improve prediction performance compared to traditional Linear Regression.

---

## 📂 Dataset

**House Prices Dataset**

### Original Features:

- `price` (target)
- `bedrooms`
- `bathrooms`
- `sqft_living`
- `sqft_lot`
- `floors`
- `waterfront`
- `view`
- `condition`
- `grade`
- `sqft_above`
- `sqft_basement`
- `yr_built`
- `yr_renovated`
- `lat`
- `long`
- `sqft_living15`
- `sqft_lot15`

---

## 🔧 Data Preprocessing

- Removed unnecessary columns (`id`, `date`, `zipcode`)
- Checked and handled missing values
- Split dataset into training and testing sets (80% – 20%)
- Defined features (X) and target variable (y)

---

## 🧠 Models Used

### 🔹 Linear Regression

- Used as a baseline regression model  
- Evaluated using R² score  
- Helps understand linear relationships between features and price  

### 🔹 Random Forest Regressor

- Ensemble model based on multiple decision trees  
- Reduces overfitting  
- Provides feature importance scores  
- Achieved higher R² compared to Linear Regression  

---

## 🎯 Objectives

- Train regression models for house price prediction  
- Compare model performance using R² score  
- Analyze feature importance  
- Identify key factors influencing house prices  

---

## 📊 Model Evaluation

- Performance metric used: **R² Score**
- Compared:
  - Linear Regression R²
  - Random Forest R²
- Higher R² indicates better predictive performance

---

## 📈 Feature Importance Analysis

- Extracted feature importance from Random Forest model  
- Ranked features based on importance score  
- Visualized top 10 most influential features  

Common important features include:
- `sqft_living`
- `grade`
- `bathrooms`
- `lat`
- `sqft_above`

---

## 🛠 Tools & Libraries

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Jupyter Notebook (.ipynb)

---

## 📁 Project Structure

- Data Loading  
- Data Preprocessing  
- Train-Test Split  
- Linear Regression Model  
- Random Forest Model  
- Model Comparison  
- Feature Importance Visualization  

---

## 📌 Key Learnings

- Ensemble methods improve regression performance  
- R² is an effective metric for regression evaluation  
- Property size and quality significantly influence house prices  
- Tree-based models provide interpretable feature importance  

---

## 👤 Author

**SANJAY BRAMMADANDI**

---

## 📄 License

This project is for educational purposes only.