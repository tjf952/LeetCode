#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def maxProfit(prices: list) -> int:
    """L122 (Medium)

    Args:
        prices (list): List of stock prices

    Returns:
        int: Maximum profit that can be achieved by buying or selling on each day
    """
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit


if __name__ == "__main__":
    test(maxProfit([7, 1, 5, 3, 6, 4]), 7)
