# Resume Screening ML Model

## 📌 Business Context

In modern recruitment processes, companies receive thousands of resumes for a single job opening.  
Manually reviewing resumes is time-consuming, inefficient, and prone to human bias.

This project builds a Machine Learning-based Resume Screening System that automates filtering of resumes based on job requirements.

The system helps HR teams:
- Reduce manual effort
- Improve hiring efficiency
- Identify top candidates quickly
- Rank candidates based on suitability

---

## 🎯 Problem Statement

Build an NLP-based Machine Learning model that can:

- Analyze resume text
- Extract important information such as skills and experience
- Classify resumes as Shortlisted (1) or Not Shortlisted (0)
- Rank candidates based on a suitability score

---

## 📊 Dataset Description

**Dataset collected :**  Kaggle 
**URL :** C:\Users\Malli Mounika\Downloads\ml_resume_dataset_4500.csv

The dataset contains 4500 resumes with the following features:

- id
- name
- years_experience
- highest_degree
- skills
- current_title
- has_portfolio
- raw_text (resume text)
- label (Target Variable)

Target:
- 1 → Suitable / Shortlisted
- 0 → Not Suitable

---

## ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression
- Random Forest Classifier

---

## 🧠 Methodology

### 1️⃣ Data Preprocessing
- Loaded dataset using pandas
- Cleaned resume text (lowercasing, removing punctuation)
- Handled missing values
- Encoded categorical variables
- Scaled numerical features

---

### 2️⃣ Feature Engineering

Text Features:
- Used TF-IDF Vectorizer to convert resume text into numerical vectors

Structured Features:
- Years of experience
- Highest degree (encoded)
- Portfolio availability
- Skills

Combined text and structured features using sparse matrix stacking.

---

### 3️⃣ Model Training

- Split dataset into training and testing sets (80-20 split)
- Trained Logistic Regression model
- Trained Random Forest Classifier
- Used Logistic Regression probabilities for ranking

---

### 4️⃣ Candidate Ranking

Created a custom function to generate a shortlist_score based on:

- Model prediction probability
- Years of experience
- Relevant skills
- Portfolio availability

Candidates are ranked based on shortlist_score.

---

## 📈 Model Evaluation

Used the following evaluation metrics:

- Accuracy Score
- Classification Report
- Confusion Matrix
- Precision-Recall Curve

Precision-Recall analysis helps in selecting the optimal threshold 
to balance false positives and false negatives.

---

## ✅ Expected Outcome

The system is expected to:

- Automatically classify resumes as shortlisted or not shortlisted
- Generate probability scores for candidate suitability
- Rank candidates based on shortlist_score
- Identify top candidates efficiently
- Reduce manual screening effort

---

## 📌 Results

- Successfully classified resumes into shortlisted and non-shortlisted categories
- TF-IDF improved text feature extraction
- Logistic Regression provided stable probability outputs
- Top candidates were ranked effectively using shortlist_score

---

## 🚀 Applications

- HR Automation Systems
- Applicant Tracking Systems (ATS)
- Internship Screening Platforms
- Recruitment Agencies

---

## 🔮 Future Improvements

- Implement BERT or advanced NLP embeddings
- Improve skill matching using semantic similarity
- Deploy as a web application (Flask / Streamlit)
- Add bias and fairness evaluation

---

## 🏁 Conclusion

This project demonstrates how Machine Learning and NLP can automate 
resume screening and candidate ranking.

By combining text processing with structured features, the system 
efficiently filters and ranks candidates based on job requirements, 
reducing recruitment time and improving hiring quality.

---
