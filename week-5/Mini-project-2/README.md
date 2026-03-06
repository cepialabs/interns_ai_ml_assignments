# Bank Customer Churn Prediction

End-to-end machine learning project for predicting customer churn using the Kaggle `Churn_Modelling.csv` dataset.

## Business Context

Companies want to identify customers likely to leave so they can take retention actions.

## Typical Dataset Columns

- Customer demographics
- Subscription details
- Usage metrics
- Support interactions
- Churn label (Yes/No)

## Expected Outcome

Binary classification model predicting churn probability.

## Project Structure

- `data/` - place `Churn_Modelling.csv` here
- `notebooks/` - optional exploration notebooks
- `src/` - preprocessing, EDA, training, prediction modules
- `models/` - trained models, metrics, plots, and risk scores
- `app/` - optional Streamlit app

## Setup

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
```

## Run Training Pipeline

```bash
python -m src.train
```

This will:
1. Load and preprocess data
2. Create EDA plots
3. Train Logistic Regression and Random Forest
4. Evaluate using Accuracy, Precision, Recall, F1, Confusion Matrix, ROC-AUC
5. Select best model by Recall then ROC-AUC
6. Save model with `joblib`
7. Generate feature importance plot (Random Forest)
8. Generate test-set churn risk scoring output

## Use Prediction Function

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


