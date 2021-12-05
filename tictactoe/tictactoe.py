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
    Xs = 0
    Os = 0
    # simply iterate over the given board and calculate how many Xs and Os are there
    for y_axis in board:
        for x_axis in y_axis:
            if x_axis == X:
                Xs += 1
            elif x_axis == O:
                Os += 1
    if Xs <= Os:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()

    for y, y_axis in enumerate(board):
        for x, x_axis in enumerate(y_axis):
            if x_axis == EMPTY:
                possible_actions.add((y, x))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if len(action) != 2:
        raise Exception("result function: incorrect action")

    if action[0] < 0 or action[0] > 2 or action[1] < 0 or action[1] > 2:
        raise Exception("result function: incorrect action value")

    y, x = action[0], action[1]

    board_copy = copy.deepcopy(board)

    if board_copy[y][x] != EMPTY:
        raise Exception("suggested action has already been taken")
    else:
        board_copy[y][x] = player(board)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Iterate over the entire board
    for x in range(3):
        # Check horizontal lines like (x,0) (x,1) and (x,2)
        if (board[x][0] == board[x][1] == board[x][2]) and (board[x][0] != EMPTY):
            return board[x][0]
        # check vertical lines (0,x) (1,x) (2,x)
        if (board[0][x] == board[1][x] == board[2][x]) and (board[0][x] != EMPTY):
            return board[0][x]

    # Check diagonals
    if (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]) \
            and board[1][1] != EMPTY:
        return board[1][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # check for a winner
    if winner(board) == X or winner(board) == O:  
        return True
    # check for no empty cells are left
    elif EMPTY not in board[0] and EMPTY not in board[1] and EMPTY not in board[2]: 
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        score = -math.inf
        action_taken = None

        for action in actions(board):
            min_value = minvalue(result(board, action))

            if min_value > score:
                score = min_value
                action_taken = action

        return action_taken

    elif player(board) == O:
        score = math.inf
        action_taken = None
        
        for action in actions(board):
            max_value = maxvalue(result(board, action))
            
            if max_value < score:
                score = max_value
                action_taken = action
                
        return action_taken


def minvalue(board):
    """
    Returns the minimum value out of all maximum values
    """

    if terminal(board):  # if game over, just return the utility of state
        return utility(board)

    max_value = math.inf  # iterate over the available actions and return the minimum out of all maximums
    for action in actions(board):
        max_value = min(max_value, maxvalue(result(board, action)))

    return max_value

def maxvalue(board):
    """
    Returns the maximum value out of all minimum values
    """

    if terminal(board):
        return utility(board)

    min_value = -math.inf
    for action in actions(board):
        min_value = max(min_value, minvalue(result(board, action)))

    return min_value