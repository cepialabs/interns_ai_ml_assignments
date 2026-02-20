# 📊 Customer Churn Data Cleaning (Machine Learning Ready)

## 🧠 Project Overview

This project focuses on **cleaning a messy real-world Customer Churn dataset** and preparing it for **machine learning**.

In real-life data science projects, data is often:

* Incomplete ❌
* Inconsistent ❌
* Contains duplicates ❌
* Contains outliers ❌

This project demonstrates **how to fix all of these problems using Python & Pandas**.

---

## 📁 Dataset Files

* 📄 `customer_churn_messy.csv` → Original messy dataset
* 📄 `customer_churn_cleaned.csv` → Cleaned, ML-ready dataset
* 📓 `pandas.ipynb` → Jupyter Notebook with full cleaning steps

---

## 🧨 Problems in the Original Dataset

The dataset intentionally contains the following issues:

| Problem                 | Example                              |
| ----------------------- | ------------------------------------ |
| Missing values          | Age column has NaN values            |
| Duplicate rows          | Same customer appears more than once |
| Inconsistent categories | Gender = Male, M, FEMALE, f, etc     |
| Outliers                | Salary has extremely large values    |
| Categorical data        | Gender and Churn are not numeric     |

---

## 🛠️ Cleaning Steps Performed

### ✅ 1. Load Dataset

```python
df = pd.read_csv("customer_churn_messy.csv")
```

### ✅ 2. Remove Duplicate Rows

```python
df = df.drop_duplicates()
```

### ✅ 3. Handle Missing Values

* Filled missing **Age** values using **mean imputation**

```python
df["Age"] = df["Age"].fillna(df["Age"].mean())
```

### ✅ 4. Fix Inconsistent Gender Values

* Converted all to lowercase
* Replaced `m` → `male`, `f` → `female`

```python
df["Gender"] = df["Gender"].str.lower().replace({"m":"male", "f":"female"})
```

### ✅ 5. Remove Salary Outliers (Using IQR Method)

```python
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)
IQR = Q3 - Q1

df = df[(df["Salary"] >= Q1 - 1.5*IQR) & (df["Salary"] <= Q3 + 1.5*IQR)]
```

### ✅ 6. Encode Categorical Columns

```python
df["Gender"] = df["Gender"].map({"male":0, "female":1})
df["Churn"] = df["Churn"].map({"No":0, "Yes":1})
```

### ✅ 7. Feature Scaling

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df[["Age","Salary"]] = scaler.fit_transform(df[["Age","Salary"]])
```

---

## 📊 Final Output

✔ No missing values
✔ No duplicates
✔ No outliers
✔ All numeric columns
✔ Scaled features
✔ **100% Machine Learning Ready** 🚀

---

## 📌 Final Columns

```
CustomerID, Age, Gender, Salary, Churn
```

---

## ▶️ How To Run This Project

1. Clone the repository
2. Open `datacleaning.ipynb`
3. Run all cells
4. A cleaned file will be generated:

   ```
   customer_churn_cleaned.csv
   ```

---

## 🧪 Libraries Used

* Python
* Pandas
* NumPy
* Scikit-learn

---

## 🎯 Learning Outcomes

* Real-world data cleaning
* Handling missing values
* Removing duplicates
* Outlier detection (IQR)
* Encoding categorical variables
* Feature scaling
* Preparing data for ML

---
## 📌 Author

**Shaik Ansar**
AI/ML Intern @ Cepia Labs
---