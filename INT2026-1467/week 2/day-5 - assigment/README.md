# 📊 Customer Retention Analysis – t-Test

## 📌 Project Overview
This project analyzes **customer retention behavior** to test the hypothesis:

**Customers who receive promotional offers are more likely to return.**

Since a direct discount column is not available, the presence of promotional emails sent
(`esent`) is used as a proxy for discount exposure.

This analysis has been customized and executed as part of my **AI/ML internship assignments**.

---

## 📂 Dataset Information
- **Rows:** 30,801  
- **Columns:** 15  

### Key Columns Used
- `retained`  
  - `1` = Returned  
  - `0` = Not returned  

- `esent`  
  - `1` = Promotional email sent  
  - `0` = No promotion  

---

## 🧪 Methodology
- Customers were divided into two groups:
  - Customers who received promotional emails
  - Customers who did not receive promotional emails
- An **independent samples t-test (Welch’s t-test)** was performed.
- The t-test was implemented **manually using NumPy**, without relying on `scipy.stats`.

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
5. Interpret results at a 5% significance level  
6. Visualize retention rates using bar charts  

---

## ✅ Results & Conclusion
The analysis compares average retention rates between customers who received promotions
and those who did not. Based on the calculated p-value, we determine whether the difference
in retention rates is statistically significant.

This provides valuable insights into the effectiveness of promotional strategies.

---

## 📁 Project Structure
```
week-2/
└── day-x-assignment-x/
    ├── Customer_Retention_Custom_Rawal_Vipul.ipynb
    ├── data.csv
    └── README.md
```

---

## 👤 Author
**Rawal Vipul**  
AI / ML Intern

---