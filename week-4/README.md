# 🏠 House Price Feature Engineering & Feature Importance

## 📌 Project Overview
This project focuses on **feature engineering** and **feature importance analysis** for a housing price dataset.  
It demonstrates how creating new features and encoding categorical variables can improve understanding of what drives house prices.

---

## 📂 Dataset
**Housing Prices Dataset**

### Original Features:
- `price` (target)
- `area`
- `bedrooms`
- `bathrooms`
- `stories`
- `mainroad`
- `guestroom`
- `basement`
- `hotwaterheating`
- `airconditioning`
- `parking`
- `prefarea`
- `furnishingstatus`

---

## 🔧 Feature Engineering
- **Price per Square Foot**
  - Created as: `price / area`
- **Categorical Encoding**
  - Converted categorical variables into numeric form using **Label Encoding**

---

## 🧠 Models Used

### 🔹 Linear Regression
- Used to analyze **feature coefficients**
- Helps understand the **direction and strength** of each feature’s impact on price

### 🔹 Decision Tree Regressor
- Used to compute **feature importance scores**
- Shows the **relative contribution** of each feature in predicting house prices

---

## 🎯 Objectives
1. Engineer meaningful features from raw data  
2. Encode categorical variables  
3. Analyze feature importance using regression and tree‑based models  

---

## 🛠 Tools & Libraries
- Python  
- Pandas  
- NumPy  
- Scikit‑learn  
- Jupyter Notebook (.ipynb)

---

## 📊 Output
- Dataset with engineered features  
- Feature importance from Linear Regression  
- Feature importance from Decision Tree model  

---

## 📁 Project Structure

---

## 📌 Key Learnings
- Feature engineering can significantly improve model understanding
- Linear regression coefficients show influence direction
- Decision trees highlight the most important features
- Proper encoding is essential for machine learning models

---

## 👤 Author
**KARTHIKA RAVELLI**

---

## 📄 License
This project is for **educational purposes only**.