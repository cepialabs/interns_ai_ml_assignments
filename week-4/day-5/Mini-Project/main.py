
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import pickle
from PIL import Image

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="SkyGuard | AQI Predictor",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CUSTOM CSS FOR STYLING ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #007BFF;
        color: white;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #0056b3;
        border: none;
        color: white;
    }
    .prediction-card {
        padding: 20px;
        border-radius: 15px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOAD ASSETS ---
@st.cache_resource
def load_model():
    # Try Joblib first (Best for SKlearn), then Pickle
    try:
        model = joblib.load('rf.pkl')
        cols = joblib.load('columns.pkl')
        return model, cols
    except:
        try:
            with open('rf.pkl', 'rb') as f:
                model = pickle.load(f)
            with open('columns.pkl', 'rb') as f:
                cols = pickle.load(f)
            return model, cols
        except Exception as e:
            st.error(f"Error loading files: {e}")
            return None, None

model, model_columns = load_model()

# --- SIDEBAR INPUTS ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/1684/1684375.png", width=100)
st.sidebar.title("Configuration")

st.sidebar.subheader("📍 Location Details")
city = st.sidebar.selectbox("Select City", ['Delhi', 'Gurugram', 'Faridabad', 'Noida', 'Ghaziabad'])
season = st.sidebar.selectbox("Current Season", ['winter', 'summer', 'monsoon', 'post_monsoon'])
year = st.sidebar.slider("Year", 2024, 2030, 2025)

st.sidebar.subheader("🌡️ Weather Conditions")
temp = st.sidebar.number_input("Temp (°C)", value=25.0)
hum = st.sidebar.number_input("Humidity (%)", value=50.0)
wind = st.sidebar.number_input("Wind Speed (km/h)", value=10.0)
vis = st.sidebar.number_input("Visibility (km)", value=2.0)

# --- MAIN CONTENT ---
st.title("☁️ SkyGuard: AI-Powered AQI Predictor")
st.markdown("Enter pollutant levels to get an instant Air Quality Index prediction.")

# Pollutant Inputs in Columns
col1, col2, col3 = st.columns(3)

with col1:
    pm25 = st.number_input("PM2.5 Level", value=80.0, help="Particulate Matter 2.5")
    pm10 = st.number_input("PM10 Level", value=120.0)

with col2:
    no2 = st.number_input("NO2 Level", value=30.0)
    so2 = st.number_input("SO2 Level", value=12.0)

with col3:
    co = st.number_input("CO Level", value=1.5)
    o3 = st.number_input("O3 Level", value=25.0)

st.divider()

# --- PREDICTION LOGIC ---
if st.button("Analyze Air Quality"):
    if model is not None:
        # Create Input DataFrame
        input_data = pd.DataFrame(columns=model_columns)
        input_data.loc[0] = 0 # Initialize with zeros
        
        # Mapping numerical values
        features = {
            'year': year, 'pm25': pm25, 'pm10': pm10, 'no2': no2,
            'so2': so2, 'co': co, 'o3': o3, 'temperature': temp,
            'humidity': hum, 'wind_speed': wind, 'visibility': vis
        }
        
        for key, val in features.items():
            if key in input_data.columns:
                input_data[key] = val
        
        # Handle Categorical Encoding (One-Hot)
        city_col = f"city_{city}"
        season_col = f"season_{season}"
        
        if city_col in input_data.columns: input_data[city_col] = 1
        if season_col in input_data.columns: input_data[season_col] = 1

        # Prediction
        prediction = model.predict(input_data)[0]
        aqi_val = round(prediction, 2)

        # Result Display with Color Coding
        res_col1, res_col2 = st.columns([1, 2])
        
        with res_col1:
            st.metric(label="Predicted AQI", value=aqi_val)
        
        with res_col2:
            if aqi_val <= 50:
                st.success("### Health Status: Good 😊")
                st.write("Air quality is satisfactory, and air pollution poses little or no risk.")
            elif aqi_val <= 100:
                st.info("### Health Status: Satisfactory 🙂")
                st.write("Air quality is acceptable; however, there may be a risk for some people.")
            elif aqi_val <= 200:
                st.warning("### Health Status: Moderate 😐")
                st.write("Members of sensitive groups may experience health effects.")
            elif aqi_val <= 300:
                st.error("### Health Status: Poor 😷")
                st.write("Everyone may begin to experience health effects; wear a mask.")
            else:
                st.error("### Health Status: SEVERE 🚨")
                st.write("Health warnings of emergency conditions. The entire population is more likely to be affected.")
    else:
        st.error("Model not found. Please upload 'rf.pkl' and 'columns.pkl'.")

st.markdown("---")
st.caption("Data Source: Aqiprediction Dataset | Model: Random Forest Regressor")
