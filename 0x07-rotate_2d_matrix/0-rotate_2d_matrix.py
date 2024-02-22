#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise
    """
    n = len(matrix[0])
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            tmp = matrix[i][j]
            # Move values from left to top
            matrix[i][j] = matrix[n - 1 - j][i]
            # Move values from bottom to left
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            # Move values from right to bottom
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            # Assign temp to right
            matrix[j][n - 1 - i] = tmp
