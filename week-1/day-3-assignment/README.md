\# DAY 3 ASSIGNMENT — Customer Churn Data Cleaning  

\*\*Intern ID:\*\* INT2026-1462  

\*\*Date:\*\* 21-01-2026  



---



\## 📌 Objective

The objective of this assignment is to clean the \*\*Customer Churn (Messy Dataset)\*\* and make it ready for \*\*Machine Learning\*\*.



The dataset contains:

\- Missing age values  

\- Duplicate rows  

\- Inconsistent gender formats  

\- Salary outliers  



---



\## 📂 Dataset Details

\- \*\*Dataset Name:\*\* Customer Churn (Messy Dataset)  

\- \*\*File Name:\*\* `customer\_churn\_messey.csv`



---



\## ✅ Files Submitted

\- `day-3-assignment.ipynb`  

\- `customer\_churn\_messey.csv`  

\- `customer\_churn\_cleaned.csv` \*(generated after cleaning)\*  



---



\## 🧹 Data Cleaning Steps Performed



\### 1) Load Dataset

\- Loaded the dataset using \*\*Pandas\*\*

\- Displayed first few rows to understand the structure



\### 2) Basic Data Understanding

\- Checked dataset shape, column names, and data types  

\- Viewed summary statistics for numeric and categorical features  



\### 3) Handle Missing Values

\- Identified missing values in the dataset  

\- Filled missing values in \*\*Age\*\* column using \*\*median\*\*



\### 4) Remove Duplicate Rows

\- Checked duplicate records  

\- Removed duplicates to avoid repeated data



\### 5) Clean Gender Column

\- Standardized gender values into:

&nbsp; - `male`

&nbsp; - `female`

\- Fixed inconsistent formats like:

&nbsp; - `M`, `m`, `Male`

&nbsp; - `F`, `f`, `Female`



\### 6) Handle Salary Outliers

\- Detected salary outliers using \*\*IQR (Inter Quartile Range)\*\* method  

\- Removed outlier rows to improve data quality



\### 7) Final Dataset Validation

\- Confirmed dataset is clean  

\- Verified no missing values and duplicates after cleaning  

\- Prepared final dataset for Machine Learning



\### 8) Save Cleaned Dataset

\- Saved cleaned dataset as:  

&nbsp; ✅ `customer\_churn\_cleaned.csv`



---



\## 🛠️ Libraries Used

\- `pandas`  

\- `numpy`  



---



\## ▶️ How to Run

1\. Keep `customer\_churn\_messey.csv` in the same folder as the notebook  

2\. Open `day-3-assignment.ipynb` in Jupyter Notebook / VS Code / Google Colab  

3\. Run all cells to generate the cleaned dataset  



---



\## ✅ Output

Final cleaned dataset file:

\- `customer\_churn\_cleaned.csv`



This dataset is now ready for \*\*Machine Learning model training\*\*.

