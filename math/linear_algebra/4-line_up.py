#!/usr/bin/env python3
""" adds two arrays element-wise """


def add_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return None
    result = []
    for a, b in zip(arr1, arr2):
        result.append(a + b)

    return result
"""
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            result[i][j] = arr1[i][j] + arr2[i][j]
"""
