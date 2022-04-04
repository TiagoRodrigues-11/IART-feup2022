import random

# Falta refinar mas a base dos algoritmos estão aqui

# Depth-First Search
# initial_state = (Estado Atual = pos, path até ao estado atual)
# process_items = função que da todos os novos estados depois de usar operadores
# final_items = função da check se chegou no final
def dfs(initial_state, process_items, final_items):
    stack = [initial_state]
    visited_items = []

    while len(stack) > 0:

        state = stack.pop()
        if state[0] not in visited_items:
            visited_items.append(state[0])
            new_items = process_items(state)
            for i in new_items:
                if final_items(i[0]):
                    return i
                stack.append(i)
    return -1



# Breadth-First Search
def bfs(initial_state, process_items, final_items):
    queue = [initial_state]

    existing_items = [initial_state] # Performance purposes
    while len(queue):
        temp_state = queue.pop(0)

        new_items = process_items(temp_state)

        for item in new_items:
            if item not in existing_items: 
                queue.append(item)
                existing_items.append(item)
            if final_items(item[0]):
                return item
    
    return -1



def initialize_board(Size):
    board = []
    for i in range(Size):
        row = []
        for j in range(Size):
            row.append(2)
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
    Board = initialize_board(5)
    LVisit = [2, 3, 4]
    pos = (2, 2)
    print(downL(pos, Board, LVisit))
    print(pos)
    print(LVisit)
    print_board(Board)