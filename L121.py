#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def maxProfit(prices: list) -> int:
    """L121 (Easy)

    Args:
        prices (list): Array where prices[i] is the price of a stock on the ith day

    Returns:
        int: Maximum profit achieved by buying and selling on one day
    """
    mb, ms = prices[0], 0
    for p in prices[1:]:
        mb = min(mb, p)
        ms = max(ms, p - mb)
    return ms


if __name__ == "__main__":
    test(maxProfit([7, 1, 5, 3, 6, 4]), 5)
