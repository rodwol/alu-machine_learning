#!/usr/bin/env python3
""" calculates the cofactor matrix of a matrix """


def cofactor(matrix):
    # Check if the input is a list of lists
    if not isinstance(matrix, list) or \
           not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Check if the matrix is square and non-empty
    rows = len(matrix)
    if rows == 0:
        raise ValueError("matrix must be a non-empty square matrix")
    for row in matrix:
        if len(row) != rows:
            raise ValueError("matrix must be a non-empty square matrix")
 
    # Handle 1x1 matrix case
    if rows == 1:
        return [[1]]  # The cofactor matrix of a 1x1 matrix is [[1]]
    
    cofactor_matrix = []
    for i in range(rows):
        cofactor_row = []
        for j in range(rows):
            submatrix = [
                row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])
            ]
            # Calculate the determinant of the submatrix
            det = determinant(submatrix)
            # Apply the sign (-1)^(i+j)
            sign = (-1) ** (i + j)
            cofactor_row.append(sign * det)
        cofactor_matrix.append(cofactor_row)
    return cofactor_matrix


def determinant(matrix):
    n = len(matrix)
    # Base case for 1x1 matrix
    if n == 1:
        return matrix[0][0]
    # Base case for 2x2 matrix
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for j in range(n):
        # Create the submatrix by excluding the first row and j-th column
        submatrix = [row[:j] + row[j+1:] for row in matrix[1:]]
        # Recursive call for determinant calculation
        det += (-1) ** j * matrix[0][j] * determinant(submatrix)
    return det
