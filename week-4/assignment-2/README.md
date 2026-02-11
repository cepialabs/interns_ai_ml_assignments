# Machine Learning Feature Scaling Project

## Objective

This project demonstrates how scaling numerical features impacts:

- Regression models (House Price Prediction)
- Classification models (Spam Email Detection)

---

## Datasets

### 1. House Prices (Regression)
Features:
- Size
- Bedrooms
- Age
- DistanceToCity

Target:
- Price

### 2. Spam Emails (Classification)
Features:
- WordFreq_Free
- WordFreq_Money
- EmailLength
- NumLinks

Target:
- Spam (0 = Not Spam, 1 = Spam)

---

## Steps Performed

1. Load dataset
2. Split into train and test sets
3. Train model WITHOUT scaling
4. Apply StandardScaler
5. Retrain model WITH scaling
6. Compare performance metrics

---

## Observations

### Linear Regression
Scaling typically does not change performance significantly
because Linear Regression is scale-invariant.

### Logistic Regression
Scaling often improves convergence speed and model stability,
especially when features vary widely in magnitude.

---

## How to Run

1. Install dependencies:
   pip install pandas numpy scikit-learn

2. Open:
   ML_Scaling_Project.ipynb

3. Run all cells.

---

## Author
B. SANJAY