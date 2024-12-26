game_matrix = [[0,0,0],[0,0,0],[0,0,0]]

player_turn = 1
player_symbol = 'X'

while 0 in [cell for row in game_matrix for cell in row]:
    coordinates = input(f"Player {player_turn}, make your move. Where do you want to place your {player_symbol}? User row,col starting from 0: ")

    [x_coordinate, y_coordinate] = [int(coordinates.split(",")[0]), int(coordinates.split(",")[1])]

    if game_matrix[x_coordinate][y_coordinate] == 0:
        game_matrix[x_coordinate][y_coordinate] = player_symbol
    else:
        print("Cell already occupied. Please choose a different cell")

    for i in range(3):
        print(game_matrix[i])

    if player_turn ==1:
        player_turn = 2
        player_symbol = 'O'
    else:
        player_turn == 1
        player_symbol = 'X'