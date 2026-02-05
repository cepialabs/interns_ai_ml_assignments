# 🏠📧 Housing Price Prediction & Spam Email Classification

## 📌 Project Overview
This project demonstrates **supervised machine learning** using two real‑world datasets:
1. **Housing Price Prediction** using regression  
2. **Spam Email Classification** using classification algorithms  

The project shows how ML models work with **numerical data** and **text data**.

---

## 📂 Datasets Used

### 🏠 Housing Dataset
Used to predict house prices based on property features.

**Features:**
- Area
- Bedrooms
- Bathrooms
- Stories
- Parking
- Air conditioning
- Furnishing status

**Target Variable:**
- `price`

**Algorithm Used:** Linear Regression

---

### 📧 Spam Email Dataset
Used to classify emails as **spam** or **not spam**.

**Data:**
- Email text
- Labels:  
  - `0` → Ham (Not Spam)  
  - `1` → Spam  

Text is converted into numerical features using **Bag of Words (CountVectorizer)**.

**Algorithms Used:**
- K‑Nearest Neighbors (KNN)
- Decision Tree

---

## 🧠 Machine Learning Techniques
- Supervised Regression
- Supervised Classification
- Text Feature Extraction
- Model Training and Evaluation

---

## 🛠 Tools & Libraries
- Python
- Pandas
- NumPy
- Scikit‑learn

---

## ▶️ How to Run
```bash
python housing_and_email_ml.py
