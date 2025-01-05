import numpy

def draw_game_board(game_matrix: numpy.ndarray[int]):

    first_row_cells = ""
    for i in range(3):
        if game_matrix[0,i] == 0:
            first_row_cells += "|    "
        elif game_matrix[0,i] == 1:
            first_row_cells += "| X  "
        else:
            first_row_cells += "| O  "

    second_row_cells = ""
    for i in range(3):
        if game_matrix[1,i] == 0:
            second_row_cells += "|    "
        elif game_matrix[1,i] == 1:
            second_row_cells += "| X  "
        else:
            second_row_cells += "| O  "
    
    third_row_cells = ""
    for i in range(3):
        if game_matrix[2,i] == 0:
            third_row_cells += "|    "
        elif game_matrix[2,i] == 1:
            third_row_cells += "| X  "
        else:
            third_row_cells += "| O  "

    return f"""
 ---  ---  --- 
{first_row_cells}|
 ---  ---  --- 
{second_row_cells}|
 ---  ---  --- 
{third_row_cells}|
 ---  ---  --- 
"""