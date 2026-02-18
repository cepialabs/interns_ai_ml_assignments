# Heart Disease Prediction using Machine Learning

## 📌 Project Overview
This project aims to predict the presence of heart disease using Machine Learning techniques.  
The model analyzes various medical attributes and classifies whether a patient has heart disease or not.

---

## 🎯 Objective
- Perform data preprocessing and cleaning
- Conduct Exploratory Data Analysis (EDA)
- Build classification models
- Evaluate model performance
- Generate medical insights from feature importance

---

## 📊 Dataset Information
The dataset contains patient medical attributes such as:

- Age
- Sex
- Chest Pain Type (cp)
- Resting Blood Pressure (trestbps)
- Cholesterol (chol)
- Fasting Blood Sugar (fbs)
- Resting ECG (restecg)
- Maximum Heart Rate (thalach)
- Exercise Induced Angina (exang)
- ST Depression (oldpeak)
- Slope
- Number of Major Vessels (ca)
- Thalassemia (thal)
- **URL:** https://www.kaggle.com/datasets/rishidamarla/heart-disease-prediction

### 🎯 Target Variable
- 0 → No Heart Disease
- 1 → Heart Disease Present

---

## 🛠 Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## 🔎 Project Workflow

### 1️⃣ Data Preprocessing
- Checked missing values
- Handled missing data
- Scaled numerical features using StandardScaler
- Split dataset (80% Training, 20% Testing)

### 2️⃣ Exploratory Data Analysis
- Class distribution visualization
- Correlation heatmap
- Boxplots and histograms
- Feature relationship analysis

### 3️⃣ Model Building
- Logistic Regression (Baseline Model)
- Random Forest Classifier (Ensemble Model)

### 4️⃣ Model Evaluation
- Accuracy Score
- F1 Score
- Confusion Matrix
- Cross-validation

---

## 📈 Results

| Model | Accuracy |
|--------|----------|
| Logistic Regression | ~82–85% |
| Random Forest | ~85–90% |

Random Forest performed better and showed strong feature importance.

---

## 🔥 Key Insights
- Chest pain type significantly affects prediction.
- High cholesterol levels increase heart disease risk.
- Ensemble models improve classification performance.
- The model can assist in early detection of heart disease.

---

## 🚀 Future Improvements
- Hyperparameter tuning
- XGBoost implementation
- Deployment using Flask/Streamlit
- Integration with healthcare systems

---

## 📌 Conclusion
This project demonstrates an end-to-end Machine Learning pipeline for heart disease prediction.  
The model can support medical professionals in early risk assessment.

---
