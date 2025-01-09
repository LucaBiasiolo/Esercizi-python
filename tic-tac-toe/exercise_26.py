import numpy

def check_game(game_matrix: numpy.ndarray[int]):
    """
    Check the status of a tic-tac-toe game.

    Parameters:
    game_matrix (numpy.ndarray[int]): A 3x3 numpy array representing the game board.
                                       1 represents player 1's move, 2 represents player 2's move,
                                       and 0 represents an empty cell.

    Returns:
    int: The result of the game.
         1 if player 1 wins,
         2 if player 2 wins,
         0 if the game is a draw,
         None if the game is still ongoing.
    """

    transposed_game_matrix = game_matrix.transpose()

    diagonal = game_matrix.diagonal()

    anti_diagonal = numpy.fliplr(game_matrix).diagonal()

    for i in [1,2]: #loop over players indexes
        for j in range(3):
            #check rows
            if numpy.array_equal(game_matrix[j], numpy.array([i,i,i])):
                #player i wins
                return i
            #check columns
            elif numpy.array_equal(transposed_game_matrix[j], numpy.array([i,i,i])):
                return i
        #check diagonals
        if numpy.array_equal(diagonal,numpy.array([i,i,i])) or numpy.array_equal(anti_diagonal, numpy.array([i,i,i])):
            return i
    
    #if board does not have zeros, the game is in a draw condition
    if not game_matrix.min() == 0:
        return 0 

if __name__ == '__main__':
    game_matrix = numpy.array([[1, 2, 0],
                                [2, 1, 0],
                                [2, 1, 1]])
    print(check_game(game_matrix))