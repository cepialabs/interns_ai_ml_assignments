from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load models
role_model = pickle.load(open("models/role_model.pkl", "rb"))
hiring_model = pickle.load(open("models/hiring_model.pkl", "rb"))

def full_resume_screening(input_df):
    
    # Step 1: Predict Role
    predicted_role = role_model.predict(input_df["Skills"])[0]
    
    # Add role to dataframe
    input_df = input_df.copy()
    input_df["Job Role"] = predicted_role
    
    # Step 2: Predict Hiring Decision
    decision = hiring_model.predict(input_df)[0]
    probabilities = hiring_model.predict_proba(input_df)[0]
    confidence = round(max(probabilities) * 100, 2)
    
    return predicted_role, decision, confidence


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = {
            "Skills": request.form["skills"],
            "Education": request.form["education"],
            "Certifications": request.form["certifications"],
            "Experience (Years)": float(request.form["experience"]),
            "Salary Expectation ($)": float(request.form["salary"]),
            "Projects Count": float(request.form["projects"])
        }

        input_df = pd.DataFrame([data])

        role, decision, confidence = full_resume_screening(input_df)

        decision_text = "Hire ✅" if decision == 1 else "Reject ❌"

        return render_template(
            "index.html",
            role=role,
            decision=decision_text,
            confidence=confidence
        )

    except Exception as e:
        return render_template("index.html", error=str(e))


if __name__ == "__main__":
    app.run(debug=True)