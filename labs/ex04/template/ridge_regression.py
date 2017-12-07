# -*- coding: utf-8 -*-
"""Exercise 3.

Ridge Regression
"""

import numpy as np


def ridge_regression(y, tx, lambda_):
    """implement ridge regression."""
    N = tx.shape[0]
    w = np.linalg.pinv(tx.T @ tx + lambda_ * (2. * N) * np.eye(tx.shape[1])) @ tx.T @ y
    e = y - tx @ w
    return w
