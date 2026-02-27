# Telecom Customer Churn Prediction

This project focuses on predicting customer churn for a telecommunications company. By analyzing demographic and service usage data, we build a machine learning model to identify customers likely to leave, enabling proactive retention strategies.

## 📁 Project Structure

* **`churnprediction_Miniproject (2).ipynb`**: The main Jupyter notebook containing data exploration, preprocessing, model training (XGBoost), and evaluation.
* **`telecom_customer_churn.csv`**: The dataset containing 7,043 customer records with 38 features, including demographics, account information, and usage metrics.
* **Streamlit App**: The expected deployment interface to interact with the model.

## 📊 Dataset Description

The dataset includes the following key features:
* **Demographics**: Gender, Age, Married, Dependents.
* **Account Info**: Tenure in Months, Contract, Payment Method, Monthly/Total Charges.
* **Services**: Phone Service, Internet Type, Device Protection, Streaming TV/Movies.
* **Target Variable**: **Customer Status** (Stayed, Churned, Joined).

## 🛠️ Methodology

1.  **Data Inspection**: Performed initial checks on data types, missing values, and data distribution.
2.  **Preprocessing**: Categorical variables were encoded, and numerical features were scaled.
3.  **Modeling**: An XGBoost model was trained to classify customer status.
4.  **Deployment**: The trained model was saved for integration into a Streamlit application.

## 🚀 Running the Project

To run the Streamlit application and generate predictions, use the following command:

```bash
uv run streamlit run main.py