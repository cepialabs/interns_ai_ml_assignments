# Machine Learning Assignment — Feature Scaling, Regression & Classification
 Bodasu karunanjali
 
 INT2026-1462

## Objective  
The objective of this assignment is to:  

- Understand the importance of feature scaling in machine learning  
- Apply scaling techniques to real-world datasets  
- Compare model performance before and after scaling  
- Implement both regression and classification models  

## Dataset Description  

### Dataset 1 — Housing Dataset (Regression)  
This dataset contains information about residential houses such as:  

- Area  
- Number of bedrooms  
- Bathrooms  
- Parking  
- Air conditioning  
- Main road availability  
- Furnishing status  
- and other related features  

**Target variable:**  
- `price` (continuous numerical value)  

### Dataset 2 — Email Dataset (Classification)  
This dataset contains email messages labeled as:  

- `spam`  
- `not spam`  

**Target variable:**  
- `type` (binary class label: spam = 1, not spam = 0)

## Methodology  

### Task 1 — House Price Prediction (Regression)  

Steps performed:  

1. Loaded and explored the housing dataset  
2. Converted categorical features to numeric values  
3. Split data into training and testing sets  
4. Trained a **Linear Regression model before scaling**  
5. Applied **Standard Scaling** to numerical features  
6. Retrained the model after scaling  
7. Compared performance using:  
   - R² Score  
   - RMSE (Root Mean Squared Error)  

### Task 2 — Email Spam Classification  

Steps performed:  

1. Loaded the email dataset  
2. Cleaned and standardized labels (`spam`, `not spam`)  
3. Converted text data into numerical form using **TF-IDF Vectorization**  
4. Split data into train and test sets  
5. Trained a **Logistic Regression classifier before scaling**  
6. Applied scaling (where applicable)  
7. Retrained the model and compared performance using **Accuracy Score**

## Results  

- Feature scaling improved the performance and stability of the regression model.  
- Proper text preprocessing and vectorization significantly improved classification results.  
- Logistic Regression performed well for spam detection after TF-IDF transformation.  

## Files in this Repository  

Untitled6.ipynb       # Main Jupyter Notebook containing full implementation  
housing_data.csv      # Housing dataset  
email_data.csv        # Email spam dataset  
README.md             # Assignment documentation  

## Tools and Technologies Used  

- Python  
- Pandas  
- NumPy  
- Scikit-Learn  
- Jupyter Notebook  
- Git & GitHub  


## Conclusion  

This assignment demonstrates the practical impact of feature scaling on machine learning models and highlights the importance of data preprocessing in both regression and classification tasks.
