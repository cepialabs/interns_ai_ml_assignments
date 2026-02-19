# Week 4 - Day 3 Assignment  
## Housing Price Prediction using Random Forest

##  Objective

The objective of this assignment is to:

- Train a **Random Forest Regressor** on the Housing dataset
- Evaluate the model using **R² score**
- Compare performance with previous models (e.g., Linear Regression)
- Visualize **feature importance**
- (Optional) Train and compare with **XGBoost**

## 📂 Dataset

Dataset Used: `Housing.csv`

The dataset contains the following features:

- price (Target variable)
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

The categorical features were encoded before training.

##  Preprocessing Steps

1. Loaded dataset using Pandas
2. Encoded categorical variables using Label Encoding
3. Split data into training and testing sets (80/20 split)

##  Model Used

### Random Forest Regressor

- `n_estimators = 100`
- `random_state = 42`

The model was trained on the training data and evaluated on the test data.

---

##  Evaluation Metric

The model was evaluated using:

- **R² Score**
- Mean Squared Error (MSE)

##  Feature Importance

Random Forest provides feature importance scores.

The most important features affecting house price were:

- Area
- Bathrooms

##  Model Comparison

Random Forest was compared with previous models (e.g., Linear Regression).

Observation:

- Random Forest performed better due to its ability to capture non-linear relationships.
- It handled categorical encoded features more effectively.

##  Optional: XGBoost

A simple XGBoost Regressor was also trained to compare performance with Random Forest.

##  Conclusion

- Random Forest achieved strong predictive performance on the Housing dataset.
- Area and property-related features significantly impact house price.
- Tree-based models outperform linear models for this dataset.

##  Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- XGBoost (Optional)