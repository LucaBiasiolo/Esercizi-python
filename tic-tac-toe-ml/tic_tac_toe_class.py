import numpy as np
from check_game import check_game

class TicTacToe():

    def __init__(self):
        self.game_board = np.zeros((3,3))
        self.ended = False

    def step(self, coordinates):
        if coordinates:
            self.game_board[coordinates[0], coordinates[1]] = 1
        else:
            empty_spots = [(i, j) for i in range(3) for j in range(3) if self.game_board[i,j] == 0]
            random_choice = np.random.choice(empty_spots)
            self.game_board[random_choice[0], random_choice[1]] = 1

        
