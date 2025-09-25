#!/usr/bin/env python3
"""
constant that normalizes a matrix
"""
import numpy as np


def normalize(X, m, s):
    """Normalize a matrix using the mean and standard deviation.

    Args:
        X (np.ndarray): Input data of shape (n_samples, n_features).
        m (np.ndarray): Mean of each feature of shape (n_features,).
        s (np.ndarray): Standard deviation of each feature of shape (n_features,).
    """
    return (X-m)/s
