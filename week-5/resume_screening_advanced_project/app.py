import streamlit as st
import pandas as pd
import numpy as np
import pdfplumber
import re
import plotly.express as px

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import cross_val_score


# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Screening & Ranking System")
st.markdown("Smart NLP-based Resume Analyzer with Ranking Engine")


# -------------------------------
# LOAD DATA
# -------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/resumes_dataset.csv")

df = load_data()


# -------------------------------
# PREPROCESSING
# -------------------------------
le = LabelEncoder()
df['Label'] = le.fit_transform(df['job_role'])

tfidf = TfidfVectorizer(stop_words='english', max_features=3000)
X = tfidf.fit_transform(df['resume_text'])
y = df['Label']


# -------------------------------
# SIDEBAR - MODEL SETTINGS
# -------------------------------
st.sidebar.header("⚙ Model Settings")

model_choice = st.sidebar.selectbox(
    "Choose Model",
    ["Logistic Regression", "Naive Bayes", "Linear SVM"]
)

if model_choice == "Logistic Regression":
    model = LogisticRegression(max_iter=1000)
elif model_choice == "Naive Bayes":
    model = MultinomialNB()
else:
    model = LinearSVC()

model.fit(X, y)

accuracy = cross_val_score(model, X, y, cv=5).mean() * 100
st.sidebar.info(f"Model Accuracy: {accuracy:.2f}%")


# -------------------------------
# SKILL DATABASE
# -------------------------------
SKILLS_DB = [
    "Python", "Machine Learning", "Deep Learning", "SQL",
    "Data Analysis", "NLP", "Power BI", "Tableau",
    "Java", "C++", "React", "Django", "Flask"
]


def extract_skills(text):
    skills = []
    for skill in SKILLS_DB:
        if re.search(rf"\b{skill}\b", text, re.IGNORECASE):
            skills.append(skill)
    return skills


def skill_match(resume_skills, job_desc):
    job_skills = extract_skills(job_desc)
    matched = list(set(resume_skills) & set(job_skills))
    score = (len(matched) / len(job_skills)) * 100 if job_skills else 0
    return score, matched


def resume_strength_score(text):
    score = 0
    text = text.lower()
    if "experience" in text:
        score += 30
    if "education" in text:
        score += 20
    if "project" in text:
        score += 20
    if "certification" in text:
        score += 30
    return score


def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + " "
    return text


# -------------------------------
# TABS
# -------------------------------
tab1, tab2 = st.tabs(["📄 Resume Analysis", "🏆 Candidate Ranking"])


# ============================================================
# TAB 1 - RESUME ANALYSIS
# ============================================================
with tab1:

    st.header("📄 Smart Resume Analyzer")

    col1, col2 = st.columns(2)

    with col1:
        uploaded_file = st.file_uploader("Upload Resume (PDF or TXT)", type=["pdf", "txt"])

    with col2:
        job_description = st.text_area("Paste Job Description")

    resume_text = ""

    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            resume_text = extract_text_from_pdf(uploaded_file)
            st.success("PDF Uploaded & Text Extracted")
        else:
            resume_text = uploaded_file.read().decode("utf-8")
            st.success("TXT Uploaded")

    if st.button("🚀 Analyze Resume"):

        if resume_text.strip() == "":
            st.warning("Please upload a resume file.")
        else:
            with st.spinner("Analyzing Resume..."):

                resume_vec = tfidf.transform([resume_text])

                # Role Prediction
                prediction = model.predict(resume_vec)
                predicted_role = le.inverse_transform(prediction)[0]

                st.success(f"🎯 Predicted Job Role: {predicted_role}")

                colA, colB, colC = st.columns(3)

                if model_choice != "Linear SVM":
                    prob = model.predict_proba(resume_vec).max() * 100
                    colA.metric("Confidence", f"{prob:.2f}%")

                if job_description.strip():
                    job_vec = tfidf.transform([job_description])
                    similarity = cosine_similarity(resume_vec, job_vec)[0][0] * 100
                    colB.metric("Job Match", f"{similarity:.2f}%")

                # Skill Analysis
                resume_skills = extract_skills(resume_text)
                skill_score, matched = skill_match(resume_skills, job_description)

                colC.metric("Skill Match", f"{skill_score:.2f}%")

                st.markdown("### 🛠 Extracted Skills")
                st.write(resume_skills)

                if resume_skills:
                    fig = px.histogram(
                        pd.DataFrame({"Skills": resume_skills}),
                        x="Skills",
                        title="Extracted Skills Distribution"
                    )
                    st.plotly_chart(fig, use_container_width=True)

                strength = resume_strength_score(resume_text)
                st.markdown("### 💪 Resume Strength")
                st.progress(strength)
                st.caption(f"Resume Strength Score: {strength}/100")


# ============================================================
# TAB 2 - CANDIDATE RANKING
# ============================================================
with tab2:

    st.header("🏆 Rank Candidates from Dataset")

    job_desc_rank = st.text_area("Enter Job Description for Ranking")

    min_score = st.slider("Minimum Match Score (%)", 0, 100, 50)

    if st.button("Rank Candidates"):

        if job_desc_rank.strip() == "":
            st.warning("Enter job description.")
        else:
            job_vec = tfidf.transform([job_desc_rank])
            resume_vecs = tfidf.transform(df['resume_text'])

            similarities = cosine_similarity(resume_vecs, job_vec).flatten() * 100

            df['Match_Score'] = similarities

            ranked_df = df[df['Match_Score'] >= min_score] \
                .sort_values(by="Match_Score", ascending=False)

            st.write("### 🔝 Top Matching Candidates")
            st.dataframe(ranked_df[['job_role', 'Match_Score']].head(5))

            if not ranked_df.empty:
                fig = px.bar(
                    ranked_df.head(5),
                    x="Match_Score",
                    y="job_role",
                    orientation="h",
                    title="Top 5 Candidates"
                )
                st.plotly_chart(fig, use_container_width=True)


# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.markdown("🚀 Advanced Internship-Level AI Resume Screening System")