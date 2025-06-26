import tensorflow as tf
from tensorflow.keras import layers, Model, Input

def build_base_network(input_shape):
    input = Input(shape=input_shape)
    x = layers.Conv2D(64, (3, 3), activation='relu')(input)
    x = layers.MaxPooling2D()(x)
    x = layers.Conv2D(128, (3, 3), activation='relu')(x)
    x = layers.MaxPooling2D()(x)
    x = layers.Flatten()(x)
    x = layers.Dense(128, activation='relu')(x)
    return Model(input, x)

input_shape = (100, 100, 1)  # Grayscale image 100x100
base_network = build_base_network(input_shape)
base_network.summary()
