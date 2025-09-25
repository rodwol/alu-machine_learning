#!/usr/bin/env python3
"""Constants for 0-norm optimization problems."""
import numpy as np


def normalization_constants(X):
    """Compute normalization constants for 0-norm optimization problems.

    Args:
        X (np.ndarray): Input data of shape (n_samples, n_features).
    """
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    return mean, std