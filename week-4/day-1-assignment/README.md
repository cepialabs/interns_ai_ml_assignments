# Feature Engineering on House Prices Dataset week 4 day 1
- **Date:** 10-02-2026  
- **Dataset:** House Prices  

---

## Objective
The objective of this assignment is to apply feature engineering techniques on
the House Prices dataset to improve data quality and model understanding.

---

## Dataset Information
- Source: Kaggle
- Problem Type: Regression
- Target Variable: House Price
- data set URL :https://www.kaggle.com/datasets?search=housing+



---

## Tasks Performed

### 1. Feature Extraction
- Created a new feature **house_age** from the `YearBuilt` column  
- Formula used: house_age = current_year - year_built
### 2. Feature Creation
- Created **price_per_square_foot** feature  
- Helps compare house prices based on size

### 3. Encoding Categorical Features
Categorical variables were converted into numeric form using:
- One-Hot Encoding
- Label Encoding  

Encoded features include:
- Neighborhood
- Condition

### 4. Feature Importance Analysis
- Applied a simple regression / tree-based model
- Analyzed feature importance to identify key factors affecting house prices

---

## Tools & Libraries Used
- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib / Seaborn
- Scikit-learn

---

## Observations
- Feature engineering improved understanding of the dataset
- Encoded categorical features helped in model training
- Feature importance analysis highlighted influential variables

---

## Conclusion
This assignment demonstrates the importance of feature engineering in machine
learning. Creating new features and selecting important ones leads to better
model performance.

---
