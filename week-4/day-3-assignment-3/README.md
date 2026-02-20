# 🏠 House Prices Prediction (Random Forest + Feature Importance)

This project predicts **house prices** using Machine Learning regression models.
It trains a **Random Forest Regressor** and compares its performance (R² score) with previous models.
It also visualizes **feature importance** to understand which features affect predictions the most.

---

## 📌 Dataset

**File:** `house_prices.csv`

### Columns
| Feature Columns | Description |
|---|---|
| age | Age feature |
| sex | Gender feature |
| bmi | Body Mass Index |
| bp | Blood pressure |
| s1 - s6 | Other numerical health-related features |

### Target Column
| Column | Meaning |
|---|---|
| price | Predicted output value |

---

## 🎯 Objective

- Train a **Random Forest Regression** model  
- Compare **R² score** with previous models  
- Visualize **Feature Importance**
- (Optional) Train **XGBoost Regressor** and compare results

---

## 🛠️ Libraries Used

- pandas  
- numpy  
- matplotlib  
- scikit-learn  
- xgboost (optional)

---

## ⚙️ Steps Performed

### 1️⃣ Load the dataset
- Loaded `house_prices.csv`
- Checked dataset shape, columns, and missing values

### 2️⃣ Train-Test Split
- Split the dataset into:
  - 80% training data
  - 20% testing data

### 3️⃣ Train Random Forest Model
- Trained a `RandomForestRegressor` using the training data

### 4️⃣ Evaluate Performance
- Used **R² Score** for model evaluation
- Also calculated **RMSE** (Root Mean Squared Error)

### 5️⃣ Feature Importance Visualization
- Plotted the top important features using a horizontal bar chart

### 6️⃣ (Optional) XGBoost Model
- Trained a simple `XGBRegressor`
- Compared R² score with Random Forest

---

## 📊 Evaluation Metrics

### ✅ R² Score
- Measures how well the model explains variance in the target
- Higher is better

### ✅ RMSE
- Measures average prediction error
- Lower is better

---

## 📈 Output

The notebook produces:
- Random Forest R² Score and RMSE
- Feature Importance Graph
- (Optional) XGBoost R² Score

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install pandas numpy matplotlib scikit-learn
```

(Optional for XGBoost)

```bash
pip install xgboost
```

### 2. Run the notebook

Open and run:

* `assignment_3.ipynb`

---

## 📌 Conclusion

Random Forest performs better than basic models in most cases because it:

* handles non-linear patterns
* reduces overfitting using multiple trees
* provides feature importance for interpretation

---

## 📌 Author

**Shaik Ansar**
AI/ML Intern @ Cepia Labs
---