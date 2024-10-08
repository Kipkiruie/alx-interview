#!/usr/bin/python3
"""Change-making module.
"""


def makeChange(coins, total):
    """Finds fewest coins needed for a given total from a set of coins.
    Args:
        coins (list): List of coin values.
        total (int): The total amount to make change for.

    Returns:
        int: The fewest number of coins needed to make the change,
             or -1 if it's not possible to make the change.
    """
    if total <= 0:
        return 0  # No coins needed for zero or negative total

    sorted_coins = sorted(coins, reverse=True)
    coins_count = 0
    rem = total

    for coin in sorted_coins:
        while rem >= coin:
            rem -= coin
            coins_count += 1

    return coins_count if rem == 0 else -1
