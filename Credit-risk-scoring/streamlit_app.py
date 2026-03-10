import streamlit as st
import joblib
import pandas as pd
from src.data_loader import load_data
from sklearn.preprocessing import LabelEncoder

# ----------------------------------
# Page Title
# ----------------------------------
st.title("📊 Employee Loan Risk Prediction System")

# ----------------------------------
# Load Trained Model
# ----------------------------------
model = joblib.load("logs/credit_risk_model.pkl")

# ----------------------------------
# Load Dataset (Same way as training)
# ----------------------------------
df = load_data("data/credit_risk_scoring_dataset.csv")

# ----------------------------------
# Encode categorical columns
# (Same logic used in model training)
# ----------------------------------
for col in df.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

# ----------------------------------
# Employee ID Input
# ----------------------------------
employee_id = st.number_input("Enter Employee ID", min_value=1000, step=1)

# ----------------------------------
# Prediction Button
# ----------------------------------
if st.button("Predict Risk"):

    employee = df[df["Employee_ID"] == employee_id]

    if employee.empty:
        st.error("❌ Employee ID Not Found!")
    else:
        # Remove ID & Target column
        X = employee.drop(["Default", "Employee_ID"], axis=1)

        prediction = model.predict(X)[0]
        probability = model.predict_proba(X)[0][1] * 100

        st.subheader("Prediction Result")

        if prediction == 1:
            st.error(f"HIGH RISK ❌")
            st.write(f"Risk Probability: {probability:.2f}%")
        else:
            st.success(f"LOW RISK ✅")
            st.write(f"Risk Probability: {probability:.2f}%")