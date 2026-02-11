# 🏠 House Price Prediction with Feature Scaling

## Project Overview

This project demonstrates the importance of feature scaling in machine learning using a House Prices dataset.  
Regression models are trained before and after scaling numerical features to observe changes in performance.

---

## Dataset

The dataset contains housing-related features such as:

- bedrooms  
- bathrooms  
- sqft_living  
- sqft_lot  
- floors  
- waterfront  
- view  
- condition  
- grade  
- yr_built  
- zipcode  
- latitude and longitude  

Target column:

- price  

Sample columns:

id, date, price, bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, grade, sqft_above, sqft_basement, yr_built, yr_renovated, zipcode, lat, long, sqft_living15, sqft_lot15

---

## Technologies Used

- Python  
- Pandas  
- Scikit-learn  
- Jupyter Notebook / VS Code  

---

## Models Used

- Linear Regression  
- KNN Regressor (optional)

---

## Workflow

1. Load dataset  
2. Separate features and target  
3. Split data into training and testing sets  
4. Train model without scaling  
5. Apply StandardScaler  
6. Train model with scaling  
7. Compare results  

---

## Results

### Linear Regression

Performance remains almost the same before and after scaling because Linear Regression is scale-independent.

### KNN Regressor (Optional)

Performance improves significantly after scaling because KNN is distance-based.

---

## Conclusion

Feature scaling ensures all numerical features contribute equally to model training.

Linear Regression shows minimal change after scaling, while KNN shows noticeable improvement.  
This highlights why scaling is an important preprocessing step in machine learning.

---

## How to Run

1. Place your dataset as `house_data.csv` in the project folder.

2. Install required libraries:

pip install pandas scikit-learn

3. Run your Python script or notebook.

---

## Author

**Swati M Patil**