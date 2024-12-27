import numpy
from esercizio_26 import check_game
from esercizio_24 import draw_game_board

while True: #loop for playing game
    print("Hi, i'm Python. Welcome to tic-tac-toe game")
    game_matrix = numpy.array([[0,0,0],[0,0,0],[0,0,0]])

    player_turn = 1
    player_symbol = 'X'
    while True: #loop for players' turns

        coordinates = input(f"Player {player_turn}, make your move. Where do you want to place your {player_symbol}? User row,col starting from 1: ")

        [x_coordinate, y_coordinate] = [int(coordinates.split(",")[0]), int(coordinates.split(",")[1])]

        if game_matrix[x_coordinate-1, y_coordinate-1] == 0:
            game_matrix[x_coordinate-1, y_coordinate-1] = player_turn

            print(draw_game_board(game_matrix)) #print game board with fake graphics

            winner_player: int = check_game(numpy.array(game_matrix))#check if someone won the game
            if winner_player in [1,2]:
                print(f"Player {winner_player} wins")
                break

            #check for draw condition
            elif winner_player == 0:
                print("It's a draw")
                break

            if player_turn ==1:
                player_turn = 2
                player_symbol = 'O'
            elif player_turn ==2:
                player_turn = 1
                player_symbol = 'X'
        else:
            print("Cell already occupied. Please choose a different cell")

    play_again = input("Do you want to play again? y/n: ")
    if play_again == 'n':
        break

#TODO: improve logic of fake graphics
#TODO: stampare parità in anticipo quando non è più possibile che qualcuno vinca
#TODO: idea per progetto: tic-tac-toe con machine learning e intelligenza artificiale, giocare contro il PC
