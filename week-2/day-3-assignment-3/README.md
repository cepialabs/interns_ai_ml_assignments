---

# 📊 Customer Purchase Amount Analysis using Probability & Distribution

## 📌 Project Overview

This project analyzes **customer purchase behavior** using **probability theory and statistical distributions**.
The goal is to understand spending patterns, calculate probabilities for high-value purchases, and compare **simulated sales data** with a **theoretical normal distribution**.

This type of analysis is commonly used in **marketing analytics, revenue forecasting, and customer segmentation**.

---

## 🎯 Objectives

* Visualize customer purchase amounts using a **histogram**
* Fit a **normal distribution** to real-world-like data
* Calculate the **probability of customers spending above a given threshold**
* Simulate random sales data and compare it with the **theoretical distribution**
* Apply statistical concepts in a practical business scenario

---

## 🗂️ Dataset Description

* **Type**: Simulated customer purchase data
* **Distribution**: Normal (Gaussian)
* **Number of customers**: 1000
* **Mean purchase amount**: ₹600
* **Standard deviation**: ₹120

> Negative purchase values were removed to maintain real-world constraints.

---

## 🛠️ Technologies & Libraries Used

* **Python**
* **NumPy** – numerical computations
* **Pandas** – data handling
* **Matplotlib** – data visualization
* **SciPy (stats)** – probability distributions & statistical analysis

---

## 📈 Key Steps Performed

### 1️⃣ Data Simulation

* Generated 1000 customer purchase values using a normal distribution.
* Ensured realistic data by removing negative values.

### 2️⃣ Data Visualization

* Plotted a **histogram** of purchase amounts.
* Overlaid a **fitted normal distribution curve**.

### 3️⃣ Probability Analysis

* Calculated the probability of a customer spending **above a specified threshold** using the cumulative distribution function (CDF).

### 4️⃣ Distribution Comparison

* Compared **simulated purchase data** with the **theoretical normal distribution**.
* Verified how closely the simulated data follows the expected statistical pattern.

---

## 📊 Output & Insights

* Most customers spend around the **average purchase value (₹600)**.
* A smaller percentage of customers make **high-value purchases**, which is crucial for:

  * Premium customer targeting
  * Marketing strategy optimization
  * Revenue forecasting

---

## ▶️ How to Run the Project

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/customer-purchase-analysis.git
   ```
2. Install required libraries:

   ```bash
   pip install numpy pandas matplotlib scipy
   ```
3. Open the notebook:

   ```bash
   jupyter notebook Untitled.ipynb
   ```
4. Run all cells to see visualizations and probability results.

---

## 📌 Use Cases

* Customer spending behavior analysis
* Marketing and sales strategy planning
* Business analytics & data science learning projects
* Internship and academic portfolio projects

---

## 🚀 Future Enhancements

* Use **real-world retail datasets**
* Add **customer segmentation**
* Perform **A/B testing simulations**
* Integrate with **machine learning models** for prediction

---

## 📌 Author

**Shaik Ansar**
AI/ML Intern @ Cepia Labs
---