# 🏠📧 Housing Price Prediction & Spam Email Classification (Logistic Regression)

This repository contains **two machine learning tasks completed in Python**:

1. **Housing Price Prediction (Regression)** – predict house prices using numerical housing features  
2. **Spam Email Classification (Binary Classification)** – classify messages as **Spam / Not Spam** using **TF‑IDF + Logistic Regression**

Both projects are implemented in a single notebook:  
📌 `Housing_prices_&_Email_dataset.ipynb`

---

## 🚀 Projects Overview

### 1) Housing Price Prediction (Regression)
**Goal:** Predict the median house value using housing-related features such as crime rate, number of rooms, tax rate, etc.

**Dataset:** `house.csv`  
This dataset matches the classic **Boston Housing dataset** structure.

**Target Column:** `MEDV` (Median house value)

---

### 2) Spam Email / SMS Classification (Logistic Regression)
**Goal:** Predict whether a message is:
- `spam` (1)
- `ham` (0)

**Dataset:** `mail.csv`  
This dataset is the popular **SMS Spam Collection dataset** format.

**Model Used:** Logistic Regression  
**Text Vectorization:** TF‑IDF

---

## 📂 Folder Structure

```
.
├── Housing_prices_&_Email_dataset.ipynb   # Full notebook (both tasks)
├── house.csv                              # Housing dataset
├── mail.csv                               # Spam dataset
└── README.md                              # Project documentation
```

---

## 🧾 Dataset Details

### 🏠 Housing Dataset (`house.csv`)
**Rows:** 506  
**Columns:** 14

**Features Used:**
- CRIM
- ZN
- INDUS
- CHAS
- NOX
- RM
- AGE
- DIS
- RAD
- TAX
- PTRATIO
- B
- LSTAT

**Target:**
- `MEDV` → Median value of owner-occupied homes

---

### 📧 Spam Dataset (`mail.csv`)
**Rows:** 5572  
**Columns:** 2

**Columns Used:**
- `label` → spam / ham  
- `message` → raw text message  

---

## ⚙️ Tech Stack
- Python 3.x  
- Pandas, NumPy  
- Matplotlib  
- Scikit-learn  

---

## 🧠 ML Workflow (Both Tasks)

### ✅ Common Steps
- Load dataset  
- Basic EDA (shape, nulls, distributions)  
- Train-test split  
- Model training  
- Model evaluation  
- Visualizations + results  

---

## 🏠 Housing Regression: Models & Metrics

### Models Used
- **Linear Regression** (baseline)
- **Random Forest Regressor** (improved)

### Evaluation Metrics
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

---

## 📧 Spam Classification: Model & Metrics

### Model Used
- **TF‑IDF Vectorizer**
- **Logistic Regression**

### Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

---

## ▶️ How to Run (Local)

### 1) Install Dependencies
```bash
pip install numpy pandas matplotlib scikit-learn
```

### 2) Run Notebook
```bash
jupyter notebook
```

Open:
📌 `Housing_prices_&_Email_dataset.ipynb`

---

## 📌 Results (What you will see in notebook)

### Housing Prediction
- Model performance table (Linear vs Random Forest)
- Actual vs Predicted plot
- Feature importance graph (Random Forest)

### Spam Classification
- Classification report
- Confusion matrix
- Example predictions on custom messages

---

## ✅ Conclusion

- The **Random Forest model** generally performs better than Linear Regression for housing prediction.
- **TF‑IDF + Logistic Regression** provides strong results for spam detection and is a great baseline for text classification tasks.

---

## 👤 Author
**Swati M Patil**

---