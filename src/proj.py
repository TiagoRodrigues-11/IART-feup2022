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

# Probably wrong
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
                print(currNode.state.pos)
                print(currNode.state.lVisit)
                printBoard(currNode.state.board)
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
            print(currNode.state.pos)
            print(currNode.state.lVisit)
            printBoard(currNode.state.board)
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
                print(currNode.state.pos)
                print(currNode.state.lVisit)
                printBoard(currNode.state.board)
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
            print(currNode.state.pos)
            print(currNode.state.lVisit)
            printBoard(currNode.state.board)
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
            print(currNode.state.pos)
            print(currNode.state.lVisit)
            printBoard(currNode.state.board)
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

# Manhatten Distance - Number of L's already visited
def heuristic3(node):
    mH = heuristic1(node)

    v = 0
    for l in node.state.board:
        for i in l:
            if(i > v): v = i
    
    totalL = v - 1
    visitedL = totalL - len(node.state.lVisit)

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
    for row in board: 
        for piece in row:
            print(piece, end = " ")
        print()

def manhattanDistance(Pos1, Pos2):
    return abs(Pos1[0] - Pos2[0]) + abs(Pos1[1] - Pos2[1])

def compareAlgorithms(initialState):
    #bfs
    start = time.time()
    bfs(initialState)
    end = time.time()
    print("BFS:", end=" ")
    print(end - start)

    #dfs
    start = time.time()
    dfs(initialState)
    end = time.time()
    print("DFS:", end=" ")
    print(end - start)

    #iterative deepening
    start = time.time()
    iterativeDeepening(initialState)
    end = time.time()
    print("Iterative Deepening:", end=" ")
    print(end - start)

    #uniform cost
    start = time.time()
    uniform(initialState, cost1)
    end = time.time()
    print("Uniform Cost:", end=" ")
    print(end - start)
    
    #greedy search
    start = time.time()
    greedySearch(initialState, heuristic1)
    end = time.time()
    print("Greedy Search:", end=" ")
    print(end - start)
    
    #A*
    start = time.time()
    aStar(initialState, heuristic1, cost1)
    end = time.time()
    print("A*:", end=" ")
    print(end - start)

# FIM DAS FUNÇÕES AUXILIARES

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
    return state
    

if __name__ == "__main__":
    f = open('./boards.json')
    boards = json.load(f)
    f.close()

    state = initializeBoard(boards[1])
    print("init:", end=" ")
    print(state.lVisit)
    compareAlgorithms(state)
