import torch
import torch.nn as nn
# import torchvision.transforms as transforms
# import torchvision.datasets as dsets
# from torch.autograd import Variable
# from torchsummary import summary

"""
A fully connected neural network with three hidden layers.
"""
class FullyConnectedNNNoGpu(
    nn.Module
):
    """
    A fully connected neural network with three hidden layers.
    Args:
        input_size (int): Size of the input layer.
        hidden_size (int): Size of the hidden layers.
        output_size (int): Size of the output layer.
    """
    def __init__(self, input_size, hidden_size, output_size):
        super(FullyConnectedNNNoGpu, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu1 = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.relu2 = nn.ReLU()
        self.fc3 = nn.Linear(hidden_size, hidden_size)
        self.relu3 = nn.ReLU()
        self.fc4 = nn.Linear(hidden_size, output_size)
        
    """
    Forwards the input through the network.
    Args:
        x (torch.Tensor): Input tensor of shape (batch_size, input_size).
    Returns:
        torch.Tensor: Output tensor of shape (batch_size, output_size).
    """
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu1(x)
        x = self.fc2(x)
        x = self.relu2(x)
        x = self.fc3(x)
        x = self.relu3(x)
        x = self.fc4(x)
        return x

    def train_model(self,epochs,train_loader,optimizer,criterion,model):
        total_iteration = 0 
        for epoch in range(epochs):
            for iter, (images, labels) in enumerate(train_loader):
                # Flatten the images
                images = images.view(-1, 28*28)
                # optimizer.zero_grad()  # Clear gradients for each batch
                optimizer.zero_grad()

                # Forward pass
                # This invokes PyTorch’s model.__call__() machinery, which then calls your custom  forward
                outputs = model(images)

                # this invokes criterion.forward(outputs, labels)
                # KEY : Do not apply Softmax before CrossEntropyLoss, because the loss function handles the required normalization internally
                loss = criterion(outputs, labels)

                # Backward pass and optimization
                loss.backward()
                optimizer.step()

                total_iteration += 1

                # print loss every 500 iterations
                if (total_iteration) % 500 == 0:
                    # loss.item() Calculates gradients for all model parameters involved in producing the loss.
                    print(f'Iteration: {total_iteration}, Loss: {loss.item()}')


