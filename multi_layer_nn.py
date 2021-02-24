import random

import numpy as np


np.random.seed(0)
INP = [[random.randint(0, 5) for i in range(4)] for j in range(3)]

class LayerDense:
    """
    """

    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

layer1 = LayerDense(4, 5)
layer2 = LayerDense(5, 2)

layer1.forward(INP)
layer2.forward(layer1.output)
print(layer2.output)