# MNIST Handwritten Digit Recognition (NumPy Implementation)

## Project Overview

This project implements a **handwritten digit recognizer for the MNIST dataset** using a **Neural Network built from scratch with NumPy**, without using deep learning libraries such as TensorFlow or PyTorch.

The model learns to classify grayscale images of handwritten digits (0–9) by training a **multi-layer neural network** using **forward propagation and backpropagation**.

This project demonstrates the **core concepts of neural networks**, including weight initialization, activation functions, loss calculation, and gradient descent.

---

# Dataset

The project uses the **MNIST dataset**, which contains images of handwritten digits.

Dataset characteristics:

* Total images: **70,000**
* Training images: **56,000**
* Testing images: **14,000**
* Image size: **28 × 28 pixels**
* Pixel values: **0–255 grayscale**

Each image is flattened into a **784-dimensional vector** before being passed into the neural network.

---

# Features

* Neural network implemented **from scratch using NumPy**
* No deep learning frameworks used
* Implements **ReLU activation**
* Uses **Softmax output layer**
* Includes **forward propagation**
* Implements **backpropagation and gradient descent**
* Visualizes predictions using **Matplotlib**
* Achieves **~92–95% accuracy**

---

# Project Structure

```
mnist-digit-recognizer/
│
├── mnist_numpy.py       # Main neural network implementation
├── README.md            # Project documentation
└── requirements.txt     # Required libraries
```

---

# Requirements

Install the required Python libraries before running the project.

```
pip install numpy matplotlib scikit-learn
```

Libraries used:

| Library      | Purpose                                           |
| ------------ | ------------------------------------------------- |
| NumPy        | Matrix operations and neural network calculations |
| Matplotlib   | Visualization of digit predictions                |
| Scikit-learn | Loading the MNIST dataset                         |

---

# Neural Network Architecture

The neural network consists of **three layers**.

```
Input Layer: 784 neurons
Hidden Layer 1: 128 neurons (ReLU)
Hidden Layer 2: 64 neurons (ReLU)
Output Layer: 10 neurons (Softmax)
```

Architecture flow:

```
784 → 128 → 64 → 10
```

Where:

* **ReLU** is used as the hidden layer activation function
* **Softmax** converts the output layer into probabilities for digits 0–9

---

# Training Process

The neural network training involves the following steps:

1. Load MNIST dataset
2. Normalize pixel values
3. Convert labels to one-hot encoding
4. Split dataset into training and testing sets
5. Initialize weights randomly
6. Perform forward propagation
7. Calculate loss
8. Perform backpropagation
9. Update weights using gradient descent
10. Repeat for multiple epochs

---

# Forward Propagation

Forward propagation calculates the network output:

```
Z1 = XW1 + b1
A1 = ReLU(Z1)

Z2 = A1W2 + b2
A2 = ReLU(Z2)

Z3 = A2W3 + b3
A3 = Softmax(Z3)
```

---

# Backpropagation

Backpropagation computes gradients and updates the weights:

```
dZ3 = A3 − Y
dW3 = A2ᵀ dZ3

dZ2 = dZ3 W3ᵀ * ReLU'(Z2)
dW2 = A1ᵀ dZ2

dZ1 = dZ2 W2ᵀ * ReLU'(Z1)
dW1 = Xᵀ dZ1
```

Weights are updated using **gradient descent**.

---

# Running the Project

Run the main program:

```
python mnist_nn.py
```

During training, the model prints the **loss value per epoch**.

Example output:

```
Epoch 0 Loss: 0.35
Epoch 5 Loss: 0.21
Epoch 10 Loss: 0.15
Epoch 15 Loss: 0.12
```

After training, the model prints **test accuracy**.

Example:

```
Test Accuracy: 0.94
```

---

# Visualization

The program also displays sample handwritten digits along with the predicted label using Matplotlib.

Example output:

```
Predicted: 7
```

The corresponding image of the handwritten digit will be displayed.

---

# Results

| Model                              | Accuracy   |
| ---------------------------------- | ---------- |
| Basic Neural Network               | ~90%       |
| Improved Network (2 hidden layers) | **92–95%** |

The improved architecture helps the model learn more complex digit patterns.

---

# Future Improvements

Possible improvements to the project include:

* Implementing **Dropout for regularization**
* Using **Convolutional Neural Networks (CNNs)**
* Adding **mini-batch gradient descent**
* Implementing **Adam optimizer**
* Applying **data augmentation**

Using CNN architectures can increase accuracy to **99%+ on MNIST**.

---

# Learning Outcomes

This project helps understand:

* Neural network fundamentals
* Matrix-based forward propagation
* Backpropagation and gradient descent
* Activation functions (ReLU, Softmax)
* One-hot encoding
* Model evaluation and accuracy

---

# Author

**Swati M Patil**
