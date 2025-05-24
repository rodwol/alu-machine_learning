#!/usr/bin/env python3
""" returns the transpose of a 2D matrix """


def matrix_transpose(matrix):
    """ returns the transpose of a 2D matrix """
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    for c in range(cols):
        transposed.append([matrix[r][c] for r in range(rows)])
    return transposed
