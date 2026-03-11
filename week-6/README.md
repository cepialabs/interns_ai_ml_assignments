# Week 6 - Day 1 Assignment 1
**Date:** 11-03-2026  

## Build a Simple Neural Network with One Hidden Layer

This assignment demonstrates how to build a **simple neural network using Python and NumPy**.  
The network contains **one hidden layer** and is trained using **forward propagation and backpropagation**.

---

# Objective

The objective of this assignment is to:

- Build a **simple neural network**
- Use **at least one hidden layer**
- Understand how **data flows from input to output**
- Learn the **training process of neural networks**

---

# Neural Network Architecture

The neural network used in this project consists of three layers:

1. **Input Layer** – Receives the input data  
2. **Hidden Layer** – Processes the data using weights and activation functions  
3. **Output Layer** – Produces the final prediction  

### Structure

```
Input Layer (2 neurons)
        ↓
Hidden Layer (3 neurons)
        ↓
Output Layer (1 neuron)
```

---


# Technologies Used

- Python
- NumPy

```

---

# How Data Flows During Training

## 1. Input Layer
The dataset is given as input to the neural network.

Example:
```
[0,1]
```

---

## 2. Hidden Layer Processing

The inputs are multiplied with weights.

```
Hidden Input = Input × Weights
```

Then an activation function is applied.

```
Hidden Output = sigmoid(Hidden Input)
```

---

## 3. Output Layer

The hidden layer output is passed to the output layer.

```
Final Input = Hidden Output × Weights
```

Then sigmoid produces the prediction.

```
Predicted Output = sigmoid(Final Input)
```

---

## 4. Error Calculation

The predicted output is compared with the actual output.

```
Error = Actual Output − Predicted Output
```

---

## 5. Backpropagation

The error is propagated backward through the network to adjust the weights.

Steps:
1. Calculate gradient
2. Update output layer weights
3. Update hidden layer weights

---

## 6. Weight Update

Weights are updated using the learning rate.

```
New Weight = Old Weight + Learning Rate × Gradient
```

---

# Training Process

The following steps repeat many times:

1. Forward propagation  
2. Prediction  
3. Error calculation  
4. Backpropagation  
5. Weight update  

After many iterations, the neural network learns the correct pattern.

---

# Expected Output

After training, the neural network prints predicted values close to the expected output.

Example:

```
Predicted Output:
[[0.01]
 [0.98]
 [0.97]
 [0.02]]
```

---

# Learning Outcome

By completing this assignment we understand:

- Neural Network basics
- Role of hidden layers
- Forward propagation
- Backpropagation
- Training of neural networks

---
