# Week 3 – Day 2 Assignments  
📅 **Date:** 5 February 2026  
📘 **Subject:** Machine Learning – Supervised Learning  
👩‍🎓 **Student Name:** Seerat Metkari  

---

## 📌 Assignment 1: Housing Price Prediction

### 🔹 Objective
To predict house prices using multiple housing features such as area, number of bedrooms, bathrooms, parking, and other amenities using a **supervised regression model**.

---

### 🔹 Dataset Description
The housing dataset contains the following columns:

- `price` (Target Variable)
- `area`
- `bedrooms`
- `bathrooms`
- `stories`
- `mainroad`
- `guestroom`
- `basement`
- `hotwaterheating`
- `airconditioning`
- `parking`
- `prefarea`
- `furnishingstatus`

---

### 🔹 Machine Learning Technique
- **Type:** Supervised Learning  
- **Algorithm:** Linear Regression  

---

### 🔹 Steps Performed
1. Imported required Python libraries
2. Loaded housing dataset
3. Converted categorical variables into numerical form using label encoding
4. Defined feature variables (X) and target variable (y)
5. Split the dataset into training and testing sets
6. Trained Linear Regression model
7. Predicted house prices
8. Evaluated the model using MAE, MSE, RMSE, and R² score

---

### 🔹 Model Evaluation Metrics
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

### 🔹 Conclusion
The Linear Regression model was able to learn the relationship between house features and prices. The evaluation metrics indicate how accurately the model predicts housing prices.

---

## 📌 Assignment 2: Email Spam Classification

### 🔹 Objective
To classify emails as **Spam** or **Not Spam** using a supervised classification algorithm.

---

### 🔹 Dataset Description
The email dataset consists of:
- `text` → Email content
- `spam` → Target label (0 = Not Spam, 1 = Spam)

Extra columns (`Unnamed`) were removed during preprocessing.

---

### 🔹 Machine Learning Technique
- **Type:** Supervised Learning  
- **Algorithm:** Logistic Regression  

---

### 🔹 Steps Performed
1. Imported necessary libraries
2. Loaded email dataset
3. Removed unnecessary `Unnamed` columns
4. Handled missing (NaN) values
5. Converted email text into numerical form using TF-IDF vectorization
6. Split dataset into training and testing sets
7. Trained Logistic Regression model
8. Evaluated model performance

---

### 🔹 Model Evaluation Metrics
- Accuracy Score
- Confusion Matrix
- Precision, Recall, and F1-Score

---

### 🔹 Conclusion
Logistic Regression effectively classified emails into spam and non-spam categories. Handling missing values and text vectorization played a crucial role in improving model performance.

---

## ✅ Final Outcome
- Successfully implemented **Regression** and **Classification** models
- Understood the importance of data preprocessing
- Learned practical application of supervised machine learning algorithms

---

## 🛠 Tools & Libraries Used
- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF Vectorizer



