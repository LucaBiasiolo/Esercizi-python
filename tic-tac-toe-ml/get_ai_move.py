import tensorflow as tf
import random
import numpy as np
from tic_tac_toe_class import TicTacToe
from check_game import check_game

def get_ai_random_move(game_matrix):
    empty_spots = [(i, j) for i in range(3) for j in range(3) if game_matrix[i,j] == 0]
    return random.choice(empty_spots)

def get_model():
    return tf.keras.models.Sequential([
        tf.keras.layers.InputLayer((3,3)),
        tf.keras.layers.Dense(68, activation='relu'),
        tf.keras.layers.Dense(9)])
    
def train_model(model, epochs=1000, epsilon=0.9, gamma=0.95, alpha=0.8):

    #epsilon is the probability of exploring a random state, while 1-epsilon the probability of exploiting current known strategies
    #gamma is the discount factor, which takes into account future rewards
    #alpha is the learning rate, the rate at which new information acquired by the model overrides old information
    #TODO: first implement tic-tac-toe with q-learning without using MLP

    for _ in range(epochs):
        tic_tac_toe = TicTacToe()
        
        game_ended = False
        while not game_ended:
            if np.random.random() > epsilon:
                #explore a random state
                tic_tac_toe.step()
            else:
                #exploit
                predicted_step = np.argmax(model.predict(tic_tac_toe.game_board).numpy())
                tic_tac_toe.step(predicted_step)
            
            winner = check_game(tic_tac_toe.game_board)
            if winner:
                game_ended = True
                reward = 0 #TODO: how do i use the reward?
                if winner == 1:
                    reward = 1
                elif winner == 2:
                    reward = -1

    tf.save(model, './Esercizi/tic-tac-toe-ml/tic_tac_toe_mlp.keras')
        

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