# House Price Prediction – Random Forest & XGBoost

This Assignment trains and evaluates machine learning models on a **house price dataset**.

## Objectives
- Train a **Random Forest** model
- Compare **R² score** with previous models
- Visualize **feature importance**
- (Optional) Train an **XGBoost** model and compare results

---

## Project Structure
```
.
├── house_prices.csv
├── train_models.py
├── README.md
```

---

## Requirements
```bash
pip install pandas numpy scikit-learn matplotlib xgboost
```

---

## Model Training

### Random Forest
- No feature scaling required
- Robust to outliers
- Provides built-in feature importance

### XGBoost (Optional)
- Gradient boosting model
- Often achieves higher R²
- Requires tuning for best performance

---

## Evaluation Metrics
- **R² Score** (primary)
- **RMSE** (secondary)

> For classification tasks, replace R² with **F1 score**.

---

## Feature Importance
Random Forest feature importance is visualized using a bar chart showing the most influential features.

---

## How to Run
```bash
python train_models.py
```

---

## Results Interpretation
- Higher **R²** indicates better predictive performance
- Feature importance highlights which house attributes most affect price

---

## Extensions
- Hyperparameter tuning (GridSearchCV)
- SHAP explainability
- Cross-validation
- Model persistence (joblib)

