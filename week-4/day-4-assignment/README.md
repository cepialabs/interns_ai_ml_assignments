# 📘 Week 4 – Day 4 Assignment  
## Random Forest & Logistic Regression with Cross-Validation  
📅 Date: 13-02-2026  
📊 Dataset: Spam Email Classifier (Kaggle)  
🧠 Problem Type: Supervised Machine Learning (Classification)

---

## 🎯 Objective

The objective of this assignment is to:

- Train Logistic Regression and Random Forest models
- Perform 10-Fold Cross-Validation
- Compare performance metrics
- Evaluate model stability
- Analyze generalization ability
- Compare results and draw insights

---

## 📊 Dataset Information

**Source:** Kaggle  
**url:** https://www.kaggle.com/datasets/abdallahwagih/spam-emails
**Dataset:** Spam Email Dataset  

**Features:**
- `Category` → ham / spam
- `Message` → Email text

**Target Variable:**
- Ham → 0  
- Spam → 1  

Total Records: 5572

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Jupyter Notebook

---

## 🧩 Steps Performed

### 1️⃣ Data Preprocessing

- Loaded dataset using Pandas
- Converted labels (ham/spam) into numeric values
- Checked class distribution
- Split dataset into training and testing sets
- Applied TF-IDF vectorization for text processing

---

### 2️⃣ Model Training

Trained two models:

- Logistic Regression
- Random Forest Classifier

Used Pipeline to combine TF-IDF and model training.

---

### 3️⃣ Cross-Validation

- Applied 10-Fold Cross-Validation
- Evaluated using:
  - Accuracy
  - Precision
  - Recall
  - F1 Score
- Calculated Standard Deviation for stability analysis

---

### 4️⃣ Model Evaluation

Evaluated models on test dataset using:

- Accuracy Score
- F1 Score
- Classification Report
- Confusion Matrix

Compared Cross-Validation results with Test results.

---

## 📈 Evaluation Metrics

| Metric Used | Purpose |
|-------------|----------|
| Accuracy | Overall correctness |
| Precision | Spam prediction correctness |
| Recall | Spam detection ability |
| F1 Score | Balance between Precision & Recall |

Primary Metric: **F1 Score**

---

## 🔍 Observations

- Logistic Regression performed slightly better for text classification.
- Random Forest showed strong performance but slightly higher variance.
- Cross-validation provided reliable performance estimation.
- Lower standard deviation indicates better model stability.
- Test accuracy was close to cross-validation accuracy, indicating good generalization.

---

## 🧠 Conclusion

This assignment demonstrated:

- Implementation of ensemble and linear models.
- Importance of cross-validation in evaluating stability.
- Comparison of multiple performance metrics.
- Understanding of generalization and model performance.

### Key Learnings:

- Cross-validation improves reliability.
- Logistic Regression works efficiently for text classification.
- Random Forest is powerful but may slightly overfit.
- F1 Score is important for classification problems.

---

## 📌 Final Note

This assignment strengthened understanding of:

- Cross-validation
- Model comparison
- Stability analysis
- Generalization evaluation
- Performance metrics in classification
