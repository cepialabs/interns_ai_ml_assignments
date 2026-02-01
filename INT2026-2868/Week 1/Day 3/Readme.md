Day 3 : Assignment 3

## 📂 Dataset Issues Addressed
The raw dataset contains the following problems:

- Missing values in the `age` column
- Duplicate records
- Inconsistent gender formats (e.g., `M`, `male`, `F`, `female`)

## 🛠️ Tools Used
- Python 3
- pandas
- NumPy

## 🧹 Data Cleaning Steps

### 1️⃣ Remove Duplicate Rows
Duplicate records were removed to avoid bias in training data.

### 2️⃣ Handle Missing Age Values
- Missing `age` values were filled using the **median**
- Median is chosen for robustness against outliers

### 3️⃣ Standardize Gender Values
- Converted values to lowercase
- Mapped all variations to:
  - `male`
  - `female`
- Rows with unknown gender values were removed

### 5️⃣ Export Clean Dataset
- Saved the cleaned data as:
