Week 3 : Day 3 : Assignment 3
## Overview

This assignment demonstrates basic machine learning models using
**Python and scikit-learn**:

1.  Spam Email Classification
    -   K-Nearest Neighbors (KNN)
    -   Decision Tree Classifier
2.  Housing Price Prediction
    -   Decision Tree Regressor

------------------------------------------------------------------------

## 1. Spam Email Classification

### Models Used

-   KNN with word count features
-   Decision Tree Classifier

### Features

-   Text is converted into numerical features using `CountVectorizer`.

------------------------------------------------------------------------

## 2. Housing Price Prediction

### Dataset

**File:** `housing.csv`

**Columns:** - `sqft` : Square footage - `bedrooms` : Number of
bedrooms - `location` : Area/location - `price` : House price (target)

### Model Used

-   Decision Tree Regressor

### Features

-   Numerical: sqft, bedrooms
-   Categorical: location (One-Hot Encoded)

------------------------------------------------------------------------

## Requirements

Install the required libraries using:

``` bash
pip install pandas scikit-learn
```

------------------------------------------------------------------------

## Learning Outcomes

-   Understand text feature extraction
-   Apply KNN and Decision Trees
-   Perform classification and regression tasks
-   Evaluate ML models

------------------------------------------------------------------------

## Author
Gunjan Damade