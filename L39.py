#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def combinationSum(candidates: list, target: int) -> list:
    """L39 (Medium)

    Args:
        candidates (list): Array of distinct integers
        target (int): Integer where chosen numbers sum to

    Returns:
        list: List of all unique combinations that sum to target
    """

    def backtrack(arr, sum, idx, res, curr):
        """Helper function to recursively test possible combinations"""
        if sum == 0:
            res.append(list(curr))
            return
        elif sum < 0 or idx == len(arr):
            return
        else:
            curr.append(arr[idx])
            backtrack(arr, sum - arr[idx], idx, res, curr)
            curr.pop()
            backtrack(arr, sum, idx + 1, res, curr)

    res = []
    curr = []
    idx = 0
    backtrack(candidates, target, idx, res, curr)
    return res


if __name__ == "__main__":
    test(combinationSum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])
