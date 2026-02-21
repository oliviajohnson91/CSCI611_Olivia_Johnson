# CSCI611_Olivia_Johnson  
## Assignment 2 – CNN on CIFAR-10

This project implements a custom Convolutional Neural Network (CNN) in PyTorch trained on the CIFAR-10 dataset. The assignment includes model training, performance evaluation, feature map visualization, and analysis of maximally activating filters.

## Model Summary

- 3 Convolutional layers (3×3 kernels, padding=1)
- ReLU activations
- MaxPooling (2×2)
- Fully connected head (1024 → 100 → 10)
- Dropout (p=0.25)
- L2 regularization (weight_decay=1e-4)

Final Test Accuracy: **74%**

Loss: CrossEntropyLoss  
Optimizer: Adam (lr=0.001)  
Batch size: 20  
Epochs: 5  

## Repository Contents

Assignment_2/
- build_cnn.ipynb (full implementation + outputs)
- CSCI611_Assignment2.pdf (report)
- README.md

## How to Run

1. Clone the repository:
   git clone https://github.com/oliviajohnson91/CSCI611_Olivia_Johnson.git

2. Navigate to the folder:
   cd CSCI611_Olivia_Johnson/Assignment_2

3. Install dependencies:
   pip install torch torchvision matplotlib numpy

4. Launch Jupyter:
   jupyter notebook

5. Open and run:
   build_cnn.ipynb

The notebook downloads CIFAR-10 automatically and generates all required plots and visualizations.

---

Olivia Johnson  
CSCI 611 – February 2026