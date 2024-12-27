import numpy
from esercizio_26 import check_game

while True: #loop for playing game
    game_matrix = [[0,0,0],[0,0,0],[0,0,0]]

    player_turn = 1
    player_symbol = 'X'
    while True: #loop for players' turns

        coordinates = input(f"Player {player_turn}, make your move. Where do you want to place your {player_symbol}? User row,col starting from 0: ")

        [x_coordinate, y_coordinate] = [int(coordinates.split(",")[0]), int(coordinates.split(",")[1])]

        if game_matrix[x_coordinate][y_coordinate] == 0:
            game_matrix[x_coordinate][y_coordinate] = player_turn
        else:
            print("Cell already occupied. Please choose a different cell")

        for i in range(3):
            print(game_matrix[i]) #print game board with fake graphics
            
        #check if someone won the game
        found_winner: str = check_game(numpy.array(game_matrix))
        if found_winner.startswith("Player"):
            print(found_winner)
            break
        
        game_still_playable = False
        for i in range(3):
            for j in range(3):
                if game_matrix[i][j] == 0:
                    game_still_playable = True

        if not game_still_playable:
            print("It's a draw")
            break

        if player_turn ==1:
            player_turn = 2
            player_symbol = 'O'
        elif player_turn ==2:
            player_turn = 1
            player_symbol = 'X'

    play_again = input("Do you want to play again? y/n: ")
    if play_again == 'n':
        break

#TODO: print game board with fake graphics
#TODO: refactor check_winner
#TODO: stampare parità in anticipo quando non è più possibile che qualcuno vinca
#TODO: move draw logic in check_winner
#TODO: idea per progetto: tic-tac-toe con machine learning e intelligenza artificiale, giocare contro il PC
