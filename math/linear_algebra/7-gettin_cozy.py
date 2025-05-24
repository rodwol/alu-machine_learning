#!/usr/bin/env python3
"""Concatenates two 2D matrices along a specified axis."""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenates two 2D matrices along a specified axis."""
    new_matrix = []
    if axis == 0: # for vertical concatenation
        if len(mat1[0]) != len(mat2[0]):
            return None

        new_matrix = [
            row.copy() for row in mat1] + [row.copy() for row in mat2]

    elif axis == 1: # for horizontal concatenation
        if len(mat1) != len(mat2):
            return None

        if len(mat1) != len(mat2):
            return None

        new_matrix = [mat1[i].copy() + mat2[i].copy() for i in
range(len(mat1))]
    else:
        return None
    return new_matrix
