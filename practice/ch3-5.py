import numpy as np
import sys
import os
sys.path.append(os.pardir)
from common.functions import sigmoid


def softmax(x):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

a = np.array([0.1, 0.3, 0.7])
y = softmax(a)
print(y)
