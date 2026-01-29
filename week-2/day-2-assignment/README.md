# 📧 Email Marketing Campaign Analysis  
**Week 2 – Day 2 Assignment**  
**Date: 29 January 2026**

---

## 📌 Objective
The objective of this assignment is to analyze an **Email Marketing Campaign dataset** and calculate important probabilities related to user engagement and conversion behavior using conditional probability and visualizations.

---

## 📂 Dataset Description
The dataset contains user-level email interaction and transaction details.

### Columns Used:
- `sent_date` – Date when email was sent  
- `open_date` – Date when email was opened  
- `click_date` – Date when email link was clicked  
- `transaction_date` – Date when transaction occurred  
- `transaction_amount` – Amount spent by the user  

---

## 🧠 Key Concepts Covered
- Probability
- Conditional Probability
- Email marketing funnel analysis
- Data preprocessing
- Visualization using Matplotlib and Seaborn

---

## 📊 Tasks Performed

### 1️⃣ Probability that a User Opens an Email  
\[
P(Open) = \frac{\text{Number of emails opened}}{\text{Total emails sent}}
\]

---

### 2️⃣ Probability that a User Clicks an Email  
\[
P(Click) = \frac{\text{Number of emails clicked}}{\text{Total emails sent}}
\]

---

### 3️⃣ Probability that a User Converts Given They Clicked  
(Conditional Probability)

\[
P(Convert | Click) = \frac{\text{Users who clicked and converted}}{\text{Users who clicked}}
\]

---

### 4️⃣ Conditional Probability Table
A conditional probability table is created using a crosstab between:
- Clicked (Yes/No)
- Converted (Yes/No)

This helps understand conversion behavior after clicking.

---

### 5️⃣ Visualizations
- Conditional probability heatmap (Conversion given Click)
- Email marketing funnel bar chart:
  - Sent → Opened → Clicked → Converted

---

## 📈 Insights
- Open rate reflects the effectiveness of email subject lines
- Click rate shows how engaging the email content is
- Conversion given click evaluates landing page or offer quality
- Conditional probability clearly explains user behavior

---

## 🛠️ Tools & Libraries Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## 📁 Project Structure
Week-2/
│
├── Day-2-Assignment/
│ ├── email_marketing.csv
│ ├── week2day2assignment.ipynb
│ └── README.md



---

## ✅ Conclusion
This analysis helps understand user engagement and conversion patterns in an email marketing campaign using probability and conditional probability concepts, supported by clear visualizations.

---
