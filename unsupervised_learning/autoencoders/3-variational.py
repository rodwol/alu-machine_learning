#!/usr/bin/env python3
"""
Variational Autoencoder (VAE) implementation in Keras
"""
import tensorflow as tf
from tensorfow.keras import layers, Model, backend as K


def autoencoder(input_dims, hidden_layers, latent_dims):
    """
    Creates a variational autoencoder (VAE).
    """

    # ----- Encoder -----
    inputs = layers.Input(shape=(input_dims,))
    x = inputs
    for nodes in hidden_layers:
        x = layers.Dense(nodes, activation="relu")(x)

    # Latent distribution
    z_mean = layers.Dense(latent_dims, activation=None)(x)
    z_log_var = layers.Dense(latent_dims, activation=None)(x)

    # Reparameterization trick
    def sampling(args):
        z_mean, z_log_var = args
        epsilon = K.random_normal(shape=(K.shape(z_mean)[0], latent_dims),
                                  mean=0., stddev=1.0)
        return z_mean + K.exp(0.5 * z_log_var) * epsilon

    z = layers.Lambda(sampling, output_shape=(latent_dims,)
        ([z_mean, z_log_var])

    encoder = Model(inputs, [z, z_mean, z_log_var], name="encoder")

    # ----- Decoder -----
    latent_inputs = layers.Input(shape=(latent_dims,))
    x = latent_inputs
    for nodes in reversed(hidden_layers):
        x = layers.Dense(nodes, activation="relu")(x)
    outputs = layers.Dense(input_dims, activation="sigmoid")(x)

    decoder = Model(latent_inputs, outputs, name="decoder")

    # ----- VAE (Autoencoder) -----
    z, z_mean, z_log_var = encoder(inputs)
    reconstructed = decoder(z)
    auto = Model(inputs, reconstructed, name="vae")

    # ----- Loss Function -----
    # Reconstruction loss
    reconstruction_loss = tf.keras.losses.binary_crossentropy
                         (inputs, reconstructed)
    reconstruction_loss = K.sum(reconstruction_loss, axis=1)

    # KL divergence
    kl_loss = -0.5 * K.sum(1 + z_log_var - K.square(z_mean)
              - K.exp(z_log_var), axis=1)

    # Total loss
    vae_loss = K.mean(reconstruction_loss + kl_loss)
    auto.add_loss(vae_loss)

    auto.compile(optimizer="adam")

    return encoder, decoder, auto
