🏠 House Price Prediction using Machine Learning
📅 Week 4 – Day 3 Assignment
📆 Date: 12 February 2026

📌 Objective

The objective of this assignment is to:

Train a Random Forest Regressor on the Housing dataset

Compare its performance with Linear Regression

Evaluate models using R² Score

Visualize Feature Importance

(Optional) Compare with XGBoost Model

📂 Dataset Description

The dataset contains housing-related features used to predict house prices.

📊 Features Used:

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

🎯 Target Variable:

price

🛠️ Technologies Used

Python

Pandas

NumPy

Matplotlib

Scikit-learn

XGBoost (Optional)

🔄 Steps Performed
1️⃣ Data Loading

Loaded dataset using Pandas.

2️⃣ Data Preprocessing

Encoded categorical variables using LabelEncoder.

Checked for missing values.

Defined features (X) and target (y).

3️⃣ Train-Test Split

Split data into:

80% Training

20% Testing

4️⃣ Model Training
✔ Linear Regression (Baseline Model)

Trained using LinearRegression()

Calculated R² Score

✔ Random Forest Regressor

Trained using RandomForestRegressor

Compared R² score with Linear Regression

✔ (Optional) XGBoost Regressor

Trained using XGBRegressor

Compared performance

📈 Model Evaluation
📊 Evaluation Metric Used:

R² Score (Coefficient of Determination)

R² Score Interpretation:

Closer to 1 → Better model performance

Closer to 0 → Poor performance

🌟 Feature Importance

Extracted feature importance from Random Forest model

Visualized using Matplotlib bar chart

Identified most important factors affecting house price

Example important features:

Area

Bathrooms

Air Conditioning

Parking

Stories

📊 Results Summary
Model	R² Score
Linear Regression	Moderate
Random Forest	Higher
XGBoost (Optional)	Highest

👉 Random Forest performed better than Linear Regression.

📷 Output Visualizations

Feature Importance Graph

Model Comparison using R² Score

🎯 Conclusion

Random Forest model improved prediction accuracy compared to Linear Regression.

Feature importance analysis helped identify key factors influencing house prices.

Ensemble models like Random Forest and XGBoost provide better performance for regression problems.

🚀 Future Improvements

Hyperparameter tuning

Cross-validation

Feature engineering

Outlier removal

Try other ensemble methods

📌 Repository Structure
📂 House-Price-Prediction
 ┣ 📜 housing.csv
 ┣ 📜 model_training.ipynb
 ┣ 📜 README.md


✨ This assignment demonstrates understanding of:

Regression models

Model comparison

Feature importance visualization
