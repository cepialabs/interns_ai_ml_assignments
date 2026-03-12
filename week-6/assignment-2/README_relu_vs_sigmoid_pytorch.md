# MNIST Activation Function Comparison (PyTorch)

This project compares two neural networks trained on the MNIST dataset
using different activation functions.

Models: 1. ReLU activation 2. Sigmoid activation

Both models use: - PyTorch - CrossEntropyLoss (categorical cross
entropy) - Adam optimizer

Model Architecture: Input (28x28 image)

Layers: - Flatten layer - Fully connected layer (784 → 128) - Activation
(ReLU or Sigmoid) - Fully connected layer (128 → 10)

Training Setup: - Epochs: 10 - Batch Size: 64

Output: The notebook plots training loss across epochs to compare the
performance of the two activation functions.

Expected Observation: ReLU generally converges faster and achieves lower
loss, while Sigmoid may train slower due to vanishing gradient problems.

Requirements:

pip install torch torchvision matplotlib jupyter

Run:

jupyter notebook mnist_relu_vs_sigmoid_pytorch.ipynb
