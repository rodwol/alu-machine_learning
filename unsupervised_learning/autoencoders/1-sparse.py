#!/usr/bin/env python3
"""
sparse autoencoder using L1 activity regularization on the latent layer
"""
import tensorflow as tf
from tensorflow.keras import layers, Model, regularizers


def autoencoder(input_dims, hidden_layers, latent_dims, lambtha):
    """
    Creates a sparse autoencoder.
    """

    # ----- Encoder -----
    input_layer = layers.Input(shape=(input_dims,))
    x = input_layer
    for nodes in hidden_layers:
        x = layers.Dense(nodes, activation='relu')(x)
    latent = layers.Dense(latent_dims,
                          activation='relu',
                          activity_regularizer=regularizers.l1(lambtha))(x)
    encoder = Model(inputs=input_layer, outputs=latent, name="encoder")

    # ----- Decoder -----
    latent_inputs = layers.Input(shape=(latent_dims,))
    x = latent_inputs
    for nodes in reversed(hidden_layers):
        x = layers.Dense(nodes, activation='relu')(x)
    output_layer = layers.Dense(input_dims, activation='sigmoid')(x)
    decoder = Model(inputs=latent_inputs, outputs=output_layer, name="decoder")

    # ----- Autoencoder -----
    auto_input = layers.Input(shape=(input_dims,))
    encoded = encoder(auto_input)
    decoded = decoder(encoded)
    auto = Model(inputs=auto_input, outputs=decoded, name="autoencoder")

    # Compile with Adam optimizer + binary crossentropy
    auto.compile(optimizer='adam', loss='binary_crossentropy')

    return encoder, decoder, auto
