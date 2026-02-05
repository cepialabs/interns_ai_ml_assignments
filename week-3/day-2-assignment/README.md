# Week 3 -- Day 2 Assignment: Email Spam Classification using Logistic Regression

**Intern Name:** Bodas Karunanjali\
**Intern ID:** INT2026-1462\
**Organization:** Cepialabs\
**Date:** 05-Feb-2026

------------------------------------------------------------------------

## Project Overview

This assignment implements **Logistic Regression for Email Spam
Classification**.\
The objective is to build a machine learning model that classifies
emails as either **Spam (1)** or **Not Spam / Ham (0)** based on their
text content.

Through this assignment, we learn:

-   How to handle real-world text data\
-   How to convert text into numerical features\
-   How Logistic Regression works for classification\
-   How to evaluate a machine learning model

------------------------------------------------------------------------

## Dataset

We used the **Spam SMS Dataset (spam.csv)** from Kaggle.

The dataset contains two main columns:

-   **v1** → Label (`ham` or `spam`)\
-   **v2** → Email / SMS message text

------------------------------------------------------------------------

## Tasks Completed

### Task 1 -- Data Loading and Exploration

-   Loaded the dataset using Pandas\
-   Handled encoding issue using `latin-1`\
-   Checked dataset structure and column names\
-   Renamed columns for better understanding

### Task 2 -- Text Preprocessing

-   Converted text messages into numerical format using **TF-IDF
    Vectorization**\
-   Removed common English stopwords\
-   Created feature matrix `X` from text\
-   Converted labels into binary values (`ham = 0`, `spam = 1`)

### Task 3 -- Model Training

-   Split data into training and testing sets\
-   Trained a **Logistic Regression** model\
-   Used training data to teach the model patterns in spam messages

### Task 4 -- Model Evaluation

-   Evaluated model using Accuracy Score\
-   Generated Classification Report\
-   Observed good precision and recall for both spam and non-spam emails

------------------------------------------------------------------------

## Results

The model achieved high accuracy (around 97%), showing that Logistic
Regression combined with TF-IDF is effective for spam detection.

The model can correctly identify most spam messages while minimizing
false predictions.

------------------------------------------------------------------------

## Files in This Folder

    week-3/day-2-assignment/
    ├── spam.csv
    ├── assignment-2.ipynb
    └── README.md

------------------------------------------------------------------------

## Conclusion

This assignment successfully demonstrated how Logistic Regression can be
applied to text classification problems.

The techniques used here form the foundation for real-world spam filters
used in email systems like Gmail and Outlook.
