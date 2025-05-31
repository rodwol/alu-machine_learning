#!/usr/bin/env python3
""" calculates the inverse of a matrix """


def inverse(matrix):
    """ calculates the inverse of a matrix """
    if not isinstance(matrix, list) or not all(isinstance(row, list) 
    for row in matrix):
        raise TypeError("matrix must be a list of lists")
    
    rows = len(matrix)
    if rows == 0:
        raise ValueError("matrix must be a non-empty square matrix")
    for row in matrix:
        if len(row) != rows:
            raise ValueError("matrix must be a non-empty square matrix")
    
    # Calculate the determinant of the matrix
    det = determinant(matrix)
    if det == 0:
        return None  # Matrix is singular
    
    # Handle 1x1 matrix case
    if rows == 1:
        return [[1 / matrix[0][0]]]
    
    # Compute the adjugate matrix
    adjugate_matrix = adjugate(matrix)
    
    inverse_matrix = []
    for i in range(rows):
        inverse_row = []
        for j in range(rows):
            inverse_row.append(adjugate_matrix[i][j] / det)
        inverse_matrix.append(inverse_row)
    
    return inverse_matrix

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
        submatrix = [row[:j] + row[j+1:] for row in matrix[1:]]
        # Recursive call for determinant calculation
        det += (-1) ** j * matrix[0][j] * determinant(submatrix)
    return det

def adjugate(matrix):
    rows = len(matrix)
    # Compute the cofactor matrix
    cofactor_matrix = []
    for i in range(rows):
        cofactor_row = []
        for j in range(rows):
            submatrix = [row[:j] + row[j+1:] for row in
                        (matrix[:i] + matrix[i+1:])]
            # Calculate the determinant of the submatrix
            det = determinant(submatrix)
            # Apply the sign (-1)^(i+j)
            sign = (-1) ** (i + j)
            cofactor_row.append(sign * det)
        cofactor_matrix.append(cofactor_row)
    
    # Transpose the cofactor matrix to get the adjugate matrix
    adjugate_matrix = [[0 for _ in range(rows)] for _ in range(rows)]
    for i in range(rows):
        for j in range(rows):
            adjugate_matrix[j][i] = cofactor_matrix[i][j]
    
    return adjugate_matrix
