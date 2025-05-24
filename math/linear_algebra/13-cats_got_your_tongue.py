#!/usr/bin/env python3
""" concatenates two arrays along the given axis without
    using any loops or conditionals
"""
import numpy as np

def np_cat(mat1, mat2, axis=0):
    """ concatenates two arrays along the given axis without
    using any loops or conditionals
    """
    return np.concatenate((mat1, mat2), axis=axis)
