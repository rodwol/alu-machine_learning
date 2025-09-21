#!/usr/bin/env python3
""" Variational Autoencoder"""

import tensorflow.keras as keras


def autoencoder(input_dims, hidden_layers, latent_dims):
    """
    function that creates a variational autoencoder
    """

    # Encoder
    X_input = keras.Input(shape=(input_dims,))
    Y_prev = X_input
    for units in hidden_layers:
        Y_prev = keras.layers.Dense(units=units, activation='relu')(Y_prev)

    # Latent layers
    z_mean = keras.layers.Dense
             (units=latent_dims, activation='linear')(Y_prev)
    z_log_sigma = keras.layers.Dense
                  (units=latent_dims, activation='linear')(Y_prev)

    def sampling(args):
        """Sampling similar points in latent space"""
        z_m, z_stand_des = args
        batch = keras.backend.shape(z_m)[0]
        dim = keras.backend.int_shape(z_m)[1]
        epsilon = keras.backend.random_normal(shape=(batch, dim))
        return z_m + keras.backend.exp(z_stand_des / 2) * epsilon

    z = keras.layers.Lambda(sampling, output_shape=(latent_dims,))
        ([z_mean, z_log_sigma])

    encoder = keras.Model(X_input, [z, z_mean, z_log_sigma])

    # Decoder
    X_decode = keras.Input(shape=(latent_dims,))
    Y_prev = X_decode
    for units in reversed(hidden_layers):
        Y_prev = keras.layers.Dense(units=units, activation='relu')(Y_prev)
    output = keras.layers.Dense(units=input_dims, activation='sigmoid')
             (Y_prev)
    decoder = keras.Model(X_decode, output)

    # Autoencoder
    z_sample, _, _ = encoder(X_input)
    d_output = decoder(z_sample)
    auto = keras.Model(X_input, d_output)

    # Loss function
    def vae_loss(x, x_decoder_mean):
        x_loss = keras.backend.binary_crossentropy(x, x_decoder_mean)
        x_loss = keras.backend.sum(x_loss, axis=1)
        kl_loss = - 0.5 * keras.backend.mean(
            1 + z_log_sigma - keras.backend.square(z_mean)
            - keras.backend.exp(z_log_sigma),
            axis=-1
        )
        return x_loss + kl_loss

    auto.compile(loss=vae_loss, optimizer='adam')

    return encoder, decoder, auto
