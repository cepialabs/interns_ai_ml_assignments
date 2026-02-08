# 🏠 House Price Prediction & 🧑‍🤝‍🧑 Customer Segmentation (ML Project)

This repository contains two complete Machine Learning projects:

1. **House Price Prediction (Supervised Regression)**
2. **Customer Segmentation (Unsupervised Clustering)**

Both projects are implemented in Jupyter Notebooks with full preprocessing, model building, evaluation, and visualization.

---

## 📂 Projects Included

### ✅ 1) House Price Prediction (Regression)
**Goal:** Predict house prices using supervised machine learning.

- Dataset Type: Housing dataset
- ML Type: Supervised Learning
- Task: Regression
- Target Column: House Price (e.g., `price` / `SalePrice`)

#### 🔍 Steps Performed
- Loaded and inspected dataset
- Handled missing values using **SimpleImputer**
- Converted categorical features using **OneHotEncoder**
- Built preprocessing + model pipeline using **ColumnTransformer + Pipeline**
- Trained multiple regression models:
  - Linear Regression
  - Random Forest Regressor
- Evaluated models using:
  - MAE (Mean Absolute Error)
  - RMSE (Root Mean Squared Error)
  - R² Score
- Visualized results (Actual vs Predicted)

---

### ✅ 2) Customer Segmentation (Clustering)
**Goal:** Group customers based on purchase behavior using unsupervised learning.

- Dataset Type: Customer segmentation dataset
- ML Type: Unsupervised Learning
- Task: Clustering
- Model Used: KMeans Clustering

#### 🔍 Steps Performed
- Loaded and inspected dataset
- Removed ID-like columns (CustomerID, Name, Email etc.)
- Handled missing values using **SimpleImputer**
- Encoded categorical features using **OneHotEncoder**
- Scaled numeric features using **StandardScaler**
- Determined best number of clusters using:
  - Elbow Method (Inertia)
  - Silhouette Score
- Built final KMeans model with best K
- Visualized clusters using PCA (2D plot)
- Generated cluster counts and cluster summary

---

## 🛠️ Technologies Used
- Python
- Jupyter Notebook
- Pandas, NumPy
- Matplotlib
- Scikit-learn

---

## 📁 Repository Structure

```

📦 ML-Regression-Clustering
┣ 📜 Housing.ipynb
┣ 📜 Customer_segmentation.ipynb
┣ 📜 housing.csv                  # (Add your dataset here)
┣ 📜 customers.csv                # (Add your dataset here)
┗ 📜 README.md

```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone <your-repo-link>
cd <your-repo-folder>
```

### 2️⃣ Install required libraries

```bash
pip install pandas numpy matplotlib scikit-learn
```

### 3️⃣ Run Jupyter Notebook

```bash
jupyter notebook
```

---

## ▶️ How to Run the Project

### 🏠 House Price Prediction

1. Place your housing dataset as:

   * `housing.csv`
2. Open:

   * `Housing.ipynb`
3. Run all cells.

---

### 🧑‍🤝‍🧑 Customer Segmentation

1. Place your customer dataset as:

   * `customers.csv`
2. Open:

   * `Customer_segmentation.ipynb`
3. Run all cells.

---

## 📊 Output / Results

### 🏠 Regression Output

* Model comparison table with MAE, RMSE, R²
* Best-performing model selection
* Actual vs Predicted price plot

### 🧑‍🤝‍🧑 Clustering Output

* Elbow Method plot (Inertia vs K)
* Silhouette Score plot
* Final cluster assignments
* PCA cluster visualization
* Cluster summary table

---

## 🚀 Future Improvements

* Add Hyperparameter Tuning (GridSearchCV / RandomizedSearchCV)
* Add more regression models (XGBoost, Gradient Boosting)
* Improve customer cluster interpretation using business labels
* Deploy both projects using Streamlit

---

## 👤 Author

**Swati M Patil**

---