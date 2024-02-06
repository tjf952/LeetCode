#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def reverse(x: int) -> int:
    """L7 (Medium)

    Args:
        x (int): A positive or negative integer

    Returns:
        int: A reversed integer with the same sign within +/- 2^31
    """
    neg = 1 if x < 0 else 0
    x = list(str(x))
    x = x[neg:][::-1]
    x = int("-" * neg + "".join(x))
    return x if x >= -(2**31) and x <= 2**31 - 1 else 0


if __name__ == "__main__":
    test(reverse(120), 21)
