import unittest
import numpy
from esercizio_26 import check_game

class TestTicTacToe(unittest.TestCase):

    def test_player_1_wins_diagonal_1(self):
        game_matrix = numpy.array([[1, 2, 0],
                                    [2, 1, 0],
                                    [2, 1, 1]])
        result = check_game(game_matrix)
        self.assertEqual(result, 1)

    def test_player_2_wins_column(self):
        game_matrix = numpy.array([[2, 2, 0],
                                    [2, 1, 0],
                                    [2, 1, 1]])
        result = check_game(game_matrix)
        self.assertEqual(result, 2)

    def test_player_1_wins_diagonal_2(self):
        game_matrix = numpy.array([[1, 2, 0],
                                    [2, 1, 0],
                                    [2, 1, 1]])
        result = check_game(game_matrix)
        self.assertEqual(result, 1)
    
    def test_player_1_wins_column(self):
        game_matrix = numpy.array([[0, 1, 0],
                                    [2, 1, 0],
                                    [2, 1, 1]])
        result = check_game(game_matrix)
        self.assertEqual(result, 1)

    def test_draw_1(self):
        game_matrix = numpy.array([[1, 2, 0],
                                    [2, 1, 0],
                                    [2, 1, 2]])
        result = check_game(game_matrix)
        self.assertEqual(result, None)

    def test_draw_2(self):
        game_matrix = numpy.array([[1, 2, 0],
                                    [2, 1, 0],
                                    [2, 1, 0]])
        result = check_game(game_matrix)
        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()