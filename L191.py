#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def hamming_weight(n: int) -> int:
    """L191 (Easy)

    Args:
        n (int): An unsigned int

    Returns:
        int: Number of 1's in the string
    """
    cnt = 0
    while n > 0:
        cnt += n % 2
        n //= 2
    return cnt


if __name__ == "__main__":
    n = 11
    test(hamming_weight(n), 3)
