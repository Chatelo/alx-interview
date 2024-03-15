#!/usr/bin/python3
"""
Main file for testing
"""

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(10, [5, 5, 5, 5, 5, 2, 2, 2, 2, 2])))
