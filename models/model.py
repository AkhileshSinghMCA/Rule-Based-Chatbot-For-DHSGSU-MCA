import torch
import torch.nn as nn

# Define the neural network class
class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(NeuralNet, self).__init__()
        # Define the layers of the neural network
        self.l1 = nn.Linear(input_size, hidden_size)  # First fully connected layer
        self.relu = nn.ReLU()  # ReLU activation function
        self.l2 = nn.Linear(hidden_size, hidden_size)  # Second fully connected layer
        self.l3 = nn.Linear(hidden_size, output_size)  # Output layer

    def forward(self, x):
        # Forward pass through the network
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        return out
