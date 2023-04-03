#!/usr/bin/python3
"""Module for N queens puzzle"""


import sys


def exit_with_error_message(message="", code=1):
    """Prints an error message to stdout and exits
    the program with the given code.

    Args:
        message (str): The error message to print.
        code (int): The exit code to use.
    """
    print(message)
    exit(code)


def is_valid_position(board, y):
    """Checks if a queen can be placed at the current
    position on the board.

    Args:
        board (list): The chessboard.
        y (int): The height parameter.

    Returns:
        bool: True if a queen can be placed at the
        current position, False otherwise.
    """
    for i in range(y):
        if board[y][1] == board[i][1] or \
           abs(board[y][1] - board[i][1]) == y - i:
            return False
    return True


def backtrack_queen_placements(board, y):
    """Recursively finds all possible ways to place
    N queens on an NxN chessboard.

    Args:
        board (list): The chessboard.
        y (int): The height parameter.
    """
    if y == N:
        print(board)
    else:
        for x in range(N):
            board[y][1] = x
            if is_valid_position(board, y):
                backtrack_queen_placements(board, y + 1)


if len(sys.argv) != 2:
    exit_with_error_message("Usage: nqueens N")

try:
    N = int(sys.argv[1])
except ValueError:
    exit_with_error_message("N must be a number")

if N < 4:
    exit_with_error_message("N must be at least 4")

board = [[y, 0] for y in range(N)]
backtrack_queen_placements(board, 0)
