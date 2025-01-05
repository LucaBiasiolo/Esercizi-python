import random
import numpy
from draw_game_board import draw_game_board
from get_ai_move import get_ai_move

print("Hello, i'm Python. Welcome to tic-tac-toe game. You will play against the AI")

player_number = random.randint(1,2)

print(f"Human player, you have been assigned player number {player_number}")

machine_number = 0
if player_number == 1:
    machine_number = 2

    player_symbol = 'X'
    machine_symbol = 'O'
else:
    machine_number = 1

    player_symbol = 'O'
    machine_symbol = 'X'

game_matrix = numpy.array([[0,0,0],[0,0,0],[0,0,0]])

#first turn
while True:
    if machine_number == 1:
        #AI starts first
        ai_coordinates = get_ai_move(game_matrix, machine_symbol)
        print(f"AI places {machine_symbol} at {ai_coordinates}")
        game_matrix[ai_coordinates[0], ai_coordinates[1]] = machine_number
        print(draw_game_board(game_matrix))

        player_coordinates = input(f"Human player, make your move. Where do you want to place your {player_symbol}? Use row,col starting from 1: ")
        [player_x_coordinate, player_y_coordinate] = [int(player_coordinates.split(",")[0]), int(player_coordinates.split(",")[1])]

    else:
        #player first
        player_coordinates = input(f"Human player, make your move. Where do you want to place your {player_symbol}? Use row,col starting from 1: ")
        [player_x_coordinate, player_y_coordinate] = [int(player_coordinates.split(",")[0]), int(player_coordinates.split(",")[1])]

        if game_matrix[player_x_coordinate-1, player_y_coordinate-1] != 0:
            game_matrix[player_x_coordinate-1, player_y_coordinate-1] = player_number
        else:
            print("Cell already occupied. Please select another cell")

        ai_coordinates = get_ai_move(game_matrix, machine_symbol)
        print(f"AI places {machine_symbol} at {ai_coordinates}")
        game_matrix[ai_coordinates[0],ai_coordinates[1]] = machine_number
        print(draw_game_board(game_matrix))
    

#TODO:draw game board using pygame