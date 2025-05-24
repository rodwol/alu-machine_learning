#!/usr/bin/env python3
""" adds two matrices element-wise """


def add_matrices2D(mat1, mat2):
    """ adds two matrices element-wise """
    if len(mat1) != len(mat2):
        return None
    
    result = [[0 for _ in range(len(mat1[0]))] for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            result[i][j] = mat1[i][j] + mat2[i][j]

    return result
