# Handwritten Digit Recognition using MNIST

## 📌 Project Overview
This mini project builds a **Neural Network model** to recognize handwritten digits (0–9) using the **MNIST dataset**.  
The model is trained to classify images of digits and predict the correct number.

The MNIST dataset contains **70,000 grayscale images** of handwritten digits.  
Each image is **28 × 28 pixels**.

---

## 🎯 Objective
The objective of this project is to:
- Build a neural network model
- Train the model using the MNIST dataset
- Evaluate model performance
- Visualize predictions

---

## 🛠 Technologies Used
- Python
- Jupyter Notebook
- NumPy
- Matplotlib
- Scikit-learn
- Seaborn

---

## 📂 Dataset
Dataset used: **MNIST Handwritten Digits Dataset**

Features:
- 70,000 images
- 28x28 pixel grayscale images
- Digits from **0 to 9**

---

## ⚙️ Project Workflow

### 1️⃣ Import Libraries
Necessary Python libraries such as NumPy, Matplotlib, and Scikit-learn are imported.

### 2️⃣ Load Dataset
The MNIST dataset is loaded using `fetch_openml`.

### 3️⃣ Data Preprocessing
- Pixel values are normalized
- Dataset is split into **training and testing sets**

### 4️⃣ Model Building
A **Multi Layer Perceptron (MLP) Neural Network** is used for classification.

### 5️⃣ Model Training
The model is trained using the training dataset.

### 6️⃣ Model Evaluation
Accuracy and classification report are calculated to evaluate performance.

### 7️⃣ Visualization
- Sample digit images are displayed
- Predicted digits are visualized
- Confusion matrix is plotted

---

## 📊 Results
- The neural network successfully predicts handwritten digits.
- Model accuracy is typically around **95%+** depending on parameters.

---

## 📷 Example Output
The model predicts digits from the test dataset and displays the corresponding image.

Example:

Predicted Digit → **7**

---

## 🚀 How to Run the Project

1. Clone the repository
2. Open the notebook in **Jupyter Notebook or Google Colab**
3. Install required libraries

```
pip install numpy matplotlib scikit-learn seaborn
```

4. Run all cells in the notebook.

---

## 📌 Conclusion
This project demonstrates how **Neural Networks can be used for image classification**.  
The MNIST dataset is a standard benchmark dataset for learning **machine learning and deep learning concepts**.
