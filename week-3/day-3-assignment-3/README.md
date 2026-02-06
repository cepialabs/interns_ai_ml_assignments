
---

# 📧 Spam Email Classification (KNN + Decision Tree)

This project builds a **Spam Email (SMS) Classifier** using Machine Learning.
It classifies messages as:

* **HAM (Not Spam)** ✅
* **SPAM** 🚨

Two ML models are trained and compared:

* **K-Nearest Neighbors (KNN)**
* **Decision Tree Classifier**

---

## 📌 Dataset Used

**File:** `mail.csv`
This dataset is a popular SMS spam dataset.

### Columns in Dataset

| Column             | Meaning                                        |
| ------------------ | ---------------------------------------------- |
| `v1`               | Label (`ham` or `spam`)                        |
| `v2`               | Message text                                   |
| `Unnamed: 2, 3, 4` | Extra empty columns (dropped in preprocessing) |

---

## 🎯 Project Objectives

* Load and clean the dataset
* Convert text emails/messages into numerical features using **TF-IDF**
* Train **KNN classifier**
* Train **Decision Tree classifier**
* Evaluate both models using:

  * Accuracy
  * Classification Report
  * Confusion Matrix
* Predict spam/ham for new custom messages

---

## 🧠 Machine Learning Models

### ✅ 1. KNN Classifier

* Uses nearest neighbors to classify a message based on similar messages.

### ✅ 2. Decision Tree Classifier

* Creates a tree structure based on word features to classify messages.

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib

---

## 📂 Project Files

| File               | Description                                     |
| ------------------ | ----------------------------------------------- |
| `Spam_email.ipynb` | Jupyter notebook containing full implementation |
| `mail.csv`         | Dataset file                                    |
| `README.md`        | Project documentation                           |

---

## 🚀 How to Run the Project

### 1️⃣ Install Required Libraries

Run this in terminal or Jupyter:

```bash
pip install pandas numpy scikit-learn matplotlib
```

---

### 2️⃣ Run the Notebook

Open Jupyter Notebook and run:

```bash
jupyter notebook
```

Then open:

✅ `Spam_email.ipynb`

---

## 🧹 Data Preprocessing Steps

* Load dataset using encoding: `windows-1252`
* Keep only useful columns: `v1` and `v2`
* Rename:

  * `v1 → label`
  * `v2 → text`
* Convert labels:

  * `ham → 0`
  * `spam → 1`
* Convert text into numerical features using:

  * **TF-IDF Vectorizer**
  * `max_features = 5000`

---

## 📊 Model Evaluation Metrics

Both models are evaluated using:

* **Accuracy Score**
* **Confusion Matrix**
* **Precision / Recall / F1-score**

---

## ✨ Example Prediction

The notebook also includes prediction for new messages like:

* `"Congratulations! You won a free iPhone. Click here!"` → **SPAM 🚨**
* `"Hey bro, are we meeting at 6pm today?"` → **HAM ✅**

---

## 📌 Results

At the end, the notebook compares:

* KNN Accuracy
* Decision Tree Accuracy

and shows a bar chart comparison.

---

## 📌 Future Improvements

* Use more models (Logistic Regression, Naive Bayes, SVM)
* Hyperparameter tuning using GridSearchCV
* Save the trained model as `.pkl` using joblib
* Deploy as a web app using Flask/Streamlit

---

## 👨‍💻 Author

**Krushna Chandra Bindhani**

---