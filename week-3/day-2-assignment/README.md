# Week 3 Assignments --- Combined README

**Intern Name:** Bodas Karunanjali\
**Intern ID:** INT2026-1462\
**Date:** 05-Feb-2026

## 📌 Assignment 1 --- Housing Price Prediction (Linear Regression)

### Objective

Predict house prices based on property features using Linear Regression.

### Dataset

Housing dataset (`housing.csv`) with key columns: - **price** --- target
variable\
- **area** --- house size\
- **bedrooms, bathrooms, stories, parking**, etc.

### Methodology

1.  Performed data exploration (`info()`, `describe()`)\
2.  Selected features: `area`, `bedrooms`\
3.  Split data into train and test sets\
4.  Trained **Linear Regression** model\
5.  Evaluated using **R² Score** and **RMSE**\
6.  Plotted Actual vs Predicted prices

### Results

-   Showed strong relationship between area and price\
-   Demonstrated usefulness of Linear Regression for prediction task

-   --------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## 📌 Assignment 1 --- Email Spam Classification (Logistic Regression)

### Objective

Build a machine learning model that classifies emails as **Spam (1)** or
**Not Spam / Ham (0)** using Logistic Regression.

### Dataset

Spam SMS dataset (`spam.csv`) with columns: - **v1** --- label (`ham` /
`spam`)\
- **v2** --- message text

### Methodology

1.  Loaded dataset with `encoding='latin-1'`\
2.  Renamed columns for clarity\
3.  Converted text to numerical features using **TF-IDF Vectorizer**\
4.  Split data into train and test sets\
5.  Trained **Logistic Regression** model\
6.  Evaluated using Accuracy and Classification Report

### Results

-   Model achieved **\~97% accuracy**\
-   Reliable detection of spam messages

### Files

    week-3/day-2-assignment/
    ├── spam.csv
    ├── assignment-2.ipynb
    └── README.md
    ├── housing.csv
    
## ✅ Overall Conclusion

These two assignments demonstrate practical use of:

-   **Logistic Regression** for classification (Spam detection)\
-   **Linear Regression** for prediction (Housing prices)

Together, they build a strong foundation in supervised machine learning
and real-world data analysis.
