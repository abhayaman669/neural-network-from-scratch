"""
SOFTMAX ACTIVATION

Input -> Exponentiate ->  Normalize -> Output

Exponentiate is e power x where x is the input
Normalize is e power of x divided by sum of e of all inputs.

Combination of Exponentiate and Normalize is softmax activation function

Wiki: https://en.wikipedia.org/wiki/Softmax_function
video: https://www.youtube.com/watch?v=omz_NdFgWyU&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3&index=6 
"""


import math


output_layer = [1.2, 3.4, 5.7]
E = math.e

exp_values= []
for rope in output_layer:
    exp_values.append(E**rope)

norm_base = sum(exp_values)
norm_values = []

for value in exp_values:
    norm_values.append(value/norm_base)

# ========================================================================
# Using Numpy 
# ========================================================================

import numpy as np


output_layer = [1.2, 3.4, 5.7]

exp_values= np.exp(output_layer)

norm_values = exp_values / np.sum(exp_values)

# ========================================================================
# Using Numpy and having batches of input
# ========================================================================
# 
# numpy.exp() will work fine for batches of input
# for numpy.sum() we need to provide some parameter
#   axis: will tell to sum rows/col (0 for rows and 1 for column)
#   keepdims: will keep the current dimension form
# 
# ========================================================================
# docs for numpy sum: https://numpy.org/doc/stable/reference/generated/numpy.sum.html
# ========================================================================

import numpy as np


output_layer = [[1.2, 3.4, 5.7], [1.3, 3, 2.7], [1.6, 2.5, 2.6]]

exp_values= np.exp(output_layer)

# ========================================================
# NOTE: if the value to find exp of is very large then the exp might overflow
# SOLLUTION: take each input and subtract them from the largest input value. :)
# ========================================================

norm_values = exp_values / np.sum(exp_values, axis=1, keepdims=True)
