#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def binary_search(nums: list, target: int) -> int:
    """L704

    Args:
        nums (list): Array of intergers sorted in ascending order
        target (int): An interger to find

    Returns:
        int: Index of target integer
    """
    b, e = 0, len(nums) - 1
    while e >= b:
        m = (b + e) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            b = m + 1
        else:
            e = m - 1
    return -1


if __name__ == "__main__":
    test(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 6), 5)
