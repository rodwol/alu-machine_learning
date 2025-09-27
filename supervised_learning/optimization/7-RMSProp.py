#!/usr/bin/env python3
"""
function that updates a variable using the RMSProp
"""
import numpy as np


def update_variables_RMSProp(alpha, beta2, epsilon, var, grad, s):
    """
    updates a variable using RMSProp optimization
    """
    new_s = beta2 * s + (1 - beta2) * np.square(grad)
    var_new = var - alpha * grad / (np.sqrt(new_s) + epsilon)
    return var_new, new_s
