from pathlib import Path
import sys
import streamlit as st
import joblib
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# PROJECT ROOT
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.predict import predict_customer_churn
from src.config import BEST_MODEL_PATH

# PAGE CONFIG
st.set_page_config(
    page_title="AI Churn Intelligence",
    page_icon="🏦",
    layout="wide"
)

# PREMIUM DARK THEME
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}

.block-container {
    padding-top: 2rem;
}

/* Headings */
h1, h2, h3 {
    color: #00C6FF;
}

/* Metric Cards */
[data-testid="stMetric"] {
    background: linear-gradient(135deg, #1f2937, #111827);
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #00C6FF33;
    box-shadow: 0px 0px 15px rgba(0,198,255,0.15);
}

[data-testid="stMetricLabel"] {
    color: #9CA3AF !important;
    font-size: 16px;
}

[data-testid="stMetricValue"] {
    color: #00C6FF !important;
    font-size: 28px;
    font-weight: bold;
}

/* Buttons */
.stButton>button {
    background-color: #00C6FF;
    color: black;
    font-weight: bold;
    border-radius: 10px;
}

.stDownloadButton>button {
    background-color: #111827;
    color: #00C6FF;
    border: 1px solid #00C6FF;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

#  HEADER 
st.markdown("""
<h1 style='text-align:center;'>🏦 AI-Powered Churn Intelligence Dashboard</h1>
<p style='text-align:center;'>Fintech Risk Prediction System</p>
""", unsafe_allow_html=True)

st.divider()

artifact = joblib.load(BEST_MODEL_PATH)
model_name = artifact["model_name"]

#  LAYOUT 
left, right = st.columns([1, 1], gap="large")

#  LEFT SIDE 
with left:
    st.subheader("📋 Customer Information")

    with st.form("churn_form"):
        credit_score = st.number_input("Credit Score", 300, 900, 650)
        geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
        gender = st.selectbox("Gender", ["Female", "Male"])
        age = st.number_input("Age", 18, 100, 40)
        tenure = st.number_input("Tenure", 0, 10, 5)
        balance = st.number_input("Balance", 0.0, 250000.0, 50000.0)
        num_products = st.number_input("Number of Products", 1, 4, 2)
        has_card = st.selectbox("Has Credit Card", [0, 1])
        is_active = st.selectbox("Is Active Member", [0, 1])
        est_salary = st.number_input("Estimated Salary", 0.0, 200000.0, 60000.0)

        submitted = st.form_submit_button("🚀 Predict Risk")

# RIGHT SIDE
with right:
    st.subheader("📊 Prediction Results")

    if submitted:
        customer = {
            "CreditScore": credit_score,
            "Geography": geography,
            "Gender": gender,
            "Age": age,
            "Tenure": tenure,
            "Balance": balance,
            "NumOfProducts": num_products,
            "HasCrCard": has_card,
            "IsActiveMember": is_active,
            "EstimatedSalary": est_salary,
        }

        result = predict_customer_churn(customer)

        probability = result["churn_probability"]
        risk_score = result["risk_score"]
        risk_category = result["risk_category"]

        # METRICS 
        m1, m2 = st.columns(2)
        m1.metric("Churn Probability", f"{probability:.2%}")
        m2.metric("Risk Score", risk_score)

        #  RISK GAUGE 
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=risk_score,
            title={'text': "Risk Level"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "#00C6FF"},
                'steps': [
                    {'range': [0, 30], 'color': "green"},
                    {'range': [30, 70], 'color': "orange"},
                    {'range': [70, 100], 'color': "red"},
                ],
            }
        ))

        fig.update_layout(
            paper_bgcolor="#0e1117",
            font_color="white",
            height=350,
            margin=dict(l=20, r=20, t=40, b=20)
        )

        st.plotly_chart(fig, use_container_width=True)

        #  RISK BADGE 
        if risk_score <= 30:
            st.markdown("<h3 style='color:#22c55e;'>🟢 LOW RISK</h3>", unsafe_allow_html=True)
        elif risk_score <= 70:
            st.markdown("<h3 style='color:#f59e0b;'>🟠 MEDIUM RISK</h3>", unsafe_allow_html=True)
        else:
            st.markdown("<h3 style='color:#ef4444;'>🔴 HIGH RISK</h3>", unsafe_allow_html=True)

        st.info(f"🤖 Model Used: {model_name}")

        #  DOWNLOAD REPORT 
        report_df = pd.DataFrame([{
            "CreditScore": credit_score,
            "Geography": geography,
            "Gender": gender,
            "Age": age,
            "Tenure": tenure,
            "Balance": balance,
            "NumOfProducts": num_products,
            "HasCrCard": has_card,
            "IsActiveMember": is_active,
            "EstimatedSalary": est_salary,
            "ChurnProbability": probability,
            "RiskScore": risk_score,
            "RiskCategory": risk_category
        }])

        csv = report_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="⬇ Download Prediction Report",
            data=csv,
            file_name="churn_prediction_report.csv",
            mime="text/csv"
        )

    else:
        st.info("Fill details and click Predict.")

st.divider()