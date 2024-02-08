#!/usr/bin/python3
import sys

""" The N queens puzzle is the challenge of placing N non-attacking
 queens on an N×N chessboard
"""


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at a given position (row, col)
      on the board.

    Args:
    - board (list): The chessboard represented as a 2D list.
    - row (int): The current row to check.
    - col (int): The current column to check.
    - N (int): The size of the board.

    Returns:
    - bool: True if it's safe to place a queen at the given position,
      False otherwise.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N, board, row):
    """
    Recursive function to solve the N Queens problem and print the solutions.

    Args:
    - N (int): The size of the board.
    - board (list): The chessboard represented as a 2D list.
    - row (int): The current row being considered.

    Returns:
    - None: The function prints solutions as a side effect.
    """
    if row == N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens(N, board, row + 1)
            board[row][col] = 0


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
except ValueError:
    print("N must be a number")
    sys.exit(1)

board = [[0] * N for _ in range(N)]
solve_nqueens(N, board, 0)
