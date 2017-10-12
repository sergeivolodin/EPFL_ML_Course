# -*- coding: utf-8 -*-
"""Exercise 3.

Split the dataset based on the given ratio.
"""


import numpy as np


def split_data(x, y, ratio, seed=1):
    """
    split the dataset based on the split ratio. If ratio is 0.8
    you will have 80% of your data set dedicated to training
    and the rest dedicated to testing
    """
    # set seed
    np.random.seed(seed)
    L = x.shape[0]
    rg = range(L)
    idx_tr = np.random.choice(rg, size = int(L * ratio))
    idx_te = np.setdiff1d(rg, idx_tr)
    return idx_tr, idx_te
