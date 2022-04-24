import copy
import csv
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
    numberL = 0

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
        queueRes = []
        for op in operators:
            newState = op(node.state)
            if(newState != None):
                newNode = Node(newState, node, node.depth + 1)
                if(newNode not in queueRes):
                    queueRes.append(newNode)

        return queueRes

    def getPath(self):
        path = [self.state.pos]
        currNode = self

        while(currNode.parent != None):
            currNode = currNode.parent
            path.append(currNode.state.pos)
        
        path.reverse()
        return path

# FIM DA CLASS NODE
# INICIO DE ALGORITMOS # 

# Depth-First Search
def dfs(initialState, limitDepth = sys.maxsize):
    initialNode = Node(initialState)
    stack = [initialNode]
    visitedNodes = []

    while len(stack) > 0:
        currNode = stack.pop()
        
        visit = False
        # Iterative Deepening - Visit nodes already visited when they're further up in the tree
        if(limitDepth != sys.maxsize):
            equals = [x for x in visitedNodes if x == currNode]
            for node in equals:
                if(node.depth < currNode.depth):
                    visit = True

        if ((currNode not in visitedNodes) or visit):
            visitedNodes.append(currNode)

            if solution(currNode):
                finalResults(currNode.state)
                return currNode.getPath()

            if currNode.depth <= limitDepth:
                newNodes = currNode.operationsMaze()
                for node in newNodes[::-1]:
                    stack.append(node)
    
    return []

# Breadth-First Search
def bfs(initialState):
    initialNode = Node(initialState)
    queue = [initialNode]
    visitedNodes = [] # Performance purposes
    
    while len(queue):
        currNode = queue.pop(0)
        visitedNodes.append(currNode)
        
        if solution(currNode):
            finalResults(currNode.state)
            return currNode.getPath()

        newNodes = currNode.operationsMaze()
        for node in newNodes:
            if node not in visitedNodes:
                queue.append(node)
    
    return []

def greedySearch(initialState, h):
    initialNode = Node(initialState)
    stack = [initialNode]
    visitedNodes = []

    while len(stack):
        currNode = stack.pop()

        if currNode not in visitedNodes:
            visitedNodes.append(currNode)

            if solution(currNode):
                finalResults(currNode.state)
                return currNode.getPath()
            
            newNodes = currNode.operationsMaze()
            for node in newNodes:
                stack.append(node)
            stack.sort(key=h)

    return []

def uniform(initialState, cost):
    initialNode = Node(initialState)
    queue = [(initialNode, 0)]  # (Node, Cost)
    visitedNodes = []

    while len(queue):
        (currNode, currCost) = queue.pop(0)

        visitedNodes.append(currNode)
        if solution(currNode):
            finalResults(currNode.state)
            return currNode.getPath()
        
        newNodes = currNode.operationsMaze()
        for node in newNodes:
            if node not in visitedNodes:
                queue.append((node, currCost + cost()))
        queue.sort(key=lambda tup: tup[1])
    
    return []

def aStar(initialState, heuristic, cost):
    initialNode = Node(initialState)
    queue = [(initialNode, 0)] # (Node, cost)
    visitedNodes = []

    while len(queue):
        (currNode, currCost) = queue.pop(0)
        visitedNodes.append(currNode)

        if solution(currNode):
            finalResults(currNode.state)
            return currNode.getPath()

        newNodes = currNode.operationsMaze()
        for node in newNodes:
            if node not in visitedNodes:
                queue.append((node, currCost + cost()))
        queue.sort(key=lambda tup: tup[1] + heuristic(tup[0]))

    return []

# Iterative deepening
def iterativeDeepening(initialState):
    path = []
    depth = 0
    while(len(path) == 0):
        path = dfs(initialState, depth)
        depth += 1
    
    print("Depth:", end=" ")
    print(depth)
    return path
    
# FIM DE ALGORITMOS #

# HEURISTIC FUNCTIONS

def heuristic1(node):
    currPos = node.state.pos
    targetPos = (0, len(node.state.board) - 1)
    return manhattanDistance(currPos, targetPos)

# Number of L's to visit
def heuristic2(node):
    return len(node.state.lVisit)

# Manhattan Distance - Number of L's already visited
def heuristic3(node):
    mH = heuristic1(node)

    visitedL = State.numberL - len(node.state.lVisit)

    return mH - visitedL

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

def cost1():
    return 1

# finalBoard
def finalBoard(state):
    if state.pos[0] == 0 and state.pos[1] == len(state.board[0]) - 1: return True
    return False

# Prints the 'board' provided
def printBoard(board):
    print('Board:')
    for row in board: 
        for piece in row:
            print(piece, end = "\t")
        print('\n\n')

def manhattanDistance(Pos1, Pos2):
    return abs(Pos1[0] - Pos2[0]) + abs(Pos1[1] - Pos2[1])

def compareAlgorithms(states):
    f = open("./algorithms.csv", 'w', newline='')
    
    writer = csv.writer(f, delimiter = ";")


    headers = ["", "Time6x6", "Time7x7", "Time8x8", "Time9x9"]
    functions = [bfs, dfs, iterativeDeepening]
    writer.writerow(headers)

    for function in functions:
        values = [function.__name__]
        for state in states:
            start = time.time()
            function(state)
            end = time.time()
            values.append(end-start)
            print(function.__name__, ": ", end - start)
        writer.writerow(values)

    values = ["uniform"]
    for state in states:
        start = time.time()
        uniform(state, cost1)
        end = time.time()
        values.append(end-start)
        print("uniform: ", end - start)
    writer.writerow(values)

    values = ["greedySearch"]
    for state in states:
        start = time.time()
        greedySearch(state, heuristic3)
        end = time.time()
        values.append(end-start)
        print("greedySearch: ", end - start)
    writer.writerow(values)

    values = ["aStar"]
    for state in states:
        start = time.time()
        aStar(state, heuristic3, cost1)
        end = time.time()
        values.append(end-start)
        print("aStar: ", end - start)
    writer.writerow(values)


def compareHeuristics(states):
    heuristics = [heuristic1, heuristic2, heuristic3]

    fGreedy = open("./greedy_search.csv", 'w', newline='')
    fAStar = open("./a_star.csv", 'w', newline='')

    writerG = csv.writer(fGreedy, delimiter = ";")
    writerA = csv.writer(fAStar, delimiter = ";")

    headers = ["", "Time6x6", "Time7x7", "Time8x8", "Time9x9"]
    writerG.writerow(headers)
    
    print("Greedy Search:")
    for heur in heuristics:
        values = [heur.__name__]

        for state in states:
            start = time.time()
            greedySearch(state, heur)
            end = time.time()
            values.append(end-start)
            print("\t" + heur.__name__ + ": ", end - start)

        writerG.writerow(values)


    writerA.writerow(headers)
    print("A* Search:")

    for heur in heuristics:
        values = [heur.__name__]

        for state in states:
            start = time.time()
            aStar(state, heur, cost1)
            end = time.time()
            values.append(end-start)
            print("\t" + heur.__name__ + ": ", end - start)

        writerA.writerow(values)

    


# FIM DAS FUNÇÕES AUXILIARES

def finalResults(state):
    print('Final position ', state.pos)
    print('L\'s to visit', state.lVisit)
    printBoard(state.board)

def initializeBoard(board):
    Pos = ()
    LVisit = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                Pos = (i, j)
            elif not (board[i][j] == 0) and not (board[i][j] in LVisit):
                LVisit.add(board[i][j])
    state = State(board, Pos, LVisit)
    State.numberL = len(LVisit)
    return state
    

if __name__ == "__main__":
    f = open('./boards.json')
    boards = json.load(f)
    f.close()

    option = 0

    searchMethods = [dfs, bfs, uniform, iterativeDeepening, greedySearch, aStar]

    heuristics = [heuristic1, heuristic2, heuristic3]

    while True:
        print('Please choose which algorithm you\'d like to use')
        print('0 - Leave apllication')
        print('1 - Depth-First Search')
        print('2 - Breadth-First Search')
        print('3 - Uniform Cost Search')
        print('4 - Iteartive Deepening')
        print('5 - Greedy Search')
        print('6 - A* Search')
        option = input('Input number: ')

        option = int(option)

        if option == 0:
            break
        else:
            func = searchMethods[option - 1]

        if option > 4:
            print('Please choose which heuristic you\'d like to use')
            print('0 - Manhattan Distance')
            print('1 - Number of Unvisited L\'s')
            print('2 - Manhattan Distance minus Visited L\'s')
            option = input('Input number: ')
            option = int(option)

            heur = heuristics[option]

        option = input('Please choose which board you\'d like to use (1-19) ')
        option = int(option)

        board = boards[option]

        if func != greedySearch and func != aStar:
            print('Path: ', func(initializeBoard(board)))
        elif func == greedySearch:
            print('Path: ', greedySearch(initializeBoard(board), heur))
        else:
            print('Path: ', aStar(initializeBoard(board), heur, cost1))

        print()


        
