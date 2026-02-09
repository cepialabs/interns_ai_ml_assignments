# 📧 Spam Email Classification (KNN & Decision Tree)

**Author:** Rawal Vipul  
**Program:** AI / ML Internship

---

## 📌 Project Overview
This project builds a **Spam Email (SMS) Classification system** using supervised machine learning.
Messages are classified into:

- **HAM (Not Spam)** ✅
- **SPAM** 🚨

Two different models are trained and compared to evaluate performance.

---

## 🎯 Objectives
- Load and clean the SMS spam dataset
- Convert text messages into numerical features using **TF-IDF**
- Train **K-Nearest Neighbors (KNN)** classifier
- Train **Decision Tree** classifier
- Evaluate models using accuracy, confusion matrix, and classification report
- Test the model on custom user messages

---

## 📂 Dataset Information
- **File Name:** `mail.csv`
- **Encoding:** `windows-1252`

### Important Columns
| Column | Description |
|------|-------------|
| v1 | Label (`ham` / `spam`) |
| v2 | Message text |

Extra unnamed columns are removed during preprocessing.

---

## 🛠️ Tools & Libraries
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

---

## 📊 Models Used
### 1️⃣ KNN Classifier
Classifies messages based on similarity with neighboring data points.

### 2️⃣ Decision Tree Classifier
Uses rule-based splitting to classify spam and ham messages.

---

## 📈 Evaluation Metrics
- Accuracy Score
- Confusion Matrix
- Precision, Recall, F1-score

---

## 📁 Project Structure
```
week-x/
└── day-x-assignment-x/
    ├── Spam_Email_Custom_Rawal_Vipul.ipynb
    ├── mail.csv
    └── README.md
```

---

## ▶️ How to Run
1. Install dependencies:
   ```bash
   pip install pandas numpy scikit-learn matplotlib
   ```
2. Launch Jupyter Notebook and open:
   ```
   Spam_Email_Custom_Rawal_Vipul.ipynb
   ```

---

## 👤 Author
**Rawal Vipul**  
AI / ML Intern