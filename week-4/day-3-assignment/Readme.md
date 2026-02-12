#  House Price Prediction using Random Forest
Bodasu karunanjali

INT2026-1462

##  Project Overview
This project implements a **House Price Prediction model** using Machine Learning.  
The goal is to train a **Random Forest model** and compare its performance with a previous model (Linear Regression), evaluate results using **R² score**, and visualize feature importance.

This project is part of a Machine Learning assignment.

---

##  Objectives
- Load and preprocess housing dataset
- Train Linear Regression model (baseline model)
- Train Random Forest model
- Compare model performance using R² score
- Visualize feature importance
- Train XGBoost model (optional)

---

##  Dataset
- Dataset used: **Housing.csv**
- The dataset contains housing features such as:
  - Area
  - Bedrooms
  - Bathrooms
  - Stories
  - Parking
  - Price (target variable)

---

##  Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost (optional)
- Jupyter Notebook

---

##  Project Workflow

###  Import Libraries
Required Python libraries for data processing and model training are imported.

###  Load Dataset
Housing dataset is loaded using Pandas.

###  Data Preprocessing
Categorical variables are converted into numerical format using one-hot encoding.

###  Train-Test Split
Dataset is divided into training and testing sets.

###  Train Linear Regression Model
Linear Regression is used as the baseline model.

###  Train Random Forest Model
Random Forest Regressor is trained to improve prediction accuracy.

###  Model Comparison
Performance of models is compared using R² score.

###  Feature Importance Visualization
Important features affecting house price are visualized.

###  Optional: XGBoost Model
XGBoost model is trained for additional performance comparison.

---

## Evaluation Metric
- **R² Score (Coefficient of Determination)**
- Higher R² score indicates better model performance.

---

##  Results
- Random Forest performed better than Linear Regression.
- Feature importance analysis showed key factors affecting house prices.
- XGBoost (optional) can further improve performance.
