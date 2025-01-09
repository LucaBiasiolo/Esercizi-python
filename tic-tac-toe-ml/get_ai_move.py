import tensorflow as tf
import random
import numpy as np

def get_ai_random_move(game_matrix, machine_symbol):
    empty_spots = [(i, j) for i in range(3) for j in range(3) if game_matrix[i,j] == 0]
    return random.choice(empty_spots)

def get_model():
    return tf.keras.models.Sequential([
        tf.keras.layers.InputLayer((3,3)),
        tf.keras.layers.Dense(68, activation='relu'),
        tf.keras.layers.Dense(9)])
    
def train_model(model, epochs=1000):

    #to train the model, use q-learning withh epsilon-greedy strategy
    #1000 epochs, where every epoch is an entire game

    for game in range(epochs):
        pass

if __name__ == '__main__':
    model = get_model()
    model.save('./tic-tac-toe-ml/tic_tac_toe_mlp.keras')
    # Example 3x3 game matrix
    game_matrix = np.array([
        [0, 1, 0],
        [0, -1, 1],
        [1, 0, -1]
    ])

    # Reshape the game matrix to match the input shape (1, 3, 3) where 1 is the batch_size
    input_data = game_matrix.reshape(1, 3, 3)

    print(model(input_data).numpy())