📧 Email Spam Classification
Week 4 – Day 4 Assignment
Date: 13 February 2026
📌 Objective

The objective of this assignment is to build and evaluate machine learning models to classify emails as Spam or Not Spam using:

Logistic Regression

Random Forest

5-Fold Cross Validation

10-Fold Cross Validation

We also analyze model stability and generalization.

📂 Dataset Information

The dataset contains the following columns:

Column Name	Description
text	Email message content
spam	Target variable (0 = Not Spam, 1 = Spam)
🛠 Technologies Used

Python

pandas

NumPy

scikit-learn

TF-IDF Vectorization

🧹 Data Preprocessing Steps

Removed null values

Removed duplicate records

Converted text to lowercase

Removed special characters

Applied TF-IDF vectorization

Removed English stopwords

🤖 Models Implemented
1️⃣ Logistic Regression

Suitable for high-dimensional text data

Fast and efficient

Good generalization performance

2️⃣ Random Forest

Ensemble-based classifier

Captures non-linear relationships

May overfit with high-dimensional sparse data

🔁 Cross Validation

We performed:

✅ 5-Fold Cross Validation

✅ 10-Fold Cross Validation

Evaluation Metrics Used:

Accuracy

Precision

Recall

F1 Score

📊 Model Comparison Summary
Metric	Logistic Regression	Random Forest
Accuracy	High	Moderate
Precision	High	Good
Recall	High	Good
F1 Score	Higher	Slightly Lower
Stability (Std Dev)	Lower	Higher
📈 Insights

Logistic Regression performed better on text data.

It showed lower standard deviation across folds → more stable.

10-Fold CV gave more reliable performance estimates.

Random Forest showed slightly higher variance.

Logistic Regression generalizes better for sparse TF-IDF features.

🎯 Conclusion

For spam email classification:

✅ Logistic Regression is more stable and generalizes better.
⚠ Random Forest may overfit on high-dimensional text data.

Cross-validation helps in evaluating true model performance and prevents overfitting.

📁 Repository Structure
├── spam.csv
├── spam_classifier.ipynb
├── README.md

