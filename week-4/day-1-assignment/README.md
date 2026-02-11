🏠 House Price Prediction & Feature Engineering
Week 4 – Day 1 Assignment
Date: 10 February 2026
Name: Seerat Metkari
📌 Objective

The objective of this assignment is to:

Perform feature engineering on the House Price dataset

Create new meaningful features

Encode categorical variables

Train regression models

Analyze feature importance

📂 Dataset Description

The dataset contains the following columns:

price – House price (Target variable)

area – Area of the house

bedrooms – Number of bedrooms

bathrooms – Number of bathrooms

stories – Number of floors

mainroad – Whether house is connected to main road (yes/no)

guestroom – Guest room availability (yes/no)

basement – Basement availability (yes/no)

hotwaterheating – Hot water heating system (yes/no)

airconditioning – Air conditioning availability (yes/no)

parking – Number of parking spaces

prefarea – Preferred area (yes/no)

furnishingstatus – Furnishing type (furnished/semi-furnished/unfurnished)

🔎 Steps Performed
1️⃣ Data Loading

Imported required libraries (Pandas, NumPy, Matplotlib, Seaborn)

Loaded dataset using pd.read_csv()

2️⃣ Data Understanding

Checked data types using df.info()

Checked summary statistics using df.describe()

Checked missing values using df.isnull().sum()

3️⃣ Feature Engineering
✔ Created New Feature:

Price per Square Foot

𝑝
𝑟
𝑖
𝑐
𝑒
_
𝑝
𝑒
𝑟
_
𝑠
𝑞
𝑓
𝑡
=
𝑝
𝑟
𝑖
𝑐
𝑒
𝑎
𝑟
𝑒
𝑎
price_per_sqft=
area
price
	​


This helps understand the price relative to property size.

4️⃣ Encoding Categorical Variables
✔ Converted Yes/No columns to 1/0:

mainroad

guestroom

basement

hotwaterheating

airconditioning

prefarea

✔ One-Hot Encoded:

furnishingstatus

This converted categorical values into numerical format suitable for machine learning models.

5️⃣ Splitting Data

Separated features (X) and target variable (y)

Used train_test_split() with 80% training and 20% testing data

6️⃣ Model Training
✔ Linear Regression Model

Used to understand relationship between features and house price.

✔ Random Forest Regressor

Used to analyze feature importance more effectively.

7️⃣ Feature Importance Analysis

Feature importance was extracted from:

Linear Regression (coefficients)

Random Forest (feature_importances_)

Most important features typically include:

Area

Bathrooms

Air conditioning

Preferred area

Parking

📊 Conclusion

Area has the strongest impact on house price.

Houses in preferred areas and with air conditioning tend to have higher prices.

Feature engineering (price per sqft) improves understanding of price structure.

Tree-based models provide better feature importance interpretation compared to linear regression.

🛠 Tools Used

Python

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn
