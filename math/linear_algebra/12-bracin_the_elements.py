#!/usr/bin/env python3
""" function that performs element-wise
        addition, subtraction, multiplication, and division using NumPy
"""
import numpy as np


def np_elementwise(mat1, mat2):
    """ function that performs element-wise
        addition, subtraction, multiplication, and division using NumPy
    """
    return (
        mat1 + mat2,
        mat1 - mat2,
        mat1 * mat2,
        mat1/mat2
    )
