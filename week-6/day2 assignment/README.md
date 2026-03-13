# Neural Network Activation Functions Comparison

## Overview

This assignment demonstrates the implementation of two neural network models using different activation functions: **ReLU (Rectified Linear Unit)** and **Sigmoid**. The objective is to train both models on a binary classification dataset and compare their training performance.

Activation functions play a crucial role in neural networks by introducing non-linearity, enabling models to learn complex patterns from data.

---

## Objectives

* Understand the purpose of activation functions in neural networks
* Implement neural network models using **ReLU** and **Sigmoid** activation functions
* Train both models on a dataset
* Compare the training performance of both models

---

## Dataset

The project uses the **Breast Cancer Wisconsin Dataset**, which is available in the **scikit-learn library**.

Dataset characteristics:

* 569 samples
* 30 numerical features
* Binary classification problem

Target Classes:

* **0 → Malignant (Cancerous)**
* **1 → Benign (Non-cancerous)**

The dataset is loaded directly using:

```python
from sklearn.datasets import load_breast_cancer
```

---

## Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* TensorFlow / Keras
* Jupyter Notebook

---

## Project Workflow

### 1. Import Libraries

Required libraries for data processing, visualization, and neural network modeling are imported.

### 2. Load Dataset

The Breast Cancer dataset is loaded from the scikit-learn library.

### 3. Data Preprocessing

* Split dataset into training and testing sets
* Normalize data using **StandardScaler**

### 4. Build Neural Network Models

Two models are created:

#### Model 1: ReLU Activation

* Hidden layers use **ReLU**
* Output layer uses **Sigmoid**

#### Model 2: Sigmoid Activation

* Hidden layers use **Sigmoid**
* Output layer uses **Sigmoid**

### 5. Model Training

Both models are trained for multiple epochs to evaluate performance.

### 6. Performance Comparison

Training loss and accuracy are compared using visualization.

---

## Results

| Model   | Activation Function | Training Speed | Performance                        |
| ------- | ------------------- | -------------- | ---------------------------------- |
| Model 1 | ReLU                | Faster         | Better convergence                 |
| Model 2 | Sigmoid             | Slower         | May suffer from vanishing gradient |

### Conclusion

The **ReLU activation function** generally provides better performance for hidden layers because it helps prevent the **vanishing gradient problem** and allows faster training compared to the Sigmoid function.

--