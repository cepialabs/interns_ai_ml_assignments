📘 Week 4 – Day 2 Assignment

Date: 11 February 2026
Name: Seerat Metkari

📊 Assignment Title:

Scaling Numerical Features and Observing Model Performance

🎯 Objective

Apply feature scaling on numerical features.

Retrain regression and classification models.

Compare model performance before and after scaling.

Datasets used:

🏠 House Prices Dataset (Regression)

📧 Spam Emails Dataset (Classification)

🏠 Part 1: House Price Prediction (Regression)
📂 Dataset Columns:

price (Target variable)

area

bedrooms

bathrooms

stories

mainroad

guestroom

basement

hotwaterheating

airconditioning

parking

prefarea

furnishingstatus

⚙️ Steps Performed:

Loaded dataset using pandas.

Converted categorical columns:

yes/no → 1/0

furnishingstatus → Label Encoding

Split dataset into training and testing sets (80-20).

Trained Linear Regression model without scaling.

Applied StandardScaler on numerical features.

Retrained Linear Regression model with scaling.

Compared R² Score and MSE.

📈 Observations:

Linear Regression performance did not change significantly after scaling.

Scaling is not very sensitive for basic linear regression.

However, scaling is important for distance-based and regularized models.

📧 Part 2: Spam Email Classification
📂 Dataset Columns:

text

spam (1 = Spam, 0 = Not Spam)

⚙️ Steps Performed:

Loaded spam dataset.

Converted text data into numerical form using TF-IDF Vectorization.

Split dataset into training and testing sets.

Trained KNN classifier without scaling.

Applied StandardScaler (with_mean=False for sparse matrix).

Retrained KNN model after scaling.

Compared Accuracy scores.

📈 Observations:

KNN accuracy improved after scaling.

Scaling is very important for distance-based algorithms like KNN.

Proper feature scaling ensures better distance calculation.

📊 Overall Conclusion

Feature scaling standardizes numerical data.

Linear Regression is less affected by scaling.

Distance-based models like KNN perform better after scaling.

Scaling is an important preprocessing step in Machine Learning.

