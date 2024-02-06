#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def two_sum(nums: list, target: int) -> list:
    """L1 (Easy)

    Args:
        nums (list): array of integers
        target (int): target sum

    Returns:
        list: Array of indices that add to sum
    """
    
    indexes = {}

    for i in range(len(nums)):
        indexes[nums[i]] = i

    for i in range(len(nums)):
        sub = target - nums[i]
        if sub in indexes and indexes[sub] != i:
            return [i, indexes[sub]]


if __name__ == "__main__":
    test(two_sum([2, 7, 11, 15], 9), [0, 1])
    test(two_sum([3, 2, 4], 6), [1, 2])
    test(two_sum([3, 3], 6), [0, 1])
