#!/usr/bin/python3
"""
0. Pascal Triangle
"""

def pascal_triangle(n):
    """This Creates a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            L = 1
            for j in range(1, i + 1):
                level.append(L)
                L = L * (i - j) // j
            res.append(level)
    return res
