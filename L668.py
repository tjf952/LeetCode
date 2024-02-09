#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def upto(m: int, n: int, num: int) -> int:
    """Helper function

    Args:
        m (int): Number of rows
        n (int): Number of columns
        num (int): search value

    Returns:
        int: Index for desired number
    """
    cnt = 0
    for i in range(1, m + 1):
        j = num // i
        cnt += j if j < n else n
    return cnt


def findKthNumber(m: int, n: int, k: int) -> int:
    """L668 (Hard)

    Args:
        m (int): Number of rows
        n (int) Number of columns
        k (int): An integer

    Returns:
        int: The kth smallest element in the mxn multiplication table
    """
    lo, hi = 1, m * n
    while lo < hi:
        mid = (hi + lo) // 2
        cnt = upto(m, n, mid)
        if cnt >= k:
            hi = mid
        else:
            lo = mid + 1
    return lo


if __name__ == "__main__":
    test(findKthNumber(3, 3, 5), 3)
