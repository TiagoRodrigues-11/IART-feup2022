import random



def initialize_board(Size):
    board = []
    for i in range(Size):
        row = []
        for j in range(Size):
            row.append(random.randint(0, 10))
        board.append(row)
    return board

def print_board(board):
    for row in board: 
        for piece in row:
            print(piece, end = " ")
        print()


def manhattan_distance(Pos1, Pos2):
    return abs(Pos1[0] - Pos2[0]) + abs(Pos1[1], Pos2[1])


if __name__ == "__main__":
    print(manhattan_distance(()))