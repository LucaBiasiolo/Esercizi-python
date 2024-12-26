import unittest
import numpy
from esercizio_26 import check_winner

class TestTicTacToe(unittest.TestCase):

    def test_player_1_wins_diagonal_1(self):
        game_matrix = numpy.array([[1, 2, 0],
                                    [2, 1, 0],
                                    [2, 1, 1]])
        result = check_winner(game_matrix)
        self.assertEqual(result, "Player 1 wins")

    def test_player_2_wins_column(self):
        game_matrix = numpy.array([[2, 2, 0],
                                    [2, 1, 0],
                                    [2, 1, 1]])
        result = check_winner(game_matrix)
        self.assertEqual(result, "Player 2 wins")

    def test_player_1_wins_diagonal_2(self):
        game_matrix = numpy.array([[1, 2, 0],
                                    [2, 1, 0],
                                    [2, 1, 1]])
        result = check_winner(game_matrix)
        self.assertEqual(result, "Player 1 wins")
    
    def test_player_1_wins_column(self):
        game_matrix = numpy.array([[0, 1, 0],
                                    [2, 1, 0],
                                    [2, 1, 1]])
        result = check_winner(game_matrix)
        self.assertEqual(result, "Player 1 wins")

    def test_draw_1(self):
        game_matrix = numpy.array([[1, 2, 0],
                                    [2, 1, 0],
                                    [2, 1, 2]])
        result = check_winner(game_matrix)
        self.assertEqual(result, "It's a draw")

    def test_draw_2(self):
        game_matrix = numpy.array([[1, 2, 0],
                                    [2, 1, 0],
                                    [2, 1, 0]])
        result = check_winner(game_matrix)
        self.assertEqual(result, "It's a draw")

if __name__ == '__main__':
    unittest.main()