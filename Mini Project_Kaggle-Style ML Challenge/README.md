# 🚢 Titanic Survival Prediction – Mini Machine Learning Project

---

## 📌 1. Introduction

The Titanic disaster is one of the most famous shipwrecks in history. 
This project aims to build a Machine Learning model to predict whether a passenger survived or not based on different features such as age, gender, ticket class, and fare.

This is a **Binary Classification Problem** where:

- 0 → Did Not Survive  
- 1 → Survived  

---

## 🎯 2. Problem Statement

To develop a predictive model that determines the survival of passengers on the Titanic using available passenger data.

The objective is to maximize classification accuracy and analyze the important factors influencing survival.

---

## 📂 3. Dataset Description

- Dataset Name: Titanic Dataset (Kaggle)
- url: https://www.kaggle.com/datasets/heptapod/titanic
- Total Records: 891
- Total Features: 12
- Target Variable: Survived
- Problem Type: Classification

### Important Features:

- Pclass → Passenger Class (1, 2, 3)
- Sex → Gender of passenger
- Age → Age of passenger
- SibSp → Number of siblings/spouses aboard
- Parch → Number of parents/children aboard
- Fare → Ticket fare
- Embarked → Port of embarkation

The dataset contains both numerical and categorical features.

---

## 🧹 4. Data Preprocessing

The following preprocessing steps were performed:

- Checked for missing values
- Filled missing values in Age and Embarked
- Dropped unnecessary columns (Name, Ticket, Cabin)
- Converted categorical variables (Sex, Embarked) using One-Hot Encoding
- Split dataset into Training (80%) and Testing (20%)

These steps ensured the dataset was clean and ready for model training.

---

## 📊 5. Exploratory Data Analysis (EDA)

Key observations from EDA:

- Female passengers had a significantly higher survival rate.
- Passengers in 1st class had better survival probability.
- Higher fare passengers were more likely to survive.
- Younger passengers had slightly better survival chances.

Correlation heatmaps and count plots were used to understand feature relationships.

---

## 🤖 6. Model Building

A Random Forest Classifier was used for prediction.

Why Random Forest?

- Handles non-linear relationships
- Reduces overfitting
- Works well with mixed data types
- Provides feature importance analysis

The model was trained using the training dataset.

---

## 📈 7. Model Evaluation

The model was evaluated using:

- Accuracy Score
- F1 Score
- Confusion Matrix

### Example Results:

- Accuracy: 85%
- F1 Score: 0.84

The confusion matrix showed that the model correctly classified most survival cases with minimal errors.

---

## ⭐ 8. Feature Importance

Feature importance analysis revealed:

- Sex was the most important feature.
- Pclass strongly influenced survival.
- Fare and Age had moderate importance.
- SibSp and Parch had lower impact.

This confirms that gender and socio-economic status played a major role in survival.

---

## 💡 9. Insights & Recommendations

- Women and first-class passengers had higher survival rates.
- Social class and economic status significantly influenced survival.
- Machine Learning models can effectively analyze historical data and extract meaningful insights.
- Model performance can be improved further using hyperparameter tuning and advanced boosting algorithms.

---

## 🏁 10. Conclusion

This project successfully developed a machine learning model to predict Titanic passenger survival.

The Random Forest model achieved good accuracy and provided meaningful insights into key survival factors.

The project demonstrates:

- Data preprocessing techniques
- Exploratory Data Analysis
- Model training and evaluation
- Feature importance interpretation

This mini project showcases practical application of Machine Learning in solving real-world problems.

---
