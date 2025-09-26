#!/usr/bin/env python3
"""
shuffles the data points in two matrices the same way
"""
import numpy as np


def shuffle_data(X, Y):
    """Shuffle the data points in two matrices the same way.

    Args:
        X (np.ndarray): First matrix of shape (m, n).
        Y (np.ndarray): Second matrix of shape (m, p).
    """
    m = X.shape[0]
    permutation = np.random.permutation(m)
    return X[permutation], Y[permutation]
