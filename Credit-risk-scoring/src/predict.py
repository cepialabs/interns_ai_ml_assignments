import joblib

def predict_risk(input_data):

    model = joblib.load("logs/credit_risk_model.pkl")

    prediction = model.predict([input_data])

    if prediction[0] == 1:
        return "High Risk (Likely to Default)"
    else:
        return "Low Risk (Safe Applicant)"