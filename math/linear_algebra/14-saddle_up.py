#!/usr/bin/env python3
""" function that performs matrix multiplication of two numpy
    arrays without using loops or conditionals """

import numpy as np


def np_matmu(mat1, mat2):
    """ function that performs matrix multiplication of
        two numpy arrays without using loops or conditionals
    """
    return np.matmul(mat1, mat2)
