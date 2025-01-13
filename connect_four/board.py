import numpy as np

def print_number_row():
  print("  1   2   3   4   5   6   7  ")

def print_horizontal_row():
  print("+---"*7+"+")

def print_vertical_row(board_row):
  if np.array_equal(board_row, np.full((1,7), '')):
    #just print the cell
    print("|   "*7 + "|")
  else:
    #print cell with Xs and Os inside
    row_to_print = ""
    for i in range(7):
        row_to_print += f"| {board_row[i]}  "
    row_to_print += "|"
    print(row_to_print)

def print_board(board):
  print_number_row()
  for i in range(6):
    print_horizontal_row()
    print_vertical_row(board[i])
  print_horizontal_row()

if __name__ == '__main__':
  board = np.full((6,7),'')

  board[0,6] = "X"
  board[5,6] = "O"
  print_board(board)
  