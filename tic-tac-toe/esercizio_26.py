import numpy

def check_game(game_matrix: numpy.ndarray[int]):
    transposed_game_matrix = game_matrix.transpose()

    diagonal = game_matrix.diagonal()

    anti_diagonal = numpy.fliplr(game_matrix).diagonal()

    for i in [1,2]: #loop over players indexes
        for j in range(3):
            #check rows
            if numpy.array_equal(game_matrix[j], numpy.array([i,i,i])):
                #player i wins
                return f"Player {i} wins"
            #check columns
            elif numpy.array_equal(transposed_game_matrix[j], numpy.array([i,i,i])):
                return f"Player {i} wins"
        #check diagonals
        if numpy.array_equal(diagonal,numpy.array([i,i,i])) or numpy.array_equal(anti_diagonal, numpy.array([i,i,i])):
            return f"Player {i} wins"
    
    return "It's a draw"

if __name__ == '__main__':
    game_matrix = numpy.array([[1, 2, 0],
                                [2, 1, 0],
                                [2, 1, 1]])
    print(check_game(game_matrix))