import streamlit as st
import pandas as pd
import numpy as np
import pdfplumber
import re
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import cross_val_score


# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------
st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

st.title("🤖 AI Resume Screening & Ranking System")
st.markdown("### Smart NLP Resume Analyzer & Candidate Ranking Dashboard")


# ------------------------------------------------
# LOAD DATA
# ------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/resumes_dataset.csv")

df = load_data()


# ------------------------------------------------
# PREPROCESSING
# ------------------------------------------------
le = LabelEncoder()
df['Label'] = le.fit_transform(df['job_role'])

tfidf = TfidfVectorizer(stop_words='english', max_features=3000)

X = tfidf.fit_transform(df['resume_text'])

y = df['Label']


# ------------------------------------------------
# SIDEBAR SETTINGS
# ------------------------------------------------
st.sidebar.title("⚙ Model Settings")

model_choice = st.sidebar.selectbox(
    "Choose ML Model",
    ["Logistic Regression","Naive Bayes","Linear SVM"]
)

if model_choice == "Logistic Regression":
    model = LogisticRegression(max_iter=1000)

elif model_choice == "Naive Bayes":
    model = MultinomialNB()

else:
    model = LinearSVC()

model.fit(X,y)

accuracy = cross_val_score(model,X,y,cv=5).mean()*100

st.sidebar.success(f"Model Accuracy: {accuracy:.2f}%")


# ------------------------------------------------
# MODEL COMPARISON
# ------------------------------------------------
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Naive Bayes": MultinomialNB(),
    "Linear SVM": LinearSVC()
}

scores = {}

for name,m in models.items():

    score = cross_val_score(m,X,y,cv=5).mean()

    scores[name] = score

st.sidebar.markdown("### 📊 Model Comparison")

st.sidebar.bar_chart(pd.DataFrame(scores,index=["Accuracy"]).T)


# ------------------------------------------------
# SKILL DATABASE
# ------------------------------------------------
SKILLS_DB = [
"Python","Machine Learning","Deep Learning","SQL","Data Analysis",
"NLP","Power BI","Tableau","Excel","Java","C++","React","Django",
"Flask","TensorFlow","PyTorch","AWS","Azure","Docker","Kubernetes",
"Git","Linux","Spark","Hadoop","MongoDB"
]


# ------------------------------------------------
# FUNCTIONS
# ------------------------------------------------
def extract_skills(text):

    skills=[]

    for skill in SKILLS_DB:

        if re.search(rf"\b{skill}\b",text,re.IGNORECASE):

            skills.append(skill)

    return skills


def skill_match(resume_skills,job_desc):

    job_skills = extract_skills(job_desc)

    matched = list(set(resume_skills)&set(job_skills))

    score = (len(matched)/len(job_skills))*100 if job_skills else 0

    return score,matched,job_skills


def missing_skills(resume_skills,job_skills):

    return list(set(job_skills)-set(resume_skills))


def resume_strength_score(text):

    score=0

    text=text.lower()

    if "experience" in text:
        score+=30

    if "education" in text:
        score+=20

    if "project" in text:
        score+=20

    if "certification" in text:
        score+=30

    return score


def estimate_experience(text):

    matches = re.findall(r'\d+\+?\s*years?',text.lower())

    if matches:
        return matches[0]

    return "Not Mentioned"


def resume_suggestions(text,skills,missing):

    suggestions=[]

    if len(skills)<5:
        suggestions.append("Add more technical skills.")

    if "project" not in text.lower():
        suggestions.append("Add project experience.")

    if "experience" not in text.lower():
        suggestions.append("Mention internship/work experience.")

    if missing:
        suggestions.append("Learn missing skills: "+", ".join(missing))

    if not suggestions:
        suggestions.append("Great resume.")

    return suggestions


def extract_text_from_pdf(file):

    text=""

    with pdfplumber.open(file) as pdf:

        for page in pdf.pages:

            if page.extract_text():

                text+=page.extract_text()

    return text


# ------------------------------------------------
# TABS
# ------------------------------------------------
tab1,tab2 = st.tabs(["📄 Resume Analyzer","🏆 Candidate Ranking"])


# ==================================================
# TAB 1
# ==================================================
with tab1:

    st.subheader("Upload Resume")

    col1,col2 = st.columns(2)

    with col1:

        uploaded_file = st.file_uploader("Upload Resume",type=["pdf","txt"])

    with col2:

        job_description = st.text_area("Paste Job Description")


    resume_text=""

    if uploaded_file:

        if uploaded_file.type=="application/pdf":

            resume_text = extract_text_from_pdf(uploaded_file)

        else:

            resume_text = uploaded_file.read().decode()


    if st.button("Analyze Resume"):

        if resume_text.strip()=="":

            st.warning("Upload resume")

        else:

            with st.spinner("Analyzing..."):

                resume_vec = tfidf.transform([resume_text])

                pred = model.predict(resume_vec)

                role = le.inverse_transform(pred)[0]

                st.success(f"Predicted Role: {role}")


                # similarity
                similarity=0

                if job_description:

                    job_vec=tfidf.transform([job_description])

                    similarity = cosine_similarity(resume_vec,job_vec)[0][0]*100

                    st.metric("Job Match",f"{similarity:.2f}%")


                skills = extract_skills(resume_text)

                skill_score,matched,job_skills = skill_match(skills,job_description)

                missing = missing_skills(skills,job_skills)


                strength = resume_strength_score(resume_text)

                experience = estimate_experience(resume_text)


                ai_score = similarity*0.5 + skill_score*0.3 + strength*0.2


                st.subheader("ATS Score")

                st.progress(int(ai_score))

                st.write(f"Score: {ai_score:.2f}/100")


                st.subheader("Skills Detected")

                st.write(skills)


                if missing:

                    st.error("Missing Skills: "+", ".join(missing))


                st.subheader("Experience")

                st.write(experience)


                st.subheader("Resume Suggestions")

                suggestions = resume_suggestions(resume_text,skills,missing)

                for s in suggestions:

                    st.write("•",s)


                # skill chart
                if skills:

                    fig = px.histogram(pd.DataFrame({"Skills":skills}),x="Skills")

                    st.plotly_chart(fig,use_container_width=True)


                # wordcloud
                wc = WordCloud(width=800,height=400).generate(resume_text)

                fig,ax = plt.subplots()

                ax.imshow(wc)

                ax.axis("off")

                st.pyplot(fig)


                report=f"""
AI Resume Screening Report

Role: {role}

Job Match: {similarity:.2f}

Skill Match: {skill_score:.2f}

Strength: {strength}

AI Score: {ai_score}

Skills:
{", ".join(skills)}

Missing Skills:
{", ".join(missing)}

Suggestions:
{chr(10).join(suggestions)}
"""

                st.download_button(
                    "Download Report",
                    report,
                    file_name="resume_report.txt"
                )


# ==================================================
# TAB 2
# ==================================================
with tab2:

    st.subheader("Candidate Ranking System")

    job_desc = st.text_area("Enter Job Description")

    min_score = st.slider("Minimum Match",0,100,50)


    if st.button("Rank Candidates"):

        job_vec = tfidf.transform([job_desc])

        resume_vecs = tfidf.transform(df['resume_text'])

        similarity = cosine_similarity(resume_vecs,job_vec).flatten()*100

        df["Match"] = similarity

        df["AI_Score"] = df["Match"]*0.7 + 30


        ranked = df[df["Match"]>=min_score].sort_values("AI_Score",ascending=False)


        st.dataframe(ranked[['job_role','AI_Score']].head(10))


        fig = px.bar(
            ranked.head(10),
            x="AI_Score",
            y="job_role",
            orientation="h",
            title="Top Candidates"
        )

        st.plotly_chart(fig,use_container_width=True)


# ------------------------------------------------
# FOOTER
# ------------------------------------------------
st.markdown("---")

st.markdown("🚀 AI Resume Screening System | NLP + ML Powered")