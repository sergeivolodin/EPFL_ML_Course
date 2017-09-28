# -*- coding: utf-8 -*-
"""Stochastic Gradient Descent"""

from costs import compute_loss
from helpers import batch_iter
gd_m = __import__('gradient descent')

def compute_stoch_gradient(y, tx, w, mae = False):
    """Compute a stochastic gradient from just few examples n and their corresponding y_n labels."""
    return gd_m.compute_gradient(y, tx, w, mae = mae)

def stochastic_gradient_descent(
        y, tx, initial_w, batch_size, max_iters, gamma, mae = False):
    """Stochastic gradient descent algorithm."""
    ws = [initial_w]
    losses = []
    w = initial_w
    for (n_iter, (y_, tx_)) in enumerate(batch_iter(y, tx, batch_size = batch_size,
                                                    num_batches=max_iters, shuffle=True)):
        loss = compute_loss(y, tx, w, mae = mae)
        stoch_gradient = compute_stoch_gradient(y_, tx_, w, mae = mae)
        w -= gamma * stoch_gradient
        ws.append(w)
        losses.append(loss)
        print("Stochastic Gradient Descent({bi}/{ti}): loss={l}, w0={w0}, w1={w1}".format(
              bi=n_iter, ti=max_iters - 1, l=loss, w0=w[0], w1=w[1]))

    return losses, ws
