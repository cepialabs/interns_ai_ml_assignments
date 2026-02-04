# Machine Learning Assignment
Sayantan Banerjee

INT2026-0885
##  Overview

This project contains two tasks based on Machine Learning techniques:

1. **Task 1 – Housing Price Prediction (Supervised Learning)**
2. **Task 2 – Customer Segmentation Based on Purchase Behaviour (Unsupervised Learning)**

Both tasks are implemented in Python using popular ML libraries such as **pandas, scikit-learn, and matplotlib**.

---

# ✅ TASK 1 — HOUSING PRICE PREDICTION (SUPERVISED LEARNING)

##  Objective
To build a regression model that predicts house prices based on various features such as area, number of rooms, and amenities.

##  Dataset
The housing dataset contains features like:

- Area  
- Bedrooms  
- Bathrooms  
- Stories  
- Main road access  
- Guest room  
- Basement  
- Hot water heating  
- Air conditioning  
- Parking  
- Preferred area  
- Furnishing status  
- **Target variable:** `price`

##  Methodology

1. Load the dataset  
2. Convert categorical values (`yes/no`, furnishing status) into numeric form  
3. Split data into training (80%) and testing (20%)  
4. Train **Linear Regression** model  
5. Evaluate using:
   - R² Score  
   - Mean Squared Error (MSE)

## result
The model successfully predicts house prices based on input features. Performance is measured using R² and MSE.

---

# ✅ TASK 2 — CUSTOMER SEGMENTATION (UNSUPERVISED LEARNING)

##  Objective  
To cluster customers into meaningful groups based on their purchase behaviour using **K-Means clustering**.

##  Dataset
The dataset contains 300 customers with the following features:

- CustomerID  
- Recency (days since last purchase)  
- Purchase Frequency  
- Monetary Value (total spend)  
- Average Order Value  

These features represent real-world **purchase behaviour analytics (RFM-style data).**

##  Methodology

1. Load the dataset  
2. Select purchase-behaviour features  
3. Standardize the data using **StandardScaler**  
4. Use **Elbow Method** to determine the optimal number of clusters  
5. Apply **K-Means clustering (k = 3)**  
6. Visualize clusters using scatter plots  

##  Result
Customers were grouped into three segments:

- **Cluster 0 – High-value loyal customers**  
- **Cluster 1 – Medium-value occasional buyers**  
- **Cluster 2 – Low-value inactive customers**

This helps businesses in targeted marketing and customer retention.

---

##  Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Jupyter Notebook  

---

