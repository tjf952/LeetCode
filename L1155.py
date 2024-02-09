#!/usr/bin/env python3

### Import Statements ###

from itertools import permutations as perm
from test import test

### Functions ###


def numRollsToTarget(n: int, k: int, target: int) -> int:
    """L1155 (Medium)

    Args:
        n (int): Number of dice
        k (int): The number of faces on each dice numbered 1 to k
        target (int): The target sum

    Returns:
        int: Number of possible ways to roll the dice
    """
    table = [[0] * (target + 1) for i in range(n + 1)]

    for j in range(1, min(k + 1, target + 1)):
        table[1][j] = 1

    for i in range(2, n + 1):
        for j in range(1, target + 1):
            for p in range(1, min(k + 1, j)):
                table[i][j] += table[i - 1][j - p]

    return table[-1][-1] % (10**9 + 7)


if __name__ == "__main__":
    test(numRollsToTarget(1, 6, 3), 1)
    test(numRollsToTarget(2, 6, 7), 6)
    test(numRollsToTarget(30, 30, 500), 222616187)
