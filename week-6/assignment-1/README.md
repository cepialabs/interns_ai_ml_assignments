Simple Neural Network From Scratch (NumPy)
Project Overview

This project demonstrates how to build a simple neural network with one hidden layer from scratch using NumPy. The goal is to understand the core concepts behind neural networks, including forward propagation, loss calculation, backpropagation, and weight updates.

Unlike high-level frameworks such as TensorFlow or PyTorch, this implementation manually performs all mathematical operations involved in training a neural network.

Neural Network Architecture

The model contains three layers:

Input Layer → Hidden Layer → Output Layer

Structure:

Input Layer (2 neurons)
        ↓
Hidden Layer (3 neurons)
        ↓
Output Layer (1 neuron)
Input Features

The model predicts whether a student passes or fails based on:

x1 = Hours studied

x2 = Hours slept

Output

1 → Pass

0 → Fail

Concepts Covered

This project demonstrates the following core machine learning concepts:

Neural network architecture

Weight and bias initialization

Forward propagation

Activation functions (Sigmoid)

Loss calculation (Mean Squared Error)

Backpropagation

Gradient descent

Model training loop

Project Workflow

The neural network training process follows these steps:

1. Input Data

The dataset containing features and labels is fed into the network.

2. Forward Propagation

Data flows through the network:

Input → Hidden Layer → Output Layer

Each neuron computes:

z = w*x + b

Then applies the activation function:

a = sigmoid(z)
3. Prediction

The output layer produces the predicted value:

y_pred

Example:

0.82 → 82% probability of passing
4. Loss Calculation

The error between the predicted value and the true value is calculated using Mean Squared Error (MSE):

Loss = (y - y_pred)^2
5. Backpropagation

The model calculates how much each weight contributed to the error by computing gradients.

Gradients propagate backward through the network:

Output Layer → Hidden Layer
6. Weight Updates

Weights are updated using Gradient Descent:

w = w - learning_rate * gradient

This reduces the prediction error over time.

7. Training Loop

The above steps repeat for many iterations (epochs) until the model learns meaningful patterns in the data.

Project Structure
simple-neural-network/
│
├── simple_neural_network.ipynb
├── README.md
File Description

simple_neural_network.ipynb

Jupyter Notebook containing:

dataset creation

neural network implementation

forward propagation

backpropagation

training loop

prediction example

Requirements

Install the required dependencies:

pip install numpy jupyter
How to Run

Clone the repository

git clone https://github.com/yourusername/simple-neural-network.git

Navigate to the project folder

cd simple-neural-network

Start Jupyter Notebook

jupyter notebook

Open:

simple_neural_network.ipynb

Run the cells step by step to train the neural network.

Learning Objective

This project helps beginners understand:

How neural networks process data

How weights are updated during training

How backpropagation works internally

It focuses on learning the mathematics and logic behind neural networks rather than relying on machine learning libraries.

Possible Improvements

You can extend this project by:

Adding more hidden layers

Implementing different activation functions

Using cross-entropy loss

Visualizing training loss

Building the same model using deep learning frameworks