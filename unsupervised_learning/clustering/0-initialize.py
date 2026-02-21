#!/usr/bin/env python3
"""
Docstring for unsupervised_learning.clustering.0-initialize
"""
import numpy as np


def initialize(X, k):
    """
    Docstring for initialize
    
    n: no of data points
    d: no of dimensions for each data point
    K: positive interger - the no of clusters
    return: numpy.ndarray (k, d) containing the intialized
    centroids for each cluster, or None on failure
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None
    if not isinstance(k, int) or k <= 0:
        return None
    
    n, d = X.shape
    min_val = X.min(axis=0)
    max_val = X.max(axis=0)

    return np.random.uniform(min_val, max_val, size=(k, d))
    