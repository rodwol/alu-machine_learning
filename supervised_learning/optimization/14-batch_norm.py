#!/usr/bin/env python3
""" creates a batch normalization with tensorflow
"""
import tensorflow as tf


def create_batch_norm_layer(prev, n, activation):
    """
    Creates a dense layer with batch normalization in TensorFlow 2.x
    """
    # Dense layer
    dense = tf.keras.layers.Dense(
        units=n,
        kernel_initializer=tf.keras.initializers.VarianceScaling
        (scale=1.0, mode="fan_avg")
    )(prev)

    # Batch normalization
    bn = tf.keras.layers.BatchNormalization(axis=-1)(dense)

    # Apply activation
    return activation(bn)