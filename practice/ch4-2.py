import numpy as np
import sys
import os
sys.path.append(os.pardir)
from common.functions import sigmoid


def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y=))