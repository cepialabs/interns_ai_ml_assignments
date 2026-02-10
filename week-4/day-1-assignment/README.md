# House Price Feature Engineering
Bodasu karunanjali

INT2026-1462

## Project Overview
This project performs feature engineering on a house price dataset using Python in Jupyter Notebook. The main goal is to create meaningful features, prepare data for machine learning, and understand the key factors affecting house prices.

The notebook includes:
- Loading and understanding the dataset  
- Creating new features  
- Encoding categorical variables  
- Analyzing feature importance  

---

## Dataset
The dataset contains the following house attributes:

- price – Target variable (house price)  
- area – Size of the house  
- bedrooms – Number of bedrooms  
- bathrooms – Number of bathrooms  
- stories – Number of floors  
- mainroad, guestroom, basement – House amenities  
- hotwaterheating, airconditioning – Comfort features  
- parking, prefarea – Location preferences  
- furnishingstatus – Furnished, Semi-furnished, or Unfurnished  

---

## Tasks Performed

## Task 1 – House Age (Proxy Feature)
Since the dataset did not include a Year Built column, an approximate House_Age_Proxy feature was created using related attributes such as:

- Number of stories  
- Presence of basement  
- Furnishing status  

This acts as an estimated measure of how old or modern a house might be.

---

## Task 2 – Price per Square Foot
A new feature was created using:

Price_per_sqft = price / area

This helps compare house prices fairly based on size.

---

## Task 3 – Encode Categorical Features
Categorical columns such as:

- mainroad  
- guestroom  
- basement  
- hotwaterheating  
- airconditioning  
- prefarea  
- furnishingstatus  

were converted into numerical form using One-Hot Encoding so that machine learning models can process them.

---

## Task 4 – Feature Importance Analysis
A Random Forest Regressor model was trained to analyze which features most influence house prices.

Typically important features include:
- area  
- bathrooms  
- airconditioning  
- price_per_sqft  

---

## Tools Used
- Python  
- Pandas  
- Scikit-learn  
- Jupyter Notebook  

---

## Conclusion
This project demonstrates how feature engineering can improve data quality and help build better predictive models for house prices.

---

