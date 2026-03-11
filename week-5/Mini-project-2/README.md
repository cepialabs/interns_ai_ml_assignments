# 🏦 AI-Powered Bank Customer Churn Prediction

An **end-to-end Machine Learning project** that predicts whether a bank customer is likely to **churn (leave the bank)** using customer demographic and financial data.

The system includes:

* Data preprocessing
* Exploratory Data Analysis (EDA)
* Machine learning model training
* Model evaluation
* Risk scoring system
* Interactive **Streamlit dashboard for real-time predictions**

This project demonstrates a **complete ML pipeline from raw dataset to deployment-ready prediction interface**.

---

# 📊 Problem Statement

Customer churn is a major issue in the banking industry.
Identifying customers who are likely to leave allows banks to:

* Improve retention strategies
* Reduce financial loss
* Improve customer satisfaction

This project builds a **predictive system that estimates churn probability and risk level**.

---

# 📂 Dataset

Dataset used: **Churn_Modelling.csv**

The dataset contains customer information such as:

| Feature         | Description                           |
| --------------- | ------------------------------------- |
| CreditScore     | Customer credit score                 |
| Geography       | Customer location                     |
| Gender          | Male / Female                         |
| Age             | Customer age                          |
| Tenure          | Years with bank                       |
| Balance         | Account balance                       |
| NumOfProducts   | Number of bank products               |
| HasCrCard       | Credit card ownership                 |
| IsActiveMember  | Activity status                       |
| EstimatedSalary | Customer salary                       |
| Exited          | Target variable (1 = churn, 0 = stay) |

---

# ⚙️ Machine Learning Pipeline

```
Raw Dataset
     ↓
Data Preprocessing
     ↓
Exploratory Data Analysis
     ↓
Feature Engineering
     ↓
Train/Test Split
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Best Model Selection
     ↓
Risk Score Generation
     ↓
Streamlit Dashboard
```

---

# 🧹 Data Preprocessing

The preprocessing pipeline performs:

* Column normalization
* Removal of unnecessary columns
* Categorical encoding
* Feature-target separation

Dropped columns:

```
RowNumber
CustomerId
Surname
```

Gender encoding:

```
Female → 0
Male → 1
```

---

# 📈 Exploratory Data Analysis

EDA helps understand patterns influencing customer churn.

Generated visualizations include:

* Churn Distribution
* Age vs Churn
* Geography vs Churn
* Correlation Heatmap

These insights help identify **important factors affecting churn**.

---

# 🤖 Models Used

Two machine learning models were trained:

| Model               | Description    |
| ------------------- | -------------- |
| Logistic Regression | Baseline model |
| Random Forest       | Ensemble model |

The **best model is selected using:**

* Recall score
* ROC-AUC score

---

# 📊 Model Evaluation Metrics

Model performance was evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

Evaluation plots generated:

* Confusion Matrix
* ROC Curve
* Feature Importance

Saved inside:

```
models/plots/
```

---

# 🎯 Feature Importance

The Random Forest model identifies the most influential features:

Top important features:

* Age
* Balance
* Estimated Salary
* Credit Score
* Number of Products
* Tenure

These features strongly impact customer churn behavior.

---

# ⚠️ Risk Scoring System

Instead of only predicting churn, the system also generates a **risk score**.

```
Risk Score = churn_probability × 100
```

Risk categories:

| Score Range | Risk Level     |
| ----------- | -------------- |
| 0 – 30      | 🟢 Low Risk    |
| 31 – 70     | 🟠 Medium Risk |
| 71 – 100    | 🔴 High Risk   |

This helps banks **prioritize high-risk customers**.

---

# 🖥️ Streamlit Prediction Dashboard

An interactive **Streamlit dashboard** allows users to:

* Enter customer details
* Predict churn probability
* View churn risk score
* View risk category
* Download prediction report

Run the dashboard:

```bash
streamlit run app/streamlit_app.py
```

---

# 📂 Project Structure

```
Mini-project-2
│
├── app
│   └── streamlit_app.py
│
├── data
│   └── Churn_Modelling.csv
│
├── models
│   ├── plots
│   │   ├── age_vs_churn.png
│   │   ├── churn_distribution.png
│   │   ├── correlation_heatmap.png
│   │   ├── geography_vs_churn.png
│   │   ├── confusion_matrix.png
│   │   ├── rf_feature_importance.png
│   │   └── roc_curve.png
│   │
│   ├── best_model.joblib
│   ├── random_forest_model.joblib
│   ├── model_metrics.csv
│   └── test_risk_scores.csv
│
├── src
│   ├── config.py
│   ├── data_preprocessing.py
│   ├── eda.py
│   ├── train.py
│   ├── predict.py
│   └── risk.py
│
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone <repository-url>
cd churn-prediction
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment (Windows):

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Training Pipeline

Run the complete ML workflow:

```bash
python -m src.train
```
# ▶️ Run App UI

Run the complete UI of the project:

```bash
cd app
```
then run

```bash
python -m streamlit run streamlit_app
```

This will:

1. Load dataset
2. Perform preprocessing
3. Generate EDA plots
4. Train ML models
5. Evaluate models
6. Select best model
7. Save trained model
8. Generate churn risk scores

---

# 🔮 Example Prediction

```python
from src.predict import predict_customer_churn

customer = {
    "CreditScore": 650,
    "Geography": "France",
    "Gender": "Female",
    "Age": 42,
    "Tenure": 4,
    "Balance": 125000.0,
    "NumOfProducts": 2,
    "HasCrCard": 1,
    "IsActiveMember": 1,
    "EstimatedSalary": 95000.0,
}

result = predict_customer_churn(customer)
print(result)
```

Example output:

```
{
 'churn_probability': 0.62,
 'risk_score': 62,
 'risk_category': 'Medium Risk'
}
```

---

# 📦 Requirements

Main libraries used:

* pandas
* numpy
* matplotlib
* seaborn
* scikit-learn
* joblib
* streamlit
* plotly

Install using:

```
pip install -r requirements.txt
```

---

# 🧠 Key Learnings

This project demonstrates:

* End-to-end ML pipeline development
* Data preprocessing techniques
* Exploratory data analysis
* Machine learning model training
* Model evaluation methods
* Feature importance interpretation
* Risk scoring system design
* Deployment using Streamlit

---

# 👨‍💻 Author

**Krushna**
**Sanket**
**Madhav**


Machine Learning & Data Science Enthusiast
