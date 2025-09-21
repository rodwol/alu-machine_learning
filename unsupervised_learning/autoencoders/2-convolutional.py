#!/usr/bin/env python3
"""
convolutional autoencoder with symmetric encoder/decoder
"""
import tensorflow as tf
from tensorflow.keras import layers, Model


def autoencoder(input_dims, filters, latent_dims):
    """
    Creates a convolutional autoencoder.
    """

    # ----- Encoder -----
    input_layer = layers.Input(shape=input_dims)
    x = input_layer
    for f in filters:
        x = layers.Conv2D(filters=f, kernel_size=(3, 3),
                          padding="same", activation="relu")(x)
        x = layers.MaxPooling2D(pool_size=(2, 2), padding="same")(x)
    # Latent space
    shape_before_flatten = x.shape[1:]  # save for decoder reshaping
    x = layers.Flatten()(x)
    latent = layers.Dense(tf.math.reduce_prod(latent_dims),
                          activation="relu")(x)
    latent = layers.Reshape(latent_dims)(latent)
    encoder = Model(inputs=input_layer, outputs=latent, name="encoder")

    # ----- Decoder -----
    latent_inputs = layers.Input(shape=latent_dims)
    x = latent_inputs
    x = layers.Flatten()(x)
    x = layers.Dense(tf.math.reduce_prod(shape_before_flatten),
                                         activation="relu")(x)
    x = layers.Reshape(shape_before_flatten)(x)

    for i, f in enumerate(reversed(filters)):
        if i < len(filters) - 1:  # all but last two
            x = layers.Conv2D(filters=f, kernel_size=(3, 3),
                              padding="same", activation="relu")(x)
            x = layers.UpSampling2D(size=(2, 2))(x)
        elif i == len(filters) - 1:  # second-to-last conv
            x = layers.Conv2D(filters=f, kernel_size=(3, 3),
                padding="valid", activation="relu")(x)

    # Last layer (reconstruction)
    output_layer = layers.Conv2D(filters=input_dims[-1], kernel_size=(3, 3),
                                 padding="same", activation="sigmoid")(x)
    decoder = Model(inputs=latent_inputs, outputs=output_layer,
              name="decoder")

    # ----- Autoencoder -----
    auto_input = layers.Input(shape=input_dims)
    encoded = encoder(auto_input)
    decoded = decoder(encoded)
    auto = Model(inputs=auto_input, outputs=decoded, name="autoencoder")

    # Compile model
    auto.compile(optimizer="adam", loss="binary_crossentropy")

    return encoder, decoder, auto
