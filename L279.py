#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def numSquares(n: int) -> int:
    """L279 (Medium)

    Args:
        n (int): An integer

    Returns:
        The least number of perfect square numbers that sum to n
    """
    dp = [0]

    def update(n: int) -> None:
        """Recursive function to update dynamic programming table"""
        idx = len(dp)
        while idx <= n:
            min_sum = float("inf")
            for s in range(1, idx + 1):
                if s**2 > idx:
                    break
                min_sum = min(1 + dp[idx - s**2], min_sum)
            dp.append(min_sum)
            idx += 1

    update(n)
    return dp[n]


if __name__ == "__main__":
    test(numSquares(12), 3)
    test(numSquares(13), 2)
