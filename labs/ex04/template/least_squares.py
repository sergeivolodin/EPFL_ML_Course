# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np


def least_squares(y, tx):
    """calculate the least squares."""
    # ***************************************************
    # returns mse, optimal weights
    # ***************************************************

    N = tx.shape[0]
    w = np.linalg.pinv(tx.T @ tx) @ tx.T @ y
    e = y - tx @ w
    mse = 1. / 2 / N * e.T @ e
    return mse, w
