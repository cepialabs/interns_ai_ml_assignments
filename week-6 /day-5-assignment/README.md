# MNIST Digit Recognition using Improved Neural Network

## week 6 - day 5 - Assignment
Improve the MNIST digit recognizer by modifying the network architecture (layers, neurons, activation, dropout) and achieve higher accuracy while explaining the design choices.

---

## Objective
The objective of this project is to build an improved neural network model to recognize handwritten digits from the MNIST dataset. The network architecture is modified by adjusting layers, neurons, activation functions, and dropout to achieve better accuracy.

---

## Dataset
The **MNIST dataset** is a widely used dataset for image classification.

- Total Images: 70,000
- Training Images: 60,000
- Testing Images: 10,000
- Image Size: 28 × 28 pixels
- Number of Classes: 10 (Digits 0–9)

The dataset is loaded using the `torchvision.datasets` module.

---

## Technologies Used
- Python
- PyTorch
- Torchvision
- NumPy
- Matplotlib
- Jupyter Notebook

---

## Data Preprocessing
The following preprocessing steps are applied:

1. Convert images to tensors.
2. Normalize pixel values.
3. Load the dataset using DataLoader for efficient batching.
4. Shuffle the training data.

---

## Model Architecture

The neural network architecture is improved by increasing the number of layers and adding dropout to prevent overfitting.

**Architecture:**

Input Layer  
→ Flatten (28×28)

Hidden Layer 1  
→ 256 Neurons  
→ ReLU Activation  
→ Dropout (0.3)

Hidden Layer 2  
→ 128 Neurons  
→ ReLU Activation  
→ Dropout (0.3)

Hidden Layer 3  
→ 64 Neurons  
→ ReLU Activation

Output Layer  
→ 10 Neurons (Digit Classes)

---

## Training Configuration

- Loss Function: CrossEntropyLoss  
- Optimizer: Adam  
- Learning Rate: 0.001  
- Batch Size: 64  
- Epochs: 5

---

## Model Training
The model is trained on the MNIST training dataset. During training, the loss is minimized using the Adam optimizer and backpropagation.

---

## Model Evaluation
The trained model is evaluated on the MNIST test dataset.

**Accuracy Achieved:**  
Approximately **97% – 98% test accuracy**

---

## Visualization
The notebook includes:

- Sample MNIST digit images
- Predicted digit visualization
- Model performance evaluation

---

## Output
The trained model is saved as:

```
mnist_improved_model.pth
```

This file can be used later for predictions without retraining the model.

---

## Conclusion
The MNIST digit recognizer was successfully improved by modifying the neural network architecture. Increasing the number of neurons and adding dropout layers helped improve the model's performance while reducing overfitting.

The model achieves high accuracy and effectively recognizes handwritten digits.

---

## Future Improvements
- Use Convolutional Neural Networks (CNN)
- Increase number of training epochs
- Apply hyperparameter tuning
- Implement data augmentation
