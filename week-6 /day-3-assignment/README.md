# MNIST Digit Classification using Neural Network (Scikit-Learn)

## Project Overview
This project trains a neural network model to classify handwritten digits using the MNIST dataset. The model uses categorical cross-entropy as the loss function and visualizes training loss across epochs.

## Objective
The objective of this assignment is to:
- Train an MNIST classification model
- Use categorical cross-entropy loss
- Plot training loss across epochs

## Dataset
MNIST dataset contains handwritten digits from 0 to 9.

Dataset details:
- 70,000 images
- Image size: 28 × 28 pixels
- Each image represents a digit

## Technologies Used
- Python
- Scikit-Learn
- NumPy
- Matplotlib

## Model Used
A neural network model using **MLPClassifier** from Scikit-Learn.

Model Architecture:
- Input Layer: 784 neurons (28×28 pixels)
- Hidden Layer 1: 128 neurons
- Hidden Layer 2: 64 neurons
- Output Layer: 10 neurons

Activation Function: ReLU

Optimizer: Adam

## Loss Function
Categorical Cross Entropy (Log Loss) is used for multi-class classification.

## Training Process
The model is trained for multiple epochs and the training loss is calculated after each epoch.

## Visualization
The training loss is plotted against epochs to understand the learning performance of the model.

## Results
The trained model achieves good accuracy on the MNIST dataset and successfully classifies handwritten digits.

## Conclusion
This project demonstrates how neural networks can be implemented using Scikit-Learn for image classification tasks without using deep learning frameworks like TensorFlow.
