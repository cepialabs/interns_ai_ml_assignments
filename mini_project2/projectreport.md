# Resume Screening ML Model

## Business Context

In modern recruitment processes, companies receive a large number of resumes for each job opening. 
Manually reviewing all resumes is time-consuming and inefficient.

This project focuses on automating the filtering of resumes based on job requirements 
using Machine Learning and Natural Language Processing (NLP).

The system helps HR teams identify suitable candidates quickly and rank them efficiently.
## Problem Statement

Build an NLP-based Machine Learning model that can:

- Analyze resume text
- Extract important information such as skills and experience
- Classify resumes as shortlisted (1) or not shortlisted (0)
- Rank candidates based on suitability score
## Dataset Description

The dataset contains 4500 resumes with the following features:

- Resume text (raw_text)
- Skills
- Years of experience
- Highest degree
- Current job title
- Portfolio availability
- Job role label (Target variable)

Target:
1 -> Suitable / Shortlisted  
0 -> Not Suitable
## Methodology
### Step 1: Data Preprocessing

- Loaded dataset using pandas
- Cleaned resume text (lowercasing, removing punctuation, removing special characters)
- Handled missing values
- Encoded categorical variables
- Scaled numerical features
### Step 2: Feature Engineering

Text Features:
- Used TF-IDF Vectorizer to convert resume text into numerical vectors.

Structured Features:
- Years of experience
- Degree (encoded)
- Portfolio availability
- Skills

Combined text and structured features using sparse matrix stacking.
### Step 3: Model Training

- Split dataset into training and testing sets (80% training, 20% testing)
- Trained Logistic Regression model
- Trained Random Forest Classifier
- Used Logistic Regression probabilities for ranking
### Step 4: Candidate Ranking

Created a custom scoring function to assign a shortlist score based on:

- Model prediction probability
- Years of experience
- Relevant skills
- Portfolio availability

Candidates are ranked based on the shortlist_score.

## Expected Outcome

The expected outcome of this project is to build an automated Resume Screening 
Machine Learning system that can:

1. Classify resumes as Shortlisted (1) or Not Shortlisted (0) 
   based on job requirements.

2. Generate prediction probabilities using Logistic Regression 
   to understand candidate suitability.

3. Rank candidates using a custom shortlist_score based on:
   - Model prediction probability
   - Years of experience
   - Relevant skills
   - Portfolio availability

4. Identify Top Candidates by sorting resumes based on shortlist_score.

5. Visualize model performance using:
   - Accuracy Score
   - Confusion Matrix
   - Classification Report
   - Precision-Recall Curve

Final Output of the System:
- Automated filtering of resumes
- Ranked list of suitable candidates
- Reduced manual screening effort
- Improved recruitment efficiency

## Model Evaluation

The following evaluation metrics were used:

- Accuracy Score
- Classification Report
- Confusion Matrix
- Precision-Recall Curve

Precision-Recall curve was used because resume screening is a classification 
problem where minimizing false positives and false negatives is important.
## Results

- The model successfully classified resumes into shortlisted and non-shortlisted categories.
- TF-IDF improved text understanding.
- Logistic Regression provided stable probability outputs.
- Top candidates were successfully ranked based on shortlist_score.
## Applications

- HR Automation Systems
- Applicant Tracking Systems (ATS)
- Resume Filtering Platforms
- Recruitment Agencies
## Conclusion

This project demonstrates how Machine Learning and NLP can automate 
resume screening and candidate ranking.

By combining text processing with structured features, the system 
efficiently filters and ranks candidates based on job requirements.

The model reduces manual effort and improves recruitment efficiency