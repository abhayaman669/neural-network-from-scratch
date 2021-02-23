import random

import numpy as np

# Taking n from user
n = int(input("Enter the let of inp/weight you want: "))
nu = int(input("Enter the no. of neuron you want: "))

inp    = [random.randint(0, 10) for i in range(n)] # list of inputs
weight = [[random.randint(0, 10) for i in range(n)] for j in range(nu)] # weights for each neuron
bias   = [random.randint(0, 5) for i in range(nu)] # bias (1 bias for 1 neuron)

# Printing all the info
print("\ninputs are: ", inp)
print("weights are: ", weight)
print("bias is: ", bias)

"""
calculating output i.e.

sum of all inp[i] * weight[i] + bias
here i is from 0 to the length of inp. here it's 3
"""

output = np.dot(weight, inp) + bias
print("="*20, "\nCalculated output is: ", output)