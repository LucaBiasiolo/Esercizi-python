def draw_row(n):
    return " ---"*n
def draw_column(n):
    return "|   "*n

def draw_board(n):
    for _ in range(n):
        print(draw_row(n))
        print(draw_column(n) + "|")
    print(draw_row(n))

if __name__ == '__main__':
    draw_board(3)

    draw_board(8)

    draw_board(19)
