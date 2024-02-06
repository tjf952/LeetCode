#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def uniquePaths(m: int, n: int) -> int:
    """L62 (Medium)

    Args:
        m (int): Rows
        n (int): Columns

    Returns:
        int: Unique number of ways to traverse an mxn grid with two directions
    """
    dp = [[1] * n for i in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]


if __name__ == "__main__":
    test(uniquePaths(3, 2), 3)
    test(uniquePaths(3, 7), 28)
