#  Week 4 - Day 4 Assignment

Bodasu karunanjali

INT2026-1462
## House Price Prediction using 10-Fold Cross Validation

---

##  Objective

This assignment focuses on:

- Performing **10-Fold Cross Validation**
- Comparing **Linear Regression** and **Random Forest Regressor**
- Evaluating model performance using regression metrics
- Analyzing model stability and generalization

---

##  Dataset Description

The dataset contains housing information with the following features:

- price (Target Variable)
- area
- bedrooms
- bathrooms
- stories
- mainroad
- guestroom
- basement
- hotwaterheating
- airconditioning
- parking
- prefarea
- furnishingstatus

The goal is to predict **house prices** based on these features.

---

##  Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

---

##  Data Preprocessing

- Converted categorical features using **One-Hot Encoding**
- Defined:
  - X → Independent variables
  - y → Target variable (price)

---

##  Models Implemented

###  Linear Regression
- Baseline regression model
- Assumes linear relationship between features and target

###  Random Forest Regressor
- Ensemble model
- Captures non-linear relationships
- Reduces overfitting through averaging multiple trees

---

##  Cross Validation

- Used **10-Fold Cross Validation**
- Evaluated using **R² score**
- Measured stability using standard deviation across folds

---

##  Performance Metrics

Models were evaluated using:

- R² Score
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)

---

##  Results Summary

- Random Forest achieved higher R² score.
- Random Forest produced lower RMSE, indicating better prediction accuracy.
- Linear Regression showed slightly lower variance across folds.
- Random Forest captured non-linear patterns more effectively.

---

##  Stability and Generalization Analysis

- 10-Fold Cross Validation showed Random Forest generalizes better.
- Lower standard deviation across folds indicates stable performance.
- Linear Regression is simpler and easier to interpret.
- Random Forest performs better for complex housing price patterns.

---

##  Conclusion

Random Forest Regressor outperforms Linear Regression in predictive accuracy and generalization capability.

However, Linear Regression remains valuable due to:
- Simplicity
- Interpretability
- Lower computational cost

For this dataset, **Random Forest is the preferred model for house price prediction.**

---
