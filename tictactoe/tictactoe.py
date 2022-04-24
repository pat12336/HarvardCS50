"""
Tic Tac Toe Player
"""

import math
import copy

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
    x_moves = 0
    y_moves = 0
    for row in board:
        for j in row:
            if j == X:
                x_moves += 1
            elif j == O:
                y_moves += 1
    
    return O if y_moves < x_moves else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    for row in range(0,3):
        for cell in range(0,3):
            if board[row][cell] == EMPTY:
                possible_actions.append((row, cell))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    p = player(board)
    result_board = copy.deepcopy(board)
    if result_board[action[0]][action[1]] is not EMPTY:
        raise Exception("Space is already occupied!")

    result_board[action[0]][action[1]] = p
    return result_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] is not EMPTY and (board[0][0] == board[0][1] and board[0][1] == board[0][2] or board[0][0] == board[1][0] and board[1][0] == board[2][0] or board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        return board[0][0]
    elif board[2][2] is not EMPTY and (board[2][2] == board[1][2] and board[1][2] == board[0][2] or board[2][2] == board[2][1] and board[2][1] == board[2][0]):
        return board[2][2]
    elif board[0][2] is not EMPTY and (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        return board[0][2]
    elif board[0][1] is not EMPTY and (board[0][1] == board[1][1] and board[1][1] == board[2][1]):
        return board[0][1]
    elif board[1][0] is not EMPTY and (board[1][0] == board[1][1] and board[1][1] == board[1][2]):
        return board[1][0]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board):
        return True
    else:
        for row in board:
            for cell in row:
                if cell == EMPTY:
                    return False
        
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board) == X:
        value = -math.inf
        move = (None, None)
        for action in actions(board):
            trial_value = min_value(result(board, action))
            if trial_value > value:
                move = action
                value = trial_value
        
    else:
        value = math.inf
        move = (None, None)
        for action in actions(board):
            trial_value = max_value(result(board, action))
            if trial_value < value:
                move = action
                value = trial_value
    
    return move


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
