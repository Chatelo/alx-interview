#!/usr/bin/python3
"""
This module contains a function that calculates the perimeter of an island
represented in a 2D grid.
"""


def island_perimeter(grid):
    """
    Function to calculate the perimeter of an island in a grid.

    Parameters:
    grid (list): 2D list of integers where 0 represents water and 1 represents
     land.

    Returns:
    result (int): The perimeter of the island in the grid.
    """

    # Get the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])

    # Initialize the result to 0
    result = 0

    # Iterate over each cell in the grid
    for row in range(rows):
        for col in range(cols):
            # If the cell is land (1)
            if grid[row][col] == 1:
                # Check the cell above
                if row == 0 or grid[row - 1][col] == 0:
                    result += 1
                # Check the cell to the left
                if col == 0 or grid[row][col - 1] == 0:
                    result += 1
                # Check the cell below
                if row == rows - 1 or grid[row + 1][col] == 0:
                    result += 1
                # Check the cell to the right
                if col == cols - 1 or grid[row][col + 1] == 0:
                    result += 1

    # Return the total perimeter
    return result
