import random


# Taking n from user
n = int(input("Enter the let of inp/weight you want: "))

inp    = [random.randint(0, 10) for i in range(n)] # list of inputs
weight = [random.randint(0, 10) for i in range(n)] # weights for each input
bias   = random.randint(0, 5)                      # bias (1 bias for 1 neuron)

# Printing all the info
print("\ninputs are: ", inp)
print("weights are: ", weight)
print("bias is: ", bias)

"""
calculating output i.e.

sum of all inp[i] * weight[i] + bias
here i is from 0 to the length of inp. here it's 3
"""
output = sum([i*j for i, j in zip(inp, weight)]) + bias
print("="*20, "\nCalculated output is: ", output)