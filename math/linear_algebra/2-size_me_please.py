#!/usr/bin/env python3
"""Calculates the shape of a matrix as a list of integers."""


def matrix_shape(matrix):
    """Calculates the shape of a matrix as a list of integers."""
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0] if matrix else None
    return shape
