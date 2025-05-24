#!/usr/bin/env python3
""" function that performs element-wise
        addition, subtraction, multiplication, and division
"""


def np_elementwise(mat1, mat2):
    """ function that performs element-wise
        addition, subtraction, multiplication, and division
    """
    add = [[a + b for a, b in zip(row1, row2)] for row1,
            row2 in zip(mat1, mat2)]
    sub = [[a - b for a, b in zip(row1, row2)] for row1,
            row2 in zip(mat1, mat2)]
    mul = [[a * b for a, b in zip(row1, row2)] for row1,
            row2 in zip(mat1, mat2)]
    div = [[a / b for a, b in zip(row1, row2)] for row1,
            row2 in zip(mat1, mat2)]
    return (add, sub, mul, div)
