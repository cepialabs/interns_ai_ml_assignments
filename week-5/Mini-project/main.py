import streamlit as st
import pandas as pd
import numpy as np
import joblib

# 1. Page Configuration
st.set_page_config(page_title="Telecom Customer Retention AI", layout="wide")

# Custom Styling for a Professional UI
st.markdown("""
    <style>
    .stAlert { border-radius: 8px; }
    .stButton>button { width: 100%; font-weight: bold; height: 3em; border-radius: 5px; }
    .main { background-color: #f8f9fa; }
    </style>
    """, unsafe_allow_html=True)

@st.cache_resource
def load_assets():
    # Ensure these files are present in your directory
    model = joblib.load('xgb.pkl')
    model_columns = joblib.load('columns (1).pkl')
    return model, model_columns

model, model_columns = load_assets()

# Header Section
st.title("📡 Enterprise Customer Churn Prediction Dashboard")
st.markdown("""
    This AI-driven analytics tool utilizes high-precision XGBoost modeling to identify at-risk customers 
    based on behavioral, financial, and service-based feature importance.
""")

# 2. Input Form
with st.form("retention_form"):
    st.subheader("📊 Customer Demographic & Service Profile")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("Demographics")
        age = st.number_input("Age (Years)", 18, 100, 30)
        tenure = st.slider("Customer Tenure (Months)", 1, 72, 12)
        referrals = st.number_input("Number of Referrals", 0, 20, 0)
        dependents = st.number_input("Number of Dependents", 0, 10, 0)
        married = st.selectbox("Marital Status", ["No", "Yes"])
        paperless = st.selectbox("Paperless Billing", ["Yes", "No"])

    with col2:
        st.info("Subscription Details")
        contract = st.selectbox("Contractual Agreement", ["Month-to-Month", "One Year", "Two Year"])
        internet = st.selectbox("Broadband Infrastructure", ["Fiber Optic", "DSL", "No Internet"])
        online_sec = st.selectbox("Cybersecurity Package", ["No", "Yes", "No Internet"])
        tech_supp = st.selectbox("Premium Technical Support", ["No", "Yes", "No Internet"])
        unlimited = st.selectbox("Unlimited Data Plan", ["Yes", "No"])
        streaming_tv = st.selectbox("IPTV/Streaming Services", ["No", "Yes", "No Internet"])
        avg_gb = st.number_input("Avg Monthly Data Consumption (GB)", 0, 500, 25)

    with col3:
        st.info("Financial Performance Indicators")
        monthly_charge = st.number_input("Current Monthly Fee ($)", 0.0, 200.0, 65.0)
        total_extra_data = st.number_input("Overage Data Charges ($)", 0.0, 500.0, 0.0)
        total_long_distance = st.number_input("Long Distance Fees ($)", 0.0, 2000.0, 15.0)
        total_refunds = st.number_input("Historical Refund Amount ($)", 0.0, 100.0, 0.0)
        total_rev = st.number_input("Life-Time Value (Total Revenue) ($)", 0.0, 15000.0, 800.0)
        offer = st.selectbox("Marketing Campaign (Offer)", ["None", "Offer A", "Offer B", "Offer C", "Offer D", "Offer E"])

    submit = st.form_submit_button("Generate Predictive Insight")

# 3. Analytics & Prediction Logic
if submit:
    # Initialize Input Dataframe
    input_df = pd.DataFrame(columns=model_columns)
    input_df.loc[0] = 0

    # Data Transformation (Numeric & Logarithmic)
    mapping = {
        'Age': age, 'Number of Dependents': dependents, 'Number of Referrals': referrals,
        'Tenure in Months': tenure, 'Avg Monthly GB Download': avg_gb, 
        'Monthly Charge': monthly_charge, 'Total Extra Data Charges': total_extra_data,
        'Total Long Distance Charges': total_long_distance, 'Total Revenue': total_rev,
        'Total Refunds': total_refunds
    }
    
    for key, val in mapping.items():
        if key in model_columns: input_df[key] = val
        log_key = f"{key}_log"
        if log_key in model_columns: input_df[log_key] = np.log1p(val)

    # Categorical Feature Alignment
    if married == "Yes": input_df['Married_Yes'] = 1
    if paperless == "Yes": input_df['Paperless Billing_Yes'] = 1
    if unlimited == "Yes": input_df['Unlimited Data_Yes'] = 1
    if streaming_tv == "Yes": input_df['Streaming TV_Yes'] = 1
    
    # Dynamic Mapping for Contract, Internet, and Offers
    if f"Contract_{contract}" in model_columns: input_df[f"Contract_{contract}"] = 1
    if f"Internet Type_{internet}" in model_columns: input_df[f"Internet Type_{internet}"] = 1
    if f"Online Security_{online_sec}" in model_columns: input_df[f"Online Security_{online_sec}"] = 1
    if f"Premium Tech Support_{tech_supp}" in model_columns: input_df[f"Premium Tech Support_{tech_supp}"] = 1
    if f"Offer_{offer}" in model_columns: input_df[f"Offer_{offer}"] = 1

    # Execute Model
    probs = model.predict_proba(input_df)[0]
    churn_prob = probs[1]

    # Result Visualization Section
    st.divider()
    res_col1, res_col2 = st.columns([2, 1])

    with res_col1:
        if churn_prob > 0.45:
            st.error(f"### 🚩 CHURN WARNING: {churn_prob*100:.2f}% Probability")
            st.markdown("#### **Primary Attrition Risk Factors:**")
            if contract == "Month-to-Month":
                st.write("- **Contract Stability:** Month-to-Month contracts exhibit 3x higher churn rates.")
            if monthly_charge > 75:
                st.write("- **Pricing Pressure:** Monthly fees exceed optimal retention threshold.")
            if tenure < 6:
                st.write("- **Customer Lifecycle:** High vulnerability detected in early-stage tenure.")
            st.warning("**Recommendation:** Deploy targeted retention offers or loyalty discounts immediately.")
        else:
            st.success(f"### ✅ LOW ATTRITION RISK: {churn_prob*100:.2f}% Probability")
            st.markdown("#### **Engagement Insights:**")
            st.write("The customer demonstrates high brand loyalty. Focus on upselling premium value-added services.")

    with res_col2:
        st.markdown("### Risk Analytics Index")
        st.metric("Churn Risk Probability", f"{churn_prob*100:.1f}%")
        st.progress(float(churn_prob))
        
        # Color-coded status message
        if churn_prob > 0.7: status = "CRITICAL RISK"
        elif churn_prob > 0.45: status = "MODERATE RISK"
        else: status = "HEALTHY / LOYAL"
        st.markdown(f"**Classification:** `{status}`")

# Sidebar - Model Intelligence
st.sidebar.markdown("## Intelligence Overview")
st.sidebar.write("""
**Methodology:**
This system uses a Gradient Boosted Decision Tree (XGBoost) model optimized via p-value significance testing.
""")
st.sidebar.divider()
st.sidebar.caption("v2.4 - Enterprise Edition")