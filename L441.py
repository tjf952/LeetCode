#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def arrangeCoins(n: int) -> int:
    """L441 (Easy)

    Args:
        n (int): The number of coins

    Returns:
        int: The number of complete rows in a staircase built with n coins
    """
    return int(-3 / 2 + ((5 / 4) + 2 * n) ** (1 / 2)) + 1


if __name__ == "__main__":
    test(arrangeCoins(8), 3)
