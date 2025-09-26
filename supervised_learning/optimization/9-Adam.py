#!/usr/bin/env python3
"""
updates a variable using the adam optimization algorithm
"""
import numpy as np


def update_variable_Adam(alpha, beta1, beta2, epsilon, var, grad, v, s, t):
    """
    updates a variable using the Adam optimization algorithm
    """
    v = beta1 * v + (1 - beta1) * grad
    v_corrected = v / (1 - (beta1 ** t))
    s = beta2 * s + (1 - beta2) * (grad ** 2)
    s_corrected = s / (1 - (beta2 ** t))
    var = var - alpha * (v_corrected / ((s_corrected ** 0.5) + epsilon))
    return var, v, s
