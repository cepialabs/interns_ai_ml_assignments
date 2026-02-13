# 🏠 House Price Prediction with Cross-Validation

## 📌 Project Objective
Build and evaluate machine learning models to predict house prices using a real-world dataset.  
The project focuses on **model performance, stability, and generalization** using **cross-validation**.

---

## 📂 Dataset
**House Sales Dataset**

**Target Variable**
- `price` – Sale price of the house

**Key Features**
- Bedrooms, bathrooms, living area, lot size
- Floors, waterfront, condition, grade
- Year built, renovation year
- Location features (zipcode, latitude, longitude)

---

## 🧠 Models Implemented
1. **Linear Regression**
   - Baseline model
   - High interpretability
   - Assumes linear relationships

2. **Random Forest Regressor**
   - Ensemble-based model
   - Captures non-linear relationships
   - Strong generalization capability

---

## ⚙️ Machine Learning Workflow

### 1. Data Preprocessing
- Converted date into `sale_year` and `sale_month`
- Removed non-informative identifiers
- Standardized numerical features
- Train-test split (80/20)

### 2. Model Training
- Trained models using pipelines
- Ensured consistent preprocessing across models

### 3. Model Evaluation
- Metrics used:
  - **RMSE (Root Mean Squared Error)**
  - **R² Score**
- Evaluated on unseen test data

### 4. Cross-Validation
- **5-Fold Cross-Validation**
- **10-Fold Cross-Validation**
- Compared:
  - Mean RMSE
  - Standard deviation (stability indicator)

---

## 📊 Results Summary

### Linear Regression
- Stable performance across folds
- Higher RMSE
- High bias, low variance

### Random Forest
- Lower RMSE and higher R²
- Slightly higher variance
- Better generalization to unseen data

### Cross-Validation Insights
- 10-fold CV provides smoother and more reliable estimates
- Random Forest generalizes better despite higher computational cost
- Reduced-complexity models were used during CV for efficiency

---

## 📈 Visualizations
- Predicted vs Actual price plot
- Feature importance ranking (Random Forest)

---

## ✅ Key Insights
- Living area (`sqft_living`) and grade are strong price drivers
- Location features significantly impact house prices
- Ensemble models outperform linear models for complex real-world data

---

## 🧪 Model Stability & Generalization
- Low standard deviation across folds indicates stable models
- Random Forest shows strong generalization
- Linear Regression useful as a baseline and for explainability

---

## 🚀 Recommendations
- Use **Random Forest** for production-level predictions
- Use **Linear Regression** for benchmarking and interpretability
- Apply reduced model complexity during cross-validation for faster iteration

---

## 🛠️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn

---

## 📌 Future Improvements
- Hyperparameter tuning with GridSearchCV
- SHAP-based explainability
- Try Gradient Boosting or XGBoost
- Log-transform target variable for skew reduction

---
