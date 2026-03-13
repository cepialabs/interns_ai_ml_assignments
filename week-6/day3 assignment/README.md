# MNIST Digit Classification using Neural Networks

## 📌 Project Overview

This project demonstrates how to train a **Neural Network model** to classify handwritten digits using the **MNIST dataset**. The model is built using **TensorFlow/Keras** and trained with **Categorical Cross Entropy loss** and the **Adam optimizer**.

The goal of this assignment is to understand how **loss functions and optimizers help train neural networks effectively**.

---

## 📊 Dataset

The **MNIST dataset** is a widely used benchmark dataset in machine learning for handwritten digit recognition.

* Total images: **70,000**
* Training images: **60,000**
* Testing images: **10,000**
* Image size: **28 × 28 pixels**
* Number of classes: **10 (digits 0–9)**

Dataset source:
https://keras.io/api/datasets/mnist/

---

## ⚙️ Technologies Used

* Python
* TensorFlow / Keras
* NumPy
* Matplotlib
* Jupyter Notebook

---

## 🧠 Model Architecture

The neural network consists of the following layers:

1. **Flatten Layer**

   * Converts 28×28 image into a 1D vector

2. **Dense Layer (128 neurons)**

   * Activation: ReLU

3. **Dense Layer (64 neurons)**

   * Activation: ReLU

4. **Output Layer (10 neurons)**

   * Activation: Softmax

---

## 📉 Loss Function

The model uses **Categorical Cross Entropy** as the loss function.

It measures the difference between the **true label distribution** and the **predicted probability distribution**.

Lower loss indicates better model predictions.

---

## ⚡ Optimizer

The **Adam optimizer** is used to update the model weights during training.

Advantages:

* Faster convergence
* Adaptive learning rate
* Widely used in deep learning models

---

## 🚀 Model Training

Training parameters:

* Optimizer: **Adam**
* Loss Function: **Categorical Cross Entropy**
* Epochs: **10**
* Batch Size: **32**

During training, the model learns patterns in handwritten digits and reduces the loss over time.

---

## 📈 Results

After training the model:

* Test Accuracy: **~97–98%**
* Training loss decreases steadily with each epoch.

Example training trend:

Epoch 1 → Loss ~0.35
Epoch 5 → Loss ~0.15
Epoch 10 → Loss ~0.08

---


