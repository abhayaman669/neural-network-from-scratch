inp = [1, 2, 3]        # list of inputs
weight = [10, 20, 30]  # weights for each input
bias = 2               # bias (1 bias for 1 neuron)

"""
calculating output i.e.

sum of all inp[i] * weight[i] + bias
here i is from 0 to the length of inp. here it's 3
"""
output = sum([i*j for i, j in zip(inp, weight)]) + bias
print(output)