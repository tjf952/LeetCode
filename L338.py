#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def countBits(n: int) -> list:
    """L338 (Easy)

    Args:
        n: An integer

    Returns:
        list: The number of 1's in the binary representation of 0 to n
    """
    sol = [0]
    for x in range(1, n + 1):
        sol.append(sol[x // 2] + x % 2)
    return sol


if __name__ == "__main__":
    test(countBits(5), [0, 1, 1, 2, 1, 2])
