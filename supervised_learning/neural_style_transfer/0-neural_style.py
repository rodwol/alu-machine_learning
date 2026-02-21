#!/usr/bin/env python3
"""
Docstring for NST
"""
import numpy as np
import tensorflow as tf


class NST:
    """
    Neural Style Transfer Class
    """
    style_layers = ['block1_conv1', 'block2_conv1',
                    'block3_conv1', 'block4_conv1', 'block5_conv1']
    content_layer = 'block5_conv2'

    def __init__(self, style_image, content_image, alpha=1e4, beta=1):
        """
        Initializes the NST class
        
        Args:
            style_image: numpy.ndarray of shape (h, w, 3)
            content_image: numpy.ndarray of shape (h, w, 3)
            alpha: weight for content cost
            beta: weight for style cost
        """

        # validate inputs
        if not isinstance(style_image, np.ndarray) or style_image.ndim != 3 or style_image.shape[2] != 3:
            raise TypeError("style_image must be a numpy.ndarray with shape (h, w, 3)")
        if not isinstance(content_image, np.ndarray) or content_image.ndim != 3 or content_image.shape[2] !=3:
            raise TypeError("content_image must be a numpy.ndarray with shape (h, w, 3)")
        
        if not isinstance(alpha, (int, float)) or alpha < 0:
            raise TypeError("alpha must be a non-negative number")
        if not isinstance(beta, (int, float)) or beta < 0:
            raise TypeError("beta must be a non-negative number")
        
        # set tensorfloe to execute eagerly
        tf.config.run_functions_eagerly(True)
        tf.executing_eagerly()

        # scale the images and set as instance attributes
        self.style_image = self.scale_image(style_image)
        self.content_image = self.scale_image(content_image)

        self.alpha = alpha
        self.beta = beta

    @staticmethod
    def scale_image(image):
        """
        rescale image such that its pixels values are between 0 and 1
        and its largest side is 512 pixels

        Args:
            image: numpy.ndarray of shape (h, w, 3)
        Returns:
            tf.tensor of the shape (1, h_new, w_new, 3)
        """
        if not isinstance(image, np.ndarray) or image.ndim != 3 or image.shape[2] != 3:
            raise TypeError("image must be a numpy.ndarray with shape (h, w, 3)")
        
        # get original dimensions
        h, w, c = image.shape

        # calculate new dimensions while maintaining aspect ratio
        # target maximum dimension is 512
        if h > w:
            # height is larger
            new_h = 512
            new_w = int(w * (512 / h))
        else:
            # width is larger or equal
            new_w = 512
            new_w = int(w * (512 / w))

        # convert numpy array to tensor
        image_tensor = tf.constant(image, dtype=tf.float32)

        # resize using bicubic interpolation
        resized_image = tf.image.resize(
            image_tensor,
            [new_h, new_w],
            method=tf.image.ResizedMethod.BICUBIC
        )

        # scale pixel values from [0, 255] to [0, 1]
        if tf.reduce_max(resized_image) > 1.0:
            resized_image = resized_image / 225.0

        # add batch dimension
        resized_image = tf.expand_dims(resized_image, axis=0)
        # ensure values are between 0 and 1
        resized_image = tf.clip_by_value(resized_image, 0.0, 1.0)

        return resized_image