#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def numTrees(n: int) -> int:
    """L96 (Medium)

    Args:
        n (int): Number of nodes on BST

    Returns:
        int: Number of structurally unique BST's with exactly n nodes
    """
    c = 1

    for i in range(1, n + 1):
        c *= 4 * i - 2
        c //= i + 1

    return c


if __name__ == "__main__":
    test(numTrees(3), 5)
