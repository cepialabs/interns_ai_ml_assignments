# 🏠 House Price Prediction using Random Forest (Assignment-2)

This project predicts **house prices** using Machine Learning regression models on the dataset `house_data.csv`.

The main goal of this assignment is to:
- Train a **Random Forest Regressor**
- Compare its **R² score** with previous models
- Visualize **feature importance**
- (Optional) Train a simple **XGBoost Regressor** and compare results

---

## 📌 Dataset Information

**Dataset File:** `house_data.csv`  
**Total Rows:** 21,613  
**Total Columns:** 21  

### 🎯 Target Column
- **price** → House price (Regression output)

### 📊 Feature Columns
- id  
- date  
- bedrooms  
- bathrooms  
- sqft_living  
- sqft_lot  
- floors  
- waterfront  
- view  
- condition  
- grade  
- sqft_above  
- sqft_basement  
- yr_built  
- yr_renovated  
- zipcode  
- lat  
- long  
- sqft_living15  
- sqft_lot15  

---

## 🎯 Objective of the Assignment

✔ Train a Random Forest model  
✔ Evaluate using **R² score**  
✔ Compare with previous models (Linear Regression / Decision Tree)  
✔ Plot feature importance graph  
✔ (Optional) Train XGBoost and compare performance  

---

## 🛠️ Technologies / Libraries Used

- Python  
- pandas  
- numpy  
- matplotlib  
- scikit-learn  
- xgboost *(optional)*  

---

## ⚙️ Project Workflow

### 1️⃣ Data Loading
- Loaded `house_data.csv`
- Checked dataset shape, columns, and missing values

### 2️⃣ Preprocessing
- Separated input features (X) and target (y)
- Removed unnecessary columns (like `id`)
- Converted `date` to a usable numeric format (or dropped it)

### 3️⃣ Train-Test Split
- Split data into:
  - 80% Training set  
  - 20% Testing set  

### 4️⃣ Model Training
Models trained:
- Previous baseline model(s) (Linear Regression / Decision Tree)
- **Random Forest Regressor**
- (Optional) **XGBoost Regressor**

### 5️⃣ Model Evaluation
Metrics used:
- **R² Score** (Main metric)
- **RMSE** (Optional)

### 6️⃣ Feature Importance Visualization
- Plotted top features that influence house price prediction using Random Forest feature importance

---

## 📊 Evaluation Metrics

### ✅ R² Score
Shows how well the model explains the variance in house prices.  
- Higher value = better model

### ✅ RMSE
Shows average prediction error.  
- Lower value = better model

---

## ▶️ How to Run This Project

### Step 1: Install required libraries
```bash
pip install pandas numpy matplotlib scikit-learn
```

(Optional for XGBoost)

```bash
pip install xgboost
```

### Step 2: Run the notebook

Open and run:

* `assignment-2.ipynb`

---

## 📈 Output

The notebook generates:

* R² score for each model
* Comparison of model performances
* Feature importance bar chart
* (Optional) XGBoost results

---

## ✅ Conclusion

Random Forest generally performs better than basic regression models because:

* It captures non-linear patterns
* It reduces overfitting using multiple trees
* It provides feature importance for interpretability

---

## 📌 Author

**Shaik Ansar**
AI/ML Intern @ Cepia Labs
---