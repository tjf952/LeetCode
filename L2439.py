#!/usr/bin/env python3

### Import Statements ###

import math
from test import test

### Functions ###


def minimizeArrayValue(nums: list) -> int:
    """L2439 (Medium)

    Args:
        nums: A list of non-negative integers

    Returns:
        int: The minimum possible value of the maximum integer of nums where:
            - any number of operations can be performed
            - one operation does nums[i]-1 and nums[i-1]+1
    """
    smol = 0
    total = 0
    for i in range(len(nums)):
        total += nums[i]
        smol = max(smol, math.ceil(total / (i + 1)))
    return smol


if __name__ == "__main__":
    test(minimizeArrayValue([3, 7, 1, 6]), 5)
