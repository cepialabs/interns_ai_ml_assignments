# 🎓 Student Performance Data Visualization

## 📌 Project Overview

This project performs **exploratory data analysis (EDA)** and **data visualization** on a Student Performance dataset to understand:

- How student scores are distributed
- How gender affects performance
- How different subjects are correlated
- How attendance impacts academic performance

This project is part of my **Data Science / Data Visualization internship assignment**.

---

## 📂 Dataset Information

**File:** `student_performance_dataset.csv`

**Columns:**

- `student_id` → Unique student ID  
- `gender` → Male / Female  
- `math_score` → Math marks (0–100)  
- `science_score` → Science marks (0–100)  
- `english_score` → English marks (0–100)  
- `attendance` → Attendance percentage  

The dataset contains **200 students** with realistic, logically correlated data.

---

## 🛠️ Technologies Used

- Python 🐍
- Pandas → Data handling
- Matplotlib → Basic visualization
- Seaborn → Advanced visualization
- Jupyter Notebook / VS Code

---

## 📁 Project Structure

```

student-performance-analysis/
│
├── student_performance_dataset.csv
├── data-visualization.ipynb
└── README.md

```

---

## 📊 Tasks Performed

### ✅ 1. Score Distribution Plot
- Visualized distribution of student marks using **histogram**
- Helps understand overall performance spread

### ✅ 2. Gender vs Performance Chart
- Compared **average scores of male and female students**
- Used **bar chart**

### ✅ 3. Correlation Heatmap
- Found relationships between:
  - Math, Science, English scores
  - Attendance
- Used **Seaborn heatmap**

### ✅ 4. Attendance vs Score Trend Chart
- Analyzed impact of **attendance on performance**
- Used **scatter plot + trend analysis**

### ✅ 5. Pairplot (EDA)
- Visualized relationships between multiple numerical features

---

## 🚀 How To Run This Project

### 1️⃣ Install dependencies

```bash
pip install pandas matplotlib seaborn
```

### 2️⃣ Open the notebook

```bash
jupyter notebook
```

Open:

```
data-visualization.ipynb
```

### 3️⃣ Run all cells

---

## 📈 Key Insights

* Students with **higher attendance generally score higher**
* All subjects show **positive correlation** with each other
* Female students have slightly **higher average performance** in this dataset
* Performance distribution shows **most students score between 60–90**

---

## 🎯 Learning Outcomes

* Learned Exploratory Data Analysis (EDA)
* Learned how to:

  * Use Pandas for analysis
  * Use Matplotlib & Seaborn for visualization
  * Interpret graphs and patterns
* Understood how data visualization helps in **decision making**

---

## 👨‍💻 Author

**Krushna Chandra Bindhani**
Intern / Data Science Enthusiast