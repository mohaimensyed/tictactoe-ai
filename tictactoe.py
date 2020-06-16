"""
Tic Tac Toe Player
"""

import math, copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board): return None

    ifX = 0
    ifO = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X: ifX+=1
            if board[i][j] == O: ifO+=1


    if ifO < ifX: return O

    else: return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board): return None

    moves = set()

    for i in range(3):
        for j in range(3):

            tup = (i, j)
            if board[i][j] == EMPTY: moves.add(tup)

    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = copy.deepcopy(board)

    if newBoard[action[0]][action[1]] != EMPTY: raise Exception('Invalid Action!')


    else: newBoard[action[0]][action[1]] = player(board)

    return newBoard



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):

        if (i == 0):
            
            if board[0][i] == X and board[1][i] == X and board[2][i] == X:
                return X

            elif board[0][i] == O and board[1][i] == O and board[2][i] == O:
                return O

            elif board[0][i] == X and board[1][i+1] == X and board[2][i+2] == X:
                return X

            elif board[0][i] == O and board[1][i+1] == O and board[2][i+2] == O:
                return O

            elif board[0][i] == X and board[0][1] == X and board[0][2] == X:
                return X

            elif board[0][i] == O and board[0][1] == O and board[0][2] == O:
                return O

        if (i == 1):

            if board[0][i] == X and board[1][i] == X and board[2][i] == X:
                return X

            elif board[0][i] == O and board[1][i] == O and board[2][i] == O:
                return O

            elif board[i][0] == X and board[i][1] == X and board[i][2] == X:
                return X

            elif board[i][0] == O and board[i][1] == O and board[i][2] == O:
                return O

        if (i == 2):

            if board[0][i] == X and board[1][i] == X and board[2][i] == X:
                return X

            elif board[0][i] == O and board[1][i] == O and board[2][i] == O:
                return O  

            elif board[0][i] == X and board[1][i-1] == X and board[2][i-2] == X:
                return X

            elif board[0][i] == O and board[1][i-1] == O and board[2][i-2] == O:
                return O 

            elif board[i][0] == X and board[i][1] == X and board[i][2] == X:
                return X

            elif board[i][0] == O and board[i][1] == O and board[i][2] == O:
                return O

    return None
                


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None: return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY: return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X: return 1
    elif winner(board) == O: return -1
    else: return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    maxplay = []
    minplay = []
    depth = 0
    isMax = True
    Min = -10000
    Max = 10000
    alpha = -10000
    beta = 10000


    if board == initial_state():

        return (1,1)



    def OptPlay(board, depth, isMax, alpha, beta):

        if terminal(board):
            return utility(board)


        if (isMax):

            optvalue = Min
            isMax = False
            depth+=1

            for action in actions(board):

                value = OptPlay(result(board, action), depth, isMax, alpha, beta)

                if(value > optvalue):
                    optvalue = value

                    if depth == 1:
                        maxplay.append(action)

                alpha = max(optvalue, alpha)

                if beta < alpha: break


            return optvalue

        else:

            optvalue = Max
            isMax = True
            depth+=1

            for action in actions(board):

                value = OptPlay(result(board, action), depth, isMax, alpha, beta)

                if(value < optvalue):
                    optvalue = value

                    if depth == 1:

                        minplay.append(action)
                
                beta = min(optvalue, beta)

                if beta < alpha: break                


            return optvalue


    
    if player(board) == X:

        OptPlay(board, depth, isMax, alpha, beta)
        return maxplay[-1]

    else:
        isMax = False
        OptPlay(board, depth, isMax, alpha, beta) 
        return minplay[-1]



