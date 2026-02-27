import streamlit as st
import pandas as pd
import numpy as np
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Screening & Ranking System")
st.markdown("Upload Resume (PDF) and Match with Job Description")

# -------------------------------
# Load Dataset
# -------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/resumes_dataset.csv")

df = load_data()

# -------------------------------
# Preprocessing
# -------------------------------
le = LabelEncoder()
df['Label'] = le.fit_transform(df['job_role'])

tfidf = TfidfVectorizer(stop_words='english', max_features=3000)
X = tfidf.fit_transform(df['resume_text'])
y = df['Label']

# -------------------------------
# Sidebar - Model Selection
# -------------------------------
st.sidebar.header("⚙ Model Settings")

model_choice = st.sidebar.selectbox(
    "Choose Model",
    ["Logistic Regression", "Naive Bayes", "Linear SVM"]
)

if model_choice == "Logistic Regression":
    model = LogisticRegression()
elif model_choice == "Naive Bayes":
    model = MultinomialNB()
else:
    model = LinearSVC()

model.fit(X, y)

# -------------------------------
# PDF Text Extraction Function
# -------------------------------
def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + " "
    return text

# -------------------------------
# Resume Upload Section
# -------------------------------
st.subheader("📌 Upload Resume")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF or TXT)",
    type=["pdf", "txt"]
)

resume_text = ""

if uploaded_file is not None:

    if uploaded_file.type == "application/pdf":
        resume_text = extract_text_from_pdf(uploaded_file)
        st.success("PDF Resume Uploaded & Text Extracted!")

    elif uploaded_file.type == "text/plain":
        resume_text = uploaded_file.read().decode("utf-8")
        st.success("TXT Resume Uploaded!")

# -------------------------------
# Job Description Section
# -------------------------------
st.subheader("📌 Job Description (Optional)")
job_description = st.text_area("Paste Job Description Here")

# -------------------------------
# Analyze Button
# -------------------------------
if st.button("🚀 Analyze Resume"):

    if resume_text.strip() == "":
        st.warning("Please upload a resume file.")
    else:

        resume_vec = tfidf.transform([resume_text])

        # Predict Job Role
        prediction = model.predict(resume_vec)
        predicted_role = le.inverse_transform(prediction)[0]

        st.success(f"🎯 Predicted Job Role: {predicted_role}")

        # Confidence Score
        if model_choice != "Linear SVM":
            prob = model.predict_proba(resume_vec).max() * 100
            st.info(f"📊 Prediction Confidence: {prob:.2f}%")

        # Job Matching Score
        if job_description.strip() != "":
            job_vec = tfidf.transform([job_description])
            similarity = cosine_similarity(resume_vec, job_vec)[0][0] * 100
            st.metric("📈 Job Match Score", f"{similarity:.2f}%")

# -------------------------------
# Ranking Feature
# -------------------------------
st.markdown("---")
st.subheader("🏆 Rank All Candidates from Dataset")

job_desc_rank = st.text_area("Enter Job Description for Ranking")

if st.button("Rank Candidates"):

    if job_desc_rank.strip() == "":
        st.warning("Enter job description to rank.")
    else:
        job_vec = tfidf.transform([job_desc_rank])
        resume_vecs = tfidf.transform(df['resume_text'])

        similarities = cosine_similarity(resume_vecs, job_vec).flatten()

        df['Match_Score'] = similarities
        ranked_df = df.sort_values(by="Match_Score", ascending=False).head(5)

        st.write("### 🔝 Top 5 Matching Candidates")
        st.dataframe(ranked_df[['job_role', 'Match_Score']])

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown("Internship Project | NLP Resume Screening with PDF Upload")