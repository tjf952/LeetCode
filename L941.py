#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def validMountainArray(arr: list) -> bool:
    """L941 (Easy)

    Args:
        arr (list): Array of integers

    Returns:
        True if valid mountain array
        - arr length >= 3
        - exists some i such that arr[0] < ... < arr[i]
        - exists some i such that arr[i] > ... > arr[arr.length - 1]
    """
    if len(arr) < 3:
        return False
    c = False
    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            c = True
        if c and arr[i] >= arr[i - 1]:
            return False
    return c and arr[1] > arr[0]


if __name__ == "__main__":
    test(validMountainArray([2, 1]), False)
    test(validMountainArray([3, 5, 5]), False)
    test(validMountainArray([0, 3, 2, 1]), True)
