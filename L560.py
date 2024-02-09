#!/usr/bin/env python3

### Import Statements ###

from collections import Counter
from test import test

### Functions ###


def subarraySum(nums: list, k: int) -> int:
    """L560 (Medium)

    Args:
        nums (list): Array of integers
        k (int): Target sum of subarrays

    Returns:
        int: Number of subarrays whose sum is k
    """
    ps, a = 0, 0
    c = Counter([0])
    for e in nums:
        ps += e
        if ps - k in c:
            a += c[ps - k]
        c[ps] += 1
    return a


if __name__ == "__main__":
    test(subarraySum([1, 2, 3], 3), 2)
