#!/usr/bin/python3
"""This module contains a function that determines the fewest number of coins
 needed to meet a given amount total.
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
      amount total.

    Parameters:
    coins (list): A list of the values of the coins in your possession.
    total (int): The total amount to meet.

    Returns:
    coins_count (int): The fewest number of coins needed to meet total.
      If total is 0 or less, return 0. If total cannot be met by any number
        of coins you have, return -1.
    """
    if total <= 0:
        return 0
    rem = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if coin_idx >= n:
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count
