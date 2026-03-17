🔢 MNIST Digit Recognizer: High-Accuracy Deep Learning Model 🚀
This project focuses on building and optimizing a Deep Neural Network to achieve high accuracy on the MNIST dataset (handwritten digits). The goal was to refine the network architecture through strategic design choices to maximize predictive performance.

📝 Project Overview
This notebook implements a full end-to-end Deep Learning pipeline, including:

Data Preparation: Loading and normalizing 60,000 training and 10,000 testing grayscale images.

Architectural Optimization: Experimenting with layers, neurons, and dropout rates to improve accuracy.

Real-world Inference: A custom script to load and predict handwritten digits from external .PNG files. 🖼️

🏗️ Model Architecture & Design Choices
To boost performance and prevent common training issues, the following optimizations were implemented:

Dense Layers: Carefully balanced neurons to capture complex patterns without excessive computational cost.

ReLU Activation: Applied to hidden layers to accelerate training and mitigate the vanishing gradient problem. ⚡

Dropout Regularization: Integrated Dropout layers to reduce overfitting, ensuring the model generalizes well to new, unseen data. 🛡️

Input Flattening: Efficiently converted 2D images (28x28) into 1D vectors for processing by the dense network.

🛠️ Tech Stack & Requirements
Python 3.x 🐍

TensorFlow / Keras (Deep Learning Framework)

NumPy (Numerical Computing)

Matplotlib (Data Visualization) 📊

Pillow (PIL) (Image Processing for inference)

🚀 How to Use
Setup: Ensure all dependencies are installed.

Training: Run the cells sequentially to preprocess the data and train the model.

Testing: Evaluate the model on the test set to view performance metrics.

Custom Predictions: Place your own handwritten digit images in the directory (formatted as Mnist0.PNG, Mnist1.PNG, etc.) and run the inference cell to see the model in action!

📈 Results & Visualization
The model includes a visualization tool that displays the processed image alongside its Actual Label vs. Predicted Label. This provides immediate feedback on the model's performance and identifies which digits are most challenging for the network. ✅