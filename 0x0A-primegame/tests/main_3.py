#!/usr/bin/python3
"""
Main file for testing
"""

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(6, [1, 1, 0, 0, 1, 8])))
