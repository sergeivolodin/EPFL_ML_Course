# -*- coding: utf-8 -*-
"""Gradient Descent"""

import numpy as np
from costs import compute_loss

def compute_gradient(y, tx, w, mae = False):
    """Compute the gradient."""

    N = y.shape[0]
    e = y - tx @ w
    if mae:
        s = np.array(np.sign(e), dtype = np.float64)

        # can (?) use 0 instead of uniform random
        # since if e_n = 0 then the error = 0
        s[e == 0] = np.random.uniform(low = -1, high = 1, size = np.sum(e == 0))
        if np.sum(e == 0) > 0:
            print("Encountered zero component: %s" % str(np.where(e == 0)[0]))

        return(- 1. / N * s.T @ tx)
    else:
        return(- 1. / N * e.T @ tx)

def gradient_descent(y, tx, initial_w, max_iters, gamma):
    """Gradient descent algorithm."""
    # Define parameters to store w and loss
    ws = [initial_w]
    losses = []
    w = initial_w
    for n_iter in range(max_iters):
        loss = compute_loss(y, tx, w)
        gradient = compute_gradient(y, tx, w)
        w -= gamma * gradient
        ws.append(w)
        losses.append(loss)
        print("Gradient Descent({bi}/{ti}): loss={l}, w0={w0}, w1={w1}".format(
              bi=n_iter, ti=max_iters - 1, l=loss, w0=w[0], w1=w[1]))

    return losses, ws
