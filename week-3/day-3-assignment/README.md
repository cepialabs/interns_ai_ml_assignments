# Week 3 – Day 3 Assignment

**Date:** 6 February 2026

## Dataset: Spam Email Dataset

### Columns in the Dataset

* **text**: The email content (raw text of the email)
* **spam**: Target label

  * `1` → Spam email
  * `0` → Not spam (ham)

---

## Objective of the Assignment

1. Use **K-Nearest Neighbors (KNN)** to classify emails as spam or not spam based on word-related features.
2. Use a **Decision Tree** to classify emails using the same dataset.
3. Understand and compare how both algorithms perform on text-based data.

---

## Step-by-Step Methodology (Without Code)

### Step 1: Understand the Problem

* Email spam detection is a **binary classification problem**.
* Input: Email text
* Output: Spam (1) or Not Spam (0)

---

### Step 2: Data Loading

* Load the spam email dataset.
* Verify that the dataset contains only two columns: `text` and `spam`.
* Check the total number of records and labels.

---

### Step 3: Data Preprocessing

Since machine learning models cannot work directly with raw text, preprocessing is required:

* Convert all text to lowercase
* Remove punctuation and special characters
* Remove stop words (e.g., *is, the, and*)
* Convert text data into numerical form using:

  * Bag of Words or
  * TF-IDF (Term Frequency–Inverse Document Frequency)

This step converts the `text` column into numerical feature vectors.

---

### Step 4: Feature and Target Separation

* **Features (X):** Transformed numerical representation of the `text` column
* **Target (y):** `spam` column

---

### Step 5: Train-Test Split

* Split the dataset into:

  * Training data (e.g., 80%)
  * Testing data (e.g., 20%)
* Training data is used to train the model.
* Testing data is used to evaluate performance.

---

## KNN Classification

### Step 6: Apply K-Nearest Neighbors (KNN)

* Choose a value of **K** (number of nearest neighbors).
* KNN classifies an email based on the majority class of its nearest neighbors.
* Distance is calculated using numerical feature vectors.

### Step 7: Model Training (KNN)

* Train the KNN model using training data.
* The model stores the training instances for comparison.

### Step 8: Prediction Using KNN

* Predict spam or non-spam emails for the test dataset.

### Step 9: Evaluation of KNN Model

* Accuracy
* Confusion Matrix
* Precision, Recall, F1-score

---

## Decision Tree Classification

### Step 10: Apply Decision Tree Algorithm

* Decision Tree splits data based on feature values.
* It creates rules in the form of a tree structure.
* Each node represents a decision based on a word feature.

### Step 11: Model Training (Decision Tree)

* Train the decision tree using training data.
* The model learns splitting rules from features.

### Step 12: Prediction Using Decision Tree

* Predict whether emails are spam or not spam for test data.

### Step 13: Evaluation of Decision Tree Model

* Accuracy
* Confusion Matrix
* Precision, Recall, F1-score

---

## Step 14: Model Comparison

| Criteria            | KNN                      | Decision Tree     |
| ------------------- | ------------------------ | ----------------- |
| Speed               | Slower during prediction | Faster prediction |
| Interpretability    | Low                      | High              |
| Performance on Text | Moderate                 | Good              |
| Memory Usage        | High                     | Low               |

---

## Conclusion

* Both KNN and Decision Tree can classify spam emails effectively.
* **KNN** depends heavily on distance and feature scaling.
* **Decision Tree** provides better interpretability and faster predictions.
* For text-based spam classification, Decision Trees often perform better and are easier to understand.






