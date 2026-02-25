

# 📄 Resume Screening using Machine Learning

**Logistic Regression & Random Forest Classifier**
📅 *Date: 25 February 2026*

---

## 📌 Project Overview

This project focuses on building a **machine learning–based resume screening system** that automatically classifies resumes as **Shortlisted** or **Rejected** based on textual content.

The goal is to simulate how recruiters can use ML models to reduce manual resume screening time and improve hiring efficiency.

---

## 🎯 Objective

* Automate resume screening using NLP and ML
* Convert resume text into numerical features using **TF-IDF**
* Train and compare **Logistic Regression** and **Random Forest** models
* Evaluate model performance using accuracy, confusion matrix, and ROC-AUC

---

## 🧠 Dataset

* **Dataset name:** Resume Screening Dataset (4500 Resumes)
* **Source:** Kaggle
* **Dataset URL:**
  [https://www.kaggle.com/datasets/kawsertalukder/resume-screening-dataset4500](https://www.kaggle.com/datasets/kawsertalukder/resume-screening-dataset4500)
* **File name:** `ml_resume_dataset_4500.csv`
* **Size:** ~4,500 resumes
* **Target column:**

  * `label`

    * `0` → Rejected
    * `1` → Shortlisted
* **Input feature:** Resume text

> 📌 *Ensure the dataset file is downloaded from Kaggle and placed in the same directory as the notebook before execution.*

---

## ⚙️ Technologies & Libraries Used

* **Programming Language:** Python
* **Libraries:**

  * pandas, numpy
  * matplotlib, seaborn
  * scikit-learn

    * TF-IDF Vectorizer
    * Logistic Regression
    * Random Forest Classifier
    * Model evaluation metrics

---

## 🧪 Workflow

1. **Import required libraries**
2. **Load and explore the dataset**
3. **Visualize label distribution**
4. **Text preprocessing using TF-IDF**
5. **Train-test split**
6. **Model training**

   * Logistic Regression
   * Random Forest Classifier
7. **Model evaluation**

   * Accuracy Score
   * Confusion Matrix
   * Classification Report
   * ROC-AUC Score
8. **Model comparison**

---

## 📊 Model Evaluation Metrics

* Accuracy
* ROC-AUC Score
* Precision, Recall, F1-score
* Confusion Matrix

These metrics help determine how well the model distinguishes between shortlisted and rejected resumes.

---

## 🏆 Results & Insights

* Logistic Regression performs well on text-heavy data due to linear decision boundaries.
* Random Forest captures non-linear patterns and feature importance.
* TF-IDF significantly improves model performance by emphasizing relevant resume keywords.

---



