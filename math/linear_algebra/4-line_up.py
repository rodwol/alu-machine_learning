#!/usr/bin/env python3
""" adds two arrays element-wise """


def add_arrays(arr1, arr2):
    """ adds two arrays element-wise """
    if len(arr1) != len(arr2):
        return None
    result = []
    for a, b in zip(arr1, arr2):
        result.append(a + b)

    return result
