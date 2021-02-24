"""
In this we we will be also have multiple input with multiple neurons
"""

import random

import numpy as np

# Taking n from user
n = int(input("Enter the len of inp you want: "))
nu = int(input("Enter the no. of neuron you want: "))

inp    = [[random.randint(0, 10) for i in range(n)] for j in range(nu)] # list of inputs for each neuron
weight = [[random.randint(0, 10) for i in range(n)] for j in range(nu)] # weights for each neuron
bias   = [random.randint(0, 5) for i in range(nu)] # bias (1 bias for 1 neuron)

# Printing all the info
print("\ninputs are: ", inp)
print("weights are: ", weight)
print("bias is: ", bias)

output = np.dot(weight, np.array(inp).T) + bias
print(output)
