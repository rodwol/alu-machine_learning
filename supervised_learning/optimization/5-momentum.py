#!/usr/bin/env python3
"""
function that updates a variable using the gradient
"""
import numpy as np


def update_variables_momentum(alpha, beta1, var, grad, v):
    """
    update a variable using the gradient and momentum
    """
    v_new = beta1 * v + (1 - beta1) * grad
    var_new = var - alpha * v_new
    return var_new, v_new
