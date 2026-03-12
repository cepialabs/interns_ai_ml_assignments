# MNIST Neural Network Training (Without TensorFlow)

This project demonstrates how to train a **neural network on the MNIST
dataset using PyTorch** instead of TensorFlow.

## Features

-   Uses **PyTorch**
-   Trains a simple neural network on MNIST digits
-   Uses **Categorical Cross Entropy (CrossEntropyLoss)**
-   Plots **training loss across epochs**

## Model Architecture

Input: 28 × 28 image

Layers: - Flatten Layer - Fully Connected Layer (784 → 128) - ReLU
Activation - Fully Connected Layer (128 → 10)

## Training Setup

-   Loss Function: CrossEntropyLoss
-   Optimizer: Adam
-   Epochs: 10
-   Batch Size: 64

## Output

The notebook generates a plot:

Training Loss vs Epochs

This helps visualize how the model improves during training.

## Requirements

Install required libraries:

    pip install torch torchvision matplotlib jupyter

## Run

    jupyter notebook mnist_pytorch_training.ipynb
