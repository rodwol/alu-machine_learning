#!/usr/bin/env python3
""" function that calculates the minor matrix of a matrix """


def minor(matrix):
    """ minor of the given matrix """

    if not isinstance(matrix, list) or \
           not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if len(matrix) == 0 or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    
    def determinant(m):
        """ computes the determinant of a square matrix """
        if len(m) == 1:
            return m[0][0]
        if len(m) == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]
        
        det = 0
        for c in range (len(m)):
            sunmatrix = [row[:c] + row[c+1:] for row in m[1:]]
            det += ((-1) ** c) * m[0][c] * determinant(submatrix)
        return det

    size = len(matrix)
    minor_matrix = []
    for i in range(size):
        minor_row = []
        for j in range(size):
            # Create submatrix by excluding i-th row and j-th column
            submatrix = [
                row[:j] + row[j+1:] for idx, row in enumerate(matrix) if idx != i
            ]
            minor_value = determinant(submatrix)
            minor_row.append(minor_value)
        minor_matrix.append(minor_row)
    
    return minor_matrix               
