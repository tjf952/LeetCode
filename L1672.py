#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def maximumWealth(accounts: list) -> int:
    """L1673 (Easy)

    Args:
        accounts (list): An mxn integer grid representing j accounts of each customer

    Returns:
        int: The maxium wealth of the richest customer
    """
    return max([sum(x) for x in accounts])


if __name__ == "__main__":
    test(maximumWealth([[1, 2, 3], [3, 2, 1]]), 6)
