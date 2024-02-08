#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def maxProfit(prices: list) -> int:
    """L309 (Medium)

    Args:
        prices (list): Array where prices[i] is the price of a given stock on ith day

    Returns:
        Maximum profit you can achieve with buy, sell, wait actions
        Restrictions are you must wait after a sell day
    """
    dp = [[0 for _ in range(3)] for _ in range(len(prices))]
    dp[0][1] -= prices[0]
    for i in range(1, len(prices)):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])  # Wait
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])  # Buy
        dp[i][2] = dp[i - 1][1] + prices[i]  # Sell
    return max(dp[-1])


if __name__ == "__main__":
    test(maxProfit([1, 2, 3, 0, 2]), 3)
