# 📊 Customer Retention Analysis – t-Test

## 📌 Project Overview

This project analyzes customer retention behavior to test the hypothesis:

**Customers who received a discount are more likely to return.**

Since the dataset does not contain a direct discount column, promotional emails sent (`esent`) are used as a proxy for discount exposure.

---

## 📂 Dataset Information

- **Rows:** 30,801  
- **Columns:** 15  

### Key Columns Used

- `retained` → Customer retention status  
  - `1` = Returned  
  - `0` = Not returned  

- `esent` → Promotional email sent  
  - `1` = Promotion sent  
  - `0` = No promotion  

---

## 🧪 Methodology

- Customers were divided into two groups:
  - Customers who received promotional emails
  - Customers who did not receive promotional emails
- An **independent samples t-test (Welch’s t-test)** was performed.
- The t-test was implemented **manually using NumPy**, without using `scipy.stats`.

---

## ⚙️ Tools & Libraries

- Python  
- Pandas  
- NumPy  
- Matplotlib  

---

## 📈 Analysis Steps

1. Load and explore the dataset  
2. Split customers based on promotion status  
3. Calculate mean retention rates  
4. Compute t-statistic and p-value manually  
5. Interpret results using a 5% significance level  
6. Visualize retention rates using a bar chart  

---

## ✅ Results & Conclusion

The analysis compares the average retention rates of customers who received promotions versus those who did not. Based on the calculated p-value, we determine whether the difference in retention is statistically significant.

This helps understand the impact of promotional strategies on customer retention.

---

## 📁 Files Included

- `Customer_retention.ipynb` → Jupyter Notebook containing full analysis  
- `data.csv` → Dataset used for analysis  

---

## 📌 Author

**Shaik Ansar**
AI/ML Intern @ Cepia Labs
---