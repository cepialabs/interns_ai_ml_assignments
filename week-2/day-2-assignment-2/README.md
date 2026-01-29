# 📧 Email Marketing Campaign – Probability & Conversion Analysis

## 📌 Project Overview

This project analyzes an **email marketing campaign** using **probability and conditional probability concepts** to understand user behavior across three stages:

* 📬 Email Opened
* 🖱️ Email Clicked
* 💰 User Converted

The goal is to answer important business questions like:

* What is the **probability that a user clicks** an email?
* What is the **probability that a user converts given they clicked**?
* How much does **clicking influence conversion**?
* Can we represent this using **Conditional Probability Tables and Visualizations**?

---

## 🎯 Objectives

* Build or load an email marketing dataset
* Compute:

  * Probability of Click
  * Probability of Conversion given Click
  * Probability of Conversion given No Click
* Create a **Conditional Probability Table (CPT)**
* Visualize:

  * Click distribution
  * Conversion probability based on click behavior
* Draw **business insights** from the analysis

---

## 🗂️ Dataset Description

The dataset contains simulated user interaction data with the following columns:

| Column Name | Description                                                    |
| ----------- | -------------------------------------------------------------- |
| `opened`    | Whether the user opened the email (1 = Yes, 0 = No)            |
| `clicked`   | Whether the user clicked the link (1 = Yes, 0 = No)            |
| `converted` | Whether the user completed a purchase/action (1 = Yes, 0 = No) |

---

## 🛠️ Technologies Used

* Python 🐍
* Pandas
* NumPy
* Matplotlib
* Jupyter Notebook / Kaggle Notebook

---

## 📊 Key Analysis Performed

### 1️⃣ Probability Calculations

* **P(Click)** = Probability that a user clicks the email
* **P(Convert | Click)** = Probability that user converts given they clicked
* **P(Convert | No Click)** = Probability that user converts without clicking

---

### 2️⃣ Conditional Probability Table (CPT)

A conditional probability table is generated using:

```python
pd.crosstab(clicked, converted, normalize="index")
```

This shows conversion probabilities **based on click behavior**.

---

### 3️⃣ Visualizations

* 📊 Bar chart for **Click vs No Click distribution**
* 📊 Bar chart for **Conversion Probability given Click**

---

## 📈 Results & Insights

* ✅ Only a fraction of users click the email.
* ✅ Users who click are **far more likely to convert**.
* ❌ Users who do not click almost never convert.
* 📌 Clicking is a **strong indicator of purchase intent**.
* 🚀 Improving subject lines, CTA buttons, and email content can significantly increase conversions.

---

## 📁 Project Structure

```
📦 Email-Marketing-Campaign
 ┣ 📜 Email-marketing-campaign.ipynb
 ┣ 📜 README.md
```

---

## ▶️ How To Run

1. Open the notebook in **Jupyter / Kaggle / Colab**
2. Run all cells step by step
3. Observe:

   * Printed probabilities
   * Conditional probability table
   * Visualizations
4. Use insights for your report / PPT / submission

---

## 💼 Business Use Case

This analysis helps marketing teams:

* Understand **funnel performance**
* Identify **where users drop off**
* Optimize **email strategies for higher ROI**
* Focus efforts on increasing **click-through rate**

---

## 👨‍💻 Author

**Krushna Chandra Bindhani**
Data Science & Machine Learning Intern

---