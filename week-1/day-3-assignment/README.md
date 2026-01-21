##  DAY 3 ASSIGNMENT — Customer Churn Data Cleaning
Intern ID: INT2026-1462

Date: 21-01-2026

##  Objective

The objective of this assignment is to clean a messy Customer Churn dataset and make it ready for Machine Learning.

The dataset intentionally contains:

Missing age values

Duplicate rows

Inconsistent gender formats

Salary outliers

##  Dataset Details

Dataset Name: Customer Churn (Messy Dataset)

Original File: customer_churn_messey.csv

##  Files Submitted

day-3-assignment.ipynb

customer_churn_messey.csv


##  Data Cleaning Steps Performed
1️⃣ Load Dataset

Loaded the dataset using Pandas

Displayed initial rows to understand data structure

## 2️⃣ Basic Data Understanding

Checked dataset shape, column names, and data types

Reviewed summary statistics for numerical and categorical columns

## 3️⃣ Handle Missing Values

Identified missing values in the Age column

Filled missing ages using the median value

## 4️⃣ Remove Duplicate Rows

Identified duplicate records

Removed duplicates to avoid data repetition

## 5️⃣ Clean Gender Column

Standardized gender values into:

male

female

Fixed inconsistent formats such as:

M, m, Male, MALE

F, f, Female, FEMALE

## 6️⃣ Handle Salary Outliers

Detected salary outliers using the IQR (Interquartile Range) method

Removed extreme salary values to improve data quality

## 7️⃣ Final Dataset Validation

Confirmed no missing values

Ensured no duplicate rows

Verified cleaned data is ready for Machine Learning

## 8️⃣ Save Cleaned Dataset

Saved the final cleaned dataset as:

##  customer_churn_cleaned.csv

##  Libraries Used

pandas

numpy

##  How to Run

Place customer_churn_messey.csv in the same directory as the notebook

Open day-3-assignment.ipynb in:

Jupyter Notebook / VS Code / Google Colab

Run all cells to generate the cleaned dataset

##  Output

Final cleaned dataset:

customer_churn_cleaned.csv

The dataset is now cleaned, structured, and ready for Machine Learning model training 
