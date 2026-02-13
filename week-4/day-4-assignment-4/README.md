# 📧 Spam Email Classification using Cross Validation (Logistic Regression vs Random Forest)

This project performs **Spam Email Classification** using Machine Learning.
It compares two models:

* **Logistic Regression**
* **Random Forest Classifier**

Both models are evaluated using **K-Fold Cross Validation (5-fold / 10-fold)** to measure:

✅ Model Stability
✅ Generalization Performance
✅ Metric Consistency across folds

---

## 📌 Dataset Used

* **File:** `emails.csv`
* **Columns:**

  * `text` → Email content (input feature)
  * `spam` → Label (target)

    * `1` = Spam
    * `0` = Not Spam (Ham)

---

## 🎯 Task Objectives

### ✔️ 1. Apply K-Fold Cross Validation

* Use **5-fold or 10-fold Stratified Cross Validation**
* Ensure balanced spam/ham distribution in each fold

### ✔️ 2. Train and Evaluate Models

* Logistic Regression
* Random Forest

### ✔️ 3. Compare Performance Metrics

For each model, compute:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score

### ✔️ 4. Document Insights

* Compare mean scores
* Compare standard deviation (std)
* Conclude which model is more stable and generalizes better

---

## ⚙️ Libraries Used

* pandas
* numpy
* scikit-learn

---

## 🧠 Approach Used

### 🔹 Step 1: Text Vectorization

Since ML models cannot directly understand raw text, we use:

✅ **TF-IDF Vectorizer**

It converts email text into numerical feature vectors.

---

### 🔹 Step 2: Cross Validation

We use **StratifiedKFold** because the dataset is imbalanced (spam vs ham).

This ensures each fold has a similar spam/ham ratio.

---

### 🔹 Step 3: Model Training and Evaluation

Each fold trains on training split and evaluates on validation split.

Finally, mean and standard deviation across folds are calculated.

---

## 📊 Evaluation Metrics

| Metric    | Meaning                                   |
| --------- | ----------------------------------------- |
| Accuracy  | Overall correct predictions               |
| Precision | How many predicted spam are actually spam |
| Recall    | How many actual spam emails were detected |
| F1 Score  | Balance of Precision & Recall             |
| ROC-AUC   | Probability-based ranking performance     |

---

## 🚀 How to Run the Project

### ✅ 1. Install dependencies

```bash
pip install pandas numpy scikit-learn
```

### ✅ 2. Run the Notebook

Open and run:

📌 `assignment-4.ipynb`

---

## 🧪 Cross Validation Setup

You can switch between 5-fold and 10-fold:

### 5-Fold CV

```python
StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
```

### 10-Fold CV

```python
StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
```

---

## 📌 Results Interpretation

After running CV, we compare:

### 🔹 Mean Score

* Higher mean → better overall performance

### 🔹 Standard Deviation (std)

* Lower std → more stable model
* Higher std → model performance varies across folds

---

## 📝 Insights (Example)

* Logistic Regression usually performs better on TF-IDF sparse text data.
* Random Forest may perform slightly worse due to high-dimensional sparse features.
* The model with higher mean F1 and lower std is considered:
  ✅ more stable
  ✅ better generalized

---

## ✅ Final Conclusion

The best model is selected based on:

* Higher F1 Score and ROC-AUC
* Lower variation across folds (std)

---

## 📁 Project Files

| File Name            | Description                              |
| -------------------- | ---------------------------------------- |
| `emails.csv`         | Dataset used                             |
| `assignment-4.ipynb` | Notebook with training + CV + evaluation |
| `README.md`          | Project documentation                    |

---

## 👨‍💻 Author

**Krushna Chandra Bindhani**
