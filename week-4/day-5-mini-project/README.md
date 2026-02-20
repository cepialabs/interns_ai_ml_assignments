# 🏠 House Price Prediction (Kaggle-Style Mini Project)

## 📌 Project Objective

This mini project focuses on building a **Kaggle-style machine learning pipeline** to predict house prices using real-world housing data.

The goal is to:

* Understand the dataset
* Perform preprocessing + feature engineering
* Train multiple regression models
* Compare models using cross-validation
* Visualize results
* Provide insights and recommendations

---

## 📂 Dataset Information

**Dataset Name:** House Price India
**File Used:** `House Price India.csv`
**Rows:** 14619
**Columns:** 23
**Target Variable:** `Price`

This dataset contains multiple real estate features, such as:

* bedrooms, bathrooms, floors
* living area, lot area
* basement area
* condition, grade
* latitude and longitude
* distance from airport, nearby schools, etc.

---

## 🧠 Machine Learning Problem Type

✅ **Regression Problem**
Because the target variable (`Price`) is a continuous numeric value.

---

## 📁 Project Structure

```
Mini_Project_House_Prices/
│── mini_project.ipynb
│── House Price India.csv
│── README.md
```

---

# ✅ Workflow (Step-by-Step)

## 1️⃣ Dataset Understanding

### What was done?

* Loaded dataset using Pandas
* Checked:

  * shape (rows, columns)
  * first few rows
  * dataset info (data types)
  * descriptive statistics

### Why?

To understand:

* Which features are numeric/categorical
* Whether missing values exist
* What the target column is

---

## 2️⃣ Data Cleaning

### What was done?

* Dropped the column:

  * `id` (unique identifier, not useful for prediction)
* Checked missing values
* Used imputation methods:

  * numerical → median
  * categorical → most frequent

### Why?

Machine learning models cannot handle missing values directly, so we must fill them properly.

---

## 3️⃣ Feature Engineering

Feature engineering was performed to create stronger and more meaningful features.

### New Features Created:

| Feature Name      | Meaning                              | Why it helps                     |
| ----------------- | ------------------------------------ | -------------------------------- |
| `HouseAge`        | Age of house = max year - built year | older houses may cost less       |
| `Renovated`       | 1 if renovation year ≠ 0 else 0      | renovated houses often cost more |
| `TotalArea`       | living area + lot area               | total size impacts price         |
| `BasementRatio`   | basement area / living area          | basement adds value              |
| `LivingRenovDiff` | renovated living area - living area  | indicates improvements           |

---

## 4️⃣ Preprocessing Pipeline (Kaggle Style)

A professional preprocessing pipeline was created using:

* `Pipeline`
* `ColumnTransformer`

### Numerical features preprocessing:

* Missing values → median
* Scaling → StandardScaler

### Categorical preprocessing:

* Missing values → most frequent
* Encoding → OneHotEncoder

### Why pipeline?

Because it ensures:

* clean workflow
* no data leakage
* reproducibility
* easy model switching

---

## 5️⃣ Models Trained

We trained multiple models to compare performance.

### Models Used:

1. **Linear Regression (Baseline)**
2. **Ridge Regression**
3. **Random Forest Regressor**
4. **Gradient Boosting Regressor**
5. *(Optional)* XGBoost (if installed)

### Why multiple models?

Because in Kaggle-style challenges, we always test:

* baseline model
* tree-based ensembles
* boosting models (best performance)

---

## 6️⃣ Model Evaluation

Evaluation was done using:

### Metrics:

* **RMSE (Root Mean Squared Error)**
  Lower RMSE = better predictions

* **R² Score**
  Higher R² = better fit

### Cross Validation:

* 5-Fold Cross Validation was used to ensure:

  * stable performance
  * generalization
  * less overfitting

---

## 7️⃣ Hyperparameter Tuning

To improve model performance, **RandomizedSearchCV** was applied on Random Forest.

### Parameters tuned:

* `n_estimators`
* `max_depth`
* `min_samples_split`
* `min_samples_leaf`
* `max_features`

### Why?

Random Forest performance depends heavily on hyperparameters.
Tuning improves accuracy and reduces RMSE.

---

## 8️⃣ Visualization & Interpretation

The following plots were generated:

### ✅ Predicted vs Actual Plot

Shows how close predictions are to true prices.

### ✅ Residual Plot

Shows prediction errors.
If residuals are randomly scattered → good model.

### ✅ Feature Importance Plot

Shows which features affect price the most.

---

# 📊 Final Results Summary

After comparing multiple models:

* Baseline Linear Regression gave a basic reference.
* Ensemble models performed better.
* Random Forest / Boosting models achieved best generalization.
* Feature engineering improved model performance.

---

# 🔍 Key Insights

* Living area and grade of house strongly influence price.
* Location (latitude/longitude) impacts house price.
* Renovation information is important.
* Total area and basement area contribute significantly.
* Tree-based models perform better than linear models due to non-linear patterns.

---

# 💡 Recommendations (Future Improvements)

To further improve performance:

✅ Apply `log1p(Price)` transformation
✅ Remove extreme outliers (very high price houses)
✅ Add location clustering using latitude & longitude
✅ Try XGBoost / LightGBM with tuning
✅ Try stacking models for best Kaggle score

---

# ⚙️ How to Run the Project

### Step 1: Install dependencies

```bash
pip install numpy pandas matplotlib scikit-learn
```

(Optional for XGBoost)

```bash
pip install xgboost
```

### Step 2: Run the notebook

Open:

```
mini_project.ipynb
```

Run cells from top to bottom.

---

# 🧾 Conclusion

This project successfully demonstrates a full Kaggle-style ML workflow:

* dataset understanding
* preprocessing pipelines
* feature engineering
* multiple model training
* cross-validation evaluation
* hyperparameter tuning
* visualization
* insights and recommendations

---

## 👤 Author

**Shaik Ansar**
Mini Project — Kaggle Style ML Challenge
