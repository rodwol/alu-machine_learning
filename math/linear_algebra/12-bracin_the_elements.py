#!/usr/bin/env python3
""" function that performs element-wise
        addition, subtraction, multiplication, and division
"""


def np_elementwise(mat1, mat2):
    """ function that performs element-wise
        addition, subtraction, multiplication, and division
    """
    sum_result = mat1 + mat2
    diff_result = mat1 - mat2
    prod_result = mat1 * mat2
    quot_result = mat1 / mat2
    return (sum_result, diff_result, prod_result, quot_result)
