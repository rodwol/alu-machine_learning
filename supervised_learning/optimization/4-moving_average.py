#!/usr/bin/env python3
"""
calculates the weighted moving average of a data set
with bias correction
"""
import numpy as np


def moving_average(data, beta):
    """Calculate the weighted moving average of a data set with bias correction.

    Args:
        data (list): List of data points.
        beta (float): Weighting factor between 0 and 1.
    """
    v = 0
    moving_averages = []
    for t, x in enumerate(data, 1):
        v = beta * v + (1 - beta) * x
        v_corrected = v / (1 - beta**t)
        moving_averages.append(v_corrected)
    return np.array(moving_averages)