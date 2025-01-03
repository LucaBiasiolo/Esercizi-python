import numpy

def generate_row(n):
    return " --- " * n

def generate_void_column(n):
    return "|    " *(n+1)

def generate_full_column(symbol):
    return f"| {symbol} "

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

if __name__ == "__main__":
    n = int(input("Benvenuto nel generatore di griglie per giochi. Quante celle deve avere un lato della griglia? "))

    riga = generate_row(n)
    colonna = generate_void_column(n)

    griglia = ""
    for _ in range(n):
        griglia += riga + "\n" + colonna + "\n"

    griglia += riga #genero riga finale

    print(griglia)