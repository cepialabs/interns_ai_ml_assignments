

# 🧠 Simple Neural Network using TensorFlow

## 📌 Project Overview

This project demonstrates how to build a **simple neural network with one hidden layer** using **TensorFlow and Keras**.
The model learns to predict whether a student will **pass or fail based on the number of hours studied**.

The objective of this project is to understand the **basic structure and working of neural networks**, including **forward propagation, backpropagation, and model training**.

---

## 🎯 Project Objective

* Understand the **structure of a neural network**
* Implement a **model with an input layer, hidden layer, and output layer**
* Train the neural network using a simple dataset
* Make predictions using the trained model
* Explain how **data flows from input to output during training**

---

## 🏗 Neural Network Architecture

The model consists of:

| Layer        | Description                             |
| ------------ | --------------------------------------- |
| Input Layer  | Receives the input data (hours studied) |
| Hidden Layer | 5 neurons with ReLU activation          |
| Output Layer | 1 neuron with Sigmoid activation        |

Structure:

```
Input Layer (1 neuron)
        ↓
Hidden Layer (5 neurons, ReLU)
        ↓
Output Layer (1 neuron, Sigmoid)
```

---

## 📊 Dataset

A simple dataset is used for training.

| Hours Studied | Result |
| ------------- | ------ |
| 1             | Fail   |
| 2             | Fail   |
| 3             | Fail   |
| 4             | Pass   |
| 5             | Pass   |

Where:

* **0 = Fail**
* **1 = Pass**

---

## ⚙️ Technologies Used

* **Python**
* **TensorFlow**
* **Keras**
* **NumPy**
* **Jupyter Notebook**

---

## 🚀 How the Model Works

### 1️⃣ Input Layer

The input layer receives the number of **hours studied**.

### 2️⃣ Forward Propagation

The input is passed to the hidden layer where neurons perform:

```
Z = W * X + b
```

Then the **ReLU activation function** is applied.

### 3️⃣ Hidden Layer

The hidden layer extracts patterns from the input data.

### 4️⃣ Output Layer

The output layer uses a **sigmoid activation function** to produce a probability between **0 and 1**.

### 5️⃣ Loss Calculation

The model compares predicted values with actual values using **Binary Crossentropy Loss**.

### 6️⃣ Backpropagation

The model updates weights using the **Adam optimizer** to reduce prediction error.

---

## 🧪 Model Training

The neural network is trained for **100 epochs** to improve accuracy.

Example training output:

```
Epoch 100/100
accuracy: 0.60
loss: 0.95
```

---

## 🔮 Prediction Example

Input:

```
Hours studied = 3
```

Model prediction:

```
[[0.2969]]
```

Interpretation:

Since **0.2969 < 0.5**, the model predicts:

```
Fail
```

## 📚 Learning Outcomes

Through this project, we learned:

* Basics of **Deep Learning**
* Structure of **Artificial Neural Networks**
* Difference between **Machine Learning and Deep Learning**
* Implementation of **hidden layers and activation functions**
* Concept of **forward propagation and backpropagation**

---

## 📌 Conclusion

This project successfully demonstrates how to build and train a **simple neural network** using TensorFlow.
Even with a small dataset, the model learns patterns and predicts outcomes based on input values.

This project helps in understanding the **fundamental concepts of neural networks and deep learning**.

---

