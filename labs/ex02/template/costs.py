# -*- coding: utf-8 -*-

import numpy as np

"""Function used to compute the loss."""

def compute_loss(y, tx, w, mae = False):
    """Calculate the loss.

    You can calculate the loss using mse or mae.
    """

    N = y.shape[0]
    e = y - tx @ w

    if mae:
        return 1. / N * np.sum(np.abs(e))
    else:
        return 1. / (2 * N) * (e.T @ e)
