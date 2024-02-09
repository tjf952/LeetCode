#!/usr/bin/env python3

### Import Statements ###

from collections import Counter
from test import test

### Functions ###


def findPairs(nums: list, k: int) -> int:
    """L532 (Medium)

    Args:
        nums (list): An array of integers
        k (int): Integer that is the difference between a pair of values in nums

    Returns:
        int: The number of unique k-diff pairs in the array
    """
    c = Counter(nums)
    a = 0
    if k == 0:
        for key in c:
            a += c[key] > 1
    else:
        for key in c:
            a += c[key - k] > 0
    return a


if __name__ == "__main__":
    test(findPairs([3, 1, 4, 1, 5], 2), 2)
