#!/usr/bin/env python3
"""
Defines a function that performs valid convolution
on a grayscale image
"""

import numpy as np

def convolve_grayscale_valid(images, kernel):
    """
    Performs a valid convolution on grayscale images
    """
    num_images = images.shape[0]
    image_height = images.shape[1]
    image_width = images.shape[2]
    kernel_height = kernel.shape[0]
    kernel_width = kernel.shape[1]

    convolved = np.zeros((num_images,
                          image_height - kernel_height + 1,
                          image_width - kernel_width + 1))
    for row in range(image_height - kernel_height + 1):
        for col in range(image_width - kernel_width + 1):
            output = np.sum(images[:, row: row + kernel_height, col: col + kernel_width] * kernel,
                            axis=1).sum(axis=1)
            convolved[:, row, col] = output
    return convolved

