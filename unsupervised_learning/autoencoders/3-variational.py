#!/usr/bin/env python3
"""
Variational Autoencoder (VAE) implementation in Keras
"""
import tensorflow as tf


def autoencoder(input_dims, hidden_layers, latent_dims):
    """
    Creates a variational autoencoder (VAE).
    """

    # ----- Encoder -----
    inputs = keras.Input(shape=(input_dims,))
    x = inputs
    for nodes in hidden_layers:
        x = keras.layers.Dense(nodes, activation="relu")(x)

    # Latent distribution layers
    z_mean = keras.layers.Dense(latent_dims, activation=None)(x)
    z_log_var = keras.layers.Dense(latent_dims, activation=None)(x)

    # Reparameterization trick
    def sampling(args):
        z_mean, z_log_var = args
        epsilon = keras.backend.random_normal(
            shape=(keras.backend.shape(z_mean)[0], latent_dims),
            mean=0.0, stddev=1.0
        )
        return z_mean + keras.backend.exp(0.5 * z_log_var) * epsilon

    z = keras.layers.Lambda(sampling, output_shape=(latent_dims,)
        ([z_mean, z_log_var])

    encoder = keras.Model(inputs, [z, z_mean, z_log_var], name="encoder")

    # ----- Decoder -----
    latent_inputs = keras.Input(shape=(latent_dims,))
    x = latent_inputs
    for nodes in reversed(hidden_layers):
        x = keras.layers.Dense(nodes, activation="relu")(x)
    outputs = keras.layers.Dense(input_dims, activation="sigmoid")(x)

    decoder = keras.Model(latent_inputs, outputs, name="decoder")

    # ----- Autoencoder -----
    z, z_mean, z_log_var = encoder(inputs)
    reconstructed = decoder(z)
    auto = keras.Model(inputs, reconstructed, name="vae")

    # ----- Loss -----
    # Reconstruction loss
    reconstruction_loss = keras.losses.binary_crossentropy(inputs, reconstructed)
    reconstruction_loss = keras.backend.sum(reconstruction_loss, axis=1)

    # KL divergence loss
    kl_loss = -0.5 * keras.backend.sum(
        1 + z_log_var - keras.backend.square(z_mean)
        - keras.backend.exp(z_log_var),
        axis=1
    )

    # Total VAE loss
    vae_loss = keras.backend.mean(reconstruction_loss + kl_loss)
    auto.add_loss(vae_loss)

    auto.compile(optimizer="adam")

    return encoder, decoder, auto
