#!/usr/bin/env python3

import numpy as np
import tensorflow as tf
train_mini_batch = __import__('3-mini_batch').train_mini_batch

def one_hot(Y, classes):
    """convert an array to a one-hot matrix"""
    oh = np.zeros((Y.shape[0], classes))
    oh[np.arange(Y.shape[0]), Y] = 1
    return oh

if __name__ == '__main__':
    lib= np.load('../data/MNIST.npz')
    x_train_3D = lib['x_train']
    y_train = lib['y_train']
    x_train = x_train_3D.reshape((x_train_3D.shape[0], -1))
    y_train_oh = one_hot(y_train, 10)
    x_valid_3D = lib['x_valid']
    y_valid = lib['y_valid']
    x_valid = x_valid_3D.reshape((x_valid_3D.shape[0], -1))
    y_valid_oh = one_hot(y_valid, 10)

    layer_sizes = [256, 256, 10]
    activations = [tf.nn.tanh, tf.nn.tanh, None]
    alpha = 0.01
    iterations = 5000

    np.random.seed(0)
    save_path = train_mini_batch(x_train, y_train_oh, x_valid, y_valid_oh,
                                 epochs=10, load_path='./graph.ckpt',
                                 save_path='./model.ckpt')
    print('Model saved in path: {}'.format(save_path))