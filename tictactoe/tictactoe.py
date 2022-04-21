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
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
