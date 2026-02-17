# 📊 Social Media Usage & Work Productivity – Machine Learning Project

## 📌 Objective
This project applies advanced machine learning techniques to analyze how social media usage, lifestyle habits, and device behavior affect **work productivity**.  
The goal is to predict **Work_Productivity_Score** and generate actionable insights.

---

## 📂 Dataset Description
The dataset contains user-level behavioral and productivity data.

### Columns
- User_ID  
- Age  
- Gender  
- Occupation  
- Device_Type  
- Daily_Phone_Hours  
- Social_Media_Hours  
- Work_Productivity_Score *(Target)*  
- Sleep_Hours  
- Stress_Level  
- App_Usage_Count  
- Caffeine_Intake_Cups  
- Weekend_Screen_Time_Hours  

---

## 🔍 Problem Type
- **Supervised Learning**
- **Regression Task**

---

## ⚙️ Project Workflow

### 1. Data Understanding
- Exploratory data analysis
- Missing value checks
- Target distribution analysis

### 2. Feature Engineering
- `Total_Screen_Time`
- `Social_Media_Ratio`
- `Caffeine_Stress_Index`

### 3. Data Preprocessing
- One-Hot Encoding for categorical features
- Standard Scaling for numerical features
- Train-test split (80/20)

### 4. Model Building
- Baseline: Linear Regression
- Advanced: Random Forest Regressor

### 5. Evaluation
- RMSE
- R² Score
- 5-Fold Cross-Validation

---

## 📈 Results Summary
| Model | Performance |
|------|------------|
| Linear Regression | Baseline |
| Random Forest | Best (Lower RMSE, Higher R²) |

---

## 🔑 Key Insights
- High social media usage negatively impacts productivity
- Sleep duration is a strong positive contributor
- Stress and caffeine interaction reduces productivity
- Excessive weekend screen time affects weekday performance

---

## 💡 Recommendations
- Promote social media moderation
- Encourage healthy sleep habits
- Manage stress-related caffeine intake
- Implement digital wellness strategies

---

## 🚀 Future Enhancements
- XGBoost / LightGBM
- SHAP explainability
- Productivity classification model
- Longitudinal data analysis

---

## 📁 Project Structure
```
├── data/
│   └── social_media_productivity.csv
├── notebooks/
│   └── analysis.ipynb
├── README.md
```

---

## 🏁 Conclusion
This project demonstrates how machine learning can transform behavioral data into meaningful productivity insights, supporting smarter digital and workplace decisions.
