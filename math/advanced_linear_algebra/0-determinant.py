#!/usr/bin/env python3
""" function that calculates the minor matrix of a matrix """


def determinant(matrix):
    """Calculates the determinant of a square matrix."""

    # Validate input type
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Handle empty matrix ([]) or non-square
    if matrix == [[]]:
        return 1

    if matrix == [] or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a square matrix")

    n = len(matrix)

    # Base cases
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    # Recursive case for larger matrices
    det = 0
    for col in range(n):
        # Create submatrix excluding first row and col-th column
        submatrix = [row[:col] + row[col+1:] for row in matrix[1:]]
        sign = (-1) ** col
        det += sign * matrix[0][col] * determinant(submatrix)

    return det
