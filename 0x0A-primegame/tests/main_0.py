#!/usr/bin/python3
"""
Main file for testing
"""

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [1, 2, 3, 4, 5])))
