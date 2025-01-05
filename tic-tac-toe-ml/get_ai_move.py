import random
import numpy
import tensorflow as tf
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Flatten, Input

def get_ai_move(game_matrix, machine_symbol):
    empty_spots = [(i, j) for i in range(3) for j in range(3) if game_matrix[i,j] == 0]
    return random.choice(empty_spots)

def get_model():
    # Placeholder for the neural network call
    # This function should return the coordinates (row, col) for the AI move
    model = Sequential([Dense(128, activation='relu', input_shape=(3,3)),
                        Dense(64, activation='relu'),
                        Dense(9, activation='linear')])
    
    model.compile(optimizer='adam',loss='mse')

    return model

if __name__ == '__main__':
    model = get_model()
    print(model(numpy.zeros((3,3), dtype=int)).numpy())