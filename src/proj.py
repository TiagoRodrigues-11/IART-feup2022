import random


# INICIO DE ALGORITMOS # 

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

# FIM DE ALGORITMOS #
# INICIO DE OPERADORES #

def down(Pos, Board):
    if not (Pos[0] < len(Board)-1): return None
    if Board[Pos[0] + 1][Pos[1]] == 1: return None
    if not (Board[Pos[0] + 1][Pos[1]] == 0): return None
    Pos = (Pos[0] + 1, Pos[1])
    Board[Pos[0]][Pos[1]] = 1
    return Pos

def downL(Pos, Board, LVisit):
    if not (Pos[0] < len(Board)-1): return None
    if Board[Pos[0] + 1][Pos[1]] == 1: return None
    if not (Board[Pos[0] + 1][Pos[1]] in LVisit): return None
    Pos = (Pos[0] + 1, Pos[1])   
    LVisit.remove(Board[Pos[0]][Pos[1]])
    Board[Pos[0]][Pos[1]] = 1
    return Pos

def up(Pos, Board):
    if not (Pos[0] > 0): return None
    if Board[Pos[0] - 1][Pos[1]] == 1: return None
    if not (Board[Pos[0] - 1][Pos[1]] == 0): return None
    Pos = (Pos[0] - 1, Pos[1])
    Board[Pos[0]][Pos[1]] = 1
    return Pos

def upL(Pos, Board, LVisit):
    if not (Pos[0] > 0): return None
    if Board[Pos[0] - 1][Pos[1]] == 1: return None
    if not (Board[Pos[0] - 1][Pos[1]] in LVisit): return None
    Pos = (Pos[0] - 1, Pos[1])
    LVisit.remove(Board[Pos[0]][Pos[1]])
    Board[Pos[0]][Pos[1]] = 1
    return Pos

def left(Pos, Board):
    if not (Pos[1] > 0): return None
    if Board[Pos[0]][Pos[1]-1] == 1: return None
    if not (Board[Pos[0]][Pos[1]-1] == 0): return None
    Pos = (Pos[0], Pos[1]-1)
    Board[Pos[0]][Pos[1]] = 1
    return Pos

def leftL(Pos, Board, LVisit):
    if not (Pos[1] > 0): return None
    if Board[Pos[0]][Pos[1]-1] == 1: return None
    if not (Board[Pos[0]][Pos[1]-1] in LVisit): return None
    Pos = (Pos[0], Pos[1]-1)
    LVisit.remove(Board[Pos[0]][Pos[1]])
    Board[Pos[0]][Pos[1]] = 1
    return Pos

def right(Pos, Board):
    if not (Pos[1] > 0): return None
    if Board[Pos[0]][Pos[1]+1] == 1: return None
    if not (Board[Pos[0]][Pos[1]+1] == 0): return None
    Pos = (Pos[0], Pos[1]+1)
    Board[Pos[0]][Pos[1]] = 1
    return Pos

def rightL(Pos, Board, LVisit):
    if not (Pos[1] < len(Board[0]) - 1): return None
    if Board[Pos[0]][Pos[1]+1] == 1: return None
    if not (Board[Pos[0]][Pos[1]+1] in LVisit): return None
    Pos = (Pos[0], Pos[1]+1)
    LVisit.remove(Board[Pos[0]][Pos[1]])
    Board[Pos[0]][Pos[1]] = 1
    return Pos

# FIM DE OPERADORES

# INICIO DAS FUNÇÕES AUXILIARES # 
# operationsMaze -> Determina novos estados a partir do estado atual e operadores dados
def operationsMaze(state):
    operators = [down, downL, up, upL, left, leftL, right, rightL]
    q_res = []
    for op in operators:
        (accept, res) = op(state[0])
        if(accept and res not in q_res):
            q_res.append((res, state[1] + [state[0]]))

    return q_res

# finalBoard

def finalBoard(Pos, Board):
    if Pos[0] == 0 and Pos[1] == len(Board[0]) - 1: return True
    return False

def print_board(board):
    for row in board: 
        for piece in row:
            print(piece, end = " ")
        print()

def manhattan_distance(Pos1, Pos2):
    return abs(Pos1[0] - Pos2[0]) + abs(Pos1[1], Pos2[1])

# FIM DAS FUNÇÕES AUXILIARES

def initialize_board(Size):
    board = []
    for i in range(Size):
        row = []
        for j in range(Size):
            row.append(2)
        board.append(row)
    return board


if __name__ == "__main__":
    Board = initialize_board(5)
    Pos1 = (0, 0)
    Pos2 = (0 ,4)
    print(finalBoard(Pos1, Board))
    print(finalBoard(Pos2, Board))