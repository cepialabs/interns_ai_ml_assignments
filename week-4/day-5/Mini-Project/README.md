# ☁️ SkyGuard: AI-Powered AQI Predictor
**My First Internship Project** 🚀

SkyGuard is a Machine Learning-based web application that predicts the Air Quality Index (AQI) based on various pollutants and environmental factors. This project was developed during my internship to provide real-time air quality insights.

## 📊 Project Overview
Predicting AQI is a complex task involving multiple variables. This project focuses on analyzing pollutants like PM2.5, PM10, NO2, and SO2 along with weather conditions to provide an accurate AQI score.

## 🛠️ Technical Stack
- **Languages:** Python 🐍
- **Libraries:** Scikit-Learn, Pandas, NumPy, Seaborn, Matplotlib
- **Model:** Random Forest Regressor 🌲
- **Deployment:** Streamlit 🎈

## 📈 Statistical Analysis & Preprocessing
To ensure high model accuracy, I implemented the following statistical techniques:

1. **Outlier Removal:** 🧹
   - Used the **Interquartile Range (IQR) Method** to detect and remove extreme values (outliers) in pollutant concentrations that could skew the model's performance.
2. **Correlation Analysis:** 🔗
   - Performed correlation analysis to identify the most influential features. 
   - Utilized **Heatmaps** and **Subplots** to visualize the relationship between pollutants like PM2.5 and the target AQI.
3. **Data Visualization:** 📊
   - Created multiple subplots (Histograms, Boxplots, and Scatter plots) to understand data distribution and feature variance.

## 🚀 Features
- **Real-time Prediction:** Input pollutant levels and get instant AQI results.
- **Categorical Handling:** One-Hot Encoding for Cities and Seasons.
- **Modern UI:** Interactive and user-friendly interface built with Streamlit.
- **Health Recommendations:** Provides safety advice based on the predicted AQI level.

## 📁 Project Structure
```text
├── app.py              # Streamlit Web App
├── rf.pkl              # Trained Random Forest Model
├── columns.pkl         # Feature column list for consistency
├── Aqiprediction.csv   # Dataset used for training
├── requirements.txt    # List of dependencies
└── README.md           # Project Documentation