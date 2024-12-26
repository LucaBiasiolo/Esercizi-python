import numpy

def check_winner(game_matrix):
    transposed_game_matrix = game_matrix.transpose()

    diagonal = game_matrix.diagonal()

    anti_diagonal = numpy.array([game_matrix[2,0], game_matrix[1,1], game_matrix[0,2]])

    for i in range(3):
        #check rows
        if numpy.array_equal(game_matrix[i], numpy.array([1,1,1])):
            #player 1 wins
            return "Player 1 wins"
        elif numpy.array_equal(game_matrix[i], numpy.array([2,2,2])):
            #player 2 wins
            return "Player 2 wins"
        #check columns
        elif numpy.array_equal(transposed_game_matrix[i], numpy.array([1, 1, 1])):
            return "Player 1 wins"
        elif numpy.array_equal(transposed_game_matrix[i], numpy.array([2,2,2])):
            return "Player 2 wins"
    #check diagonals
    if numpy.array_equal(diagonal,numpy.array([1,1,1])) or numpy.array_equal(anti_diagonal, numpy.array([1,1,1])):
        return "Player 1 wins"
    elif numpy.array_equal(diagonal,numpy.array([2,2,2])) or numpy.array_equal(anti_diagonal, numpy.array([2,2,2])):
        return "Player 2 wins"
    return "It's a draw"

if __name__ == '__main__':
    game_matrix = numpy.array([[1, 2, 0],
                                [2, 1, 0],
                                [2, 1, 1]])
    print(check_winner(game_matrix))