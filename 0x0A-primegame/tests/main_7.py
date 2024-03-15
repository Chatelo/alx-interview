#!/usr/bin/python3
"""
Main file for testing
"""

isWinner = __import__('0-prime_game').isWinner

nums = [0] * 100
for i in range(100):
    nums[i] = i * i

print("Winner: {}".format(isWinner(100, nums)))
