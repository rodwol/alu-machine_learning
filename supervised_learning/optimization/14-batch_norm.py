#!/usr/bin/env python3
""" creates a batch normalization with tensorflow
"""
import tensorflow as tf


def create_batch_norm_layer(prev, n, activation):
    """
    Creates a dense layer with batch normalization in TensorFlow 2.x
    """
    # Dense layer
    init = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    model = tf.layers.Dense(units=n, kernel_initializer=init)
    Z = model(prev)
    gamma = tf.Variable(tf.constant(1.0, shape=[n]), name='gamma')
    beta = tf.Variable(tf.constant(0.0, shape=[n]), name='beta')
    mean, variance = tf.nn.moments(Z, axes=[0])
    epsilon = 1e-8
    Z_norm = tf.nn.batch_normalization(Z, mean, variance, beta, gamma, epsilon)
    return activation(Z_norm)
