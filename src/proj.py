import copy
import json
import sys
import time

# INICIO DE OPERADORES #

def down(state):
    # Pre Condition
    if not (state.pos[0] < len(state.board)-1): return None
    if not (state.board[state.pos[0] + 1][state.pos[1]] == 0): return None
    
    # Create and Return New State
    newState = copy.deepcopy(state)
    newState.pos = (newState.pos[0] + 1, newState.pos[1])
    newState.board[newState.pos[0]][newState.pos[1]] = 1

    return newState

def downL(state):
    # Pre Conditions
    if not (state.pos[0] < len(state.board)-1): return None
    if not (state.board[state.pos[0] + 1][state.pos[1]] in state.lVisit): return None

    # Create and Return New State
    newState = copy.deepcopy(state)
    newState.pos = (newState.pos[0] + 1, newState.pos[1])
    newState.lVisit.remove(newState.board[newState.pos[0]][newState.pos[1]])
    newState.board[newState.pos[0]][newState.pos[1]] = 1
   
    return newState

def up(state):
    # Pre Conditions
    if not (state.pos[0] > 0): return None
    if not (state.board[state.pos[0] - 1][state.pos[1]] == 0): return None

    # Create and Return New State
    newState = copy.deepcopy(state)
    newState.pos = (newState.pos[0] - 1, newState.pos[1])
    newState.board[newState.pos[0]][newState.pos[1]] = 1

    return newState
    
    
def upL(state):
    # Pre Conditions
    if not (state.pos[0] > 0): return None
    if not (state.board[state.pos[0] - 1][state.pos[1]] in state.lVisit): return None

    # Create and Return New State
    newState = copy.deepcopy(state)
    newState.pos = (newState.pos[0] - 1, newState.pos[1])
    newState.lVisit.remove(newState.board[newState.pos[0]][newState.pos[1]])
    newState.board[newState.pos[0]][newState.pos[1]] = 1

    return newState

def left(state):
    # Pre Conditions
    if not (state.pos[1] > 0): return None
    if not (state.board[state.pos[0]][state.pos[1]-1] == 0): return None

    # Create and Return New State
    newState = copy.deepcopy(state)
    newState.pos = (newState.pos[0], newState.pos[1] - 1)
    newState.board[newState.pos[0]][newState.pos[1]] = 1
    
    return newState

def leftL(state):
    # Pre Conditions
    if not (state.pos[1] > 0): return None
    if not (state.board[state.pos[0]][state.pos[1]-1] in state.lVisit): return None

    # Create and Return New State
    newState = copy.deepcopy(state)
    newState.pos = (newState.pos[0], newState.pos[1] - 1)
    newState.lVisit.remove(newState.board[newState.pos[0]][newState.pos[1]])
    newState.board[newState.pos[0]][newState.pos[1]] = 1
    
    return newState

def right(state):
    # Pre Conditions
    if not (state.pos[1] < len(state.board[0]) - 1): return None
    if not (state.board[state.pos[0]][state.pos[1]+1] == 0): return None

    # Create and Return New State
    newState = copy.deepcopy(state)
    newState.pos = (newState.pos[0], newState.pos[1] + 1)
    newState.board[newState.pos[0]][newState.pos[1]] = 1
    
    return newState

def rightL(state):
    # Pre Conditions
    if not (state.pos[1] < len(state.board[0]) - 1): return None
    if not (state.board[state.pos[0]][state.pos[1]+1] in state.lVisit): return None

    # Create and Return New State
    newState = copy.deepcopy(state)
    newState.pos = (newState.pos[0], newState.pos[1] + 1)
    newState.lVisit.remove(newState.board[newState.pos[0]][newState.pos[1]])
    newState.board[newState.pos[0]][newState.pos[1]] = 1
    
    return newState

# FIM DE OPERADORES
# INICIO DA CLASS NODE

class State:
    def __init__(self, board, pos, lVisit):
        self.board = board              # Array de Array
        self.pos = pos                  # Tuple
        self.lVisit = lVisit            # Lista

    def __eq__(self, other):
        if(other == None): return False
        if(self.board != other.board): return False
        elif(self.pos != other.pos): return False
        elif(self.lVisit != other.lVisit): return False
        else: return True

class Node:
    def __init__(self, state, parent = None, depth=0):
        self.state = state
        self.parent = parent
        self.depth = depth

    def __eq__(self, other):
        if(other == None): return False
        if(self.state == other.state): return True
        else: return False

    # operationsMaze -> Determina novos estados a partir do estado atual e operadores dados
    def operationsMaze(node):
        operators = [down, downL, up, upL, left, leftL, right, rightL]
        q_res = []
        for op in operators:
            new_state = op(node.state)
            if(new_state != None):
                new_node = Node(new_state, node, node.depth + 1)
                if(new_node not in q_res):
                    q_res.append(new_node)

        return q_res[::-1]

    def getPath(self):
        path = [self.state.pos]
        curr_node = self

        while(curr_node.parent != None):
            curr_node = curr_node.parent
            path.append(curr_node.state.pos)
        
        path.reverse()
        return path

# FIM DA CLASS NODE
# INICIO DE ALGORITMOS # 

# Probably wrong
# Depth-First Search
def dfs(initial_state, limit_depth = sys.maxsize):
    initial_node = Node(initial_state)
    stack = [initial_node]
    visited_nodes = []

    while len(stack) > 0:
        curr_node = stack.pop()

        if curr_node not in visited_nodes:
            visited_nodes.append(curr_node)

            if(solution(curr_node)):
                print(curr_node.state.pos)
                print(curr_node.state.lVisit)
                print_board(curr_node.state.board)
                return curr_node.getPath()

            if(curr_node.depth <= limit_depth):
                new_nodes = curr_node.operationsMaze()
                for node in new_nodes:
                    stack.append(node)
    
    return []

# Breadth-First Search
def bfs(initial_state):
    initial_node = Node(initial_state)
    queue = [initial_node]
    visited_nodes = [] # Performance purposes
    
    while len(queue):
        curr_node = queue.pop(0)
        visited_nodes.append(curr_node)
        
        if(solution(curr_node)):
            print(curr_node.state.pos)
            print(curr_node.state.lVisit)
            print_board(curr_node.state.board)
            return curr_node.getPath()

        new_nodes = curr_node.operationsMaze()
        for node in new_nodes:
            if node not in visited_nodes:
                queue.append(node)
    
    return []

def greedy_search(initial_state, h):
    initial_node = Node(initial_state)
    stack = [initial_node]
    visited_nodes = []

    while len(stack):
        curr_node = stack.pop()

        if curr_node not in visited_nodes:
            visited_nodes.append(curr_node)

            if(solution(curr_node)):
                print(curr_node.state.pos)
                print(curr_node.state.lVisit)
                print_board(curr_node.state.board)
                return curr_node.getPath()
            
            new_nodes = curr_node.operationsMaze()
            new_nodes.sort(reverse=True, key=h)
            for node in new_nodes:
                stack.append(node)

    return []

def uniform(initialState):
    initialNode = Node(initialState)
    queue = [(initialNode, 0)]
    visitedNodes = []

    while len(queue):
        queue.sort(key=lambda tup: tup[1])
        (currNode, currCost) = queue.pop(0)

        visitedNodes.append(currNode)
        if solution(currNode):
            print(currNode.state.pos)
            print(currNode.state.lVisit)
            print_board(currNode.state.board)
            return currNode.getPath()
        
        newNodes = currNode.operationsMaze()
        for node in newNodes:
            if node not in visitedNodes:
                queue.append((node, currCost + cost()))
    
    return []

# Iterative deepening
def iterative_deepening(initial_state):
    path = []
    depth = 0
    while(len(path) == 0):
        path = dfs(initial_state, depth)
        depth += 1
    
    print("Depth:", end=" ")
    print(depth)
    return path
    
# FIM DE ALGORITMOS #

# HEURISTIC FUNCTIONS

def h_1(node):
    curr_pos = node.state.pos
    target_pos = (0, len(node.state.board) - 1)
    return manhattan_distance(curr_pos, target_pos)

# END HEURISTIC FUNCTIONS

# INICIO DAS FUNÇÕES AUXILIARES # 

def solution(node):
    state = copy.deepcopy(node.state)
    if(len(state.lVisit) == 0):
        if(state.pos[0] == 0):
            if(state.pos[1] == (len(state.board) - 1)):
                if(state.board[state.pos[0]][state.pos[1]] == 1):
                    return True
    return False

def cost():
    return 1

# finalBoard
def finalBoard(state):
    if state.pos[0] == 0 and state.pos[1] == len(state.board[0]) - 1: return True
    return False

# Prints the 'board' provided
def print_board(board):
    for row in board: 
        for piece in row:
            print(piece, end = " ")
        print()

def manhattan_distance(Pos1, Pos2):
    return abs(Pos1[0] - Pos2[0]) + abs(Pos1[1] - Pos2[1])

def compare_algorithms(initial_state):
    #bfs
    start = time.time()
    bfs(initial_state)
    end = time.time()
    print("BFS:", end=" ")
    print(end - start)

    #dfs
    start = time.time()
    dfs(initial_state)
    end = time.time()
    print("DFS:", end=" ")
    print(end - start)

    #iterative_deepening
    start = time.time()
    iterative_deepening(initial_state)
    end = time.time()
    print("Iterative Deepening:", end=" ")
    print(end - start)

    #uniform cost
    start = time.time()
    uniform(initial_state)
    end = time.time()
    print("Uniform Cost:", end=" ")
    print(end - start)
    
    #greedy search
    start = time.time()
    greedy_search(initial_state, h_1)
    end = time.time()
    print("Greedy Search:", end=" ")
    print(end - start)
    
    '''
    #A*
    start = time.time()
    bfs(initial_state)
    end = time.time()
    print("A*:", end=" ")
    print(end - start)
    '''

# FIM DAS FUNÇÕES AUXILIARES

def initialize_board(board):
    Pos = ()
    LVisit = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                Pos = (i, j)
            elif not (board[i][j] == 0) and not (board[i][j] in LVisit):
                LVisit.add(board[i][j])
    state = State(board, Pos, LVisit)
    return state
    

if __name__ == "__main__":
    f = open('./boards.json')
    boards = json.load(f)
    f.close()

    state = initialize_board(boards[0])
    print("init:", end=" ")
    print(state.lVisit)
    compare_algorithms(state)

    