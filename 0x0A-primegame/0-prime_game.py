#!/usr/bin/python3
"""
This is a Python script that determines the winner of a game based
 on prime numbers.
"""


def isWinner(x, nums):
    """
    This function determines the winner of the game.

    Parameters:
    x (int): The number of rounds in the game.
    nums (list): A list of integers representing the maximum number
      for each round.

    Returns:
    str: The name of the winner ('Maria' or 'Ben') or None if it's a draw.
    """
    # Return None if there are no rounds or no maximum numbers
    if x < 1 or not nums:
        return None

    marias_wins, bens_wins = 0, 0
    n = max(nums)

    # Initialize a list of booleans representing prime numbers
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False

    # Use the Sieve of Eratosthenes to identify prime numbers
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False

    # Determine the winner of each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0:n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    # Determine the overall winner
    if marias_wins == bens_wins:
        return None
    return "Maria" if marias_wins > bens_wins else "Ben"
