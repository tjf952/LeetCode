#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def largestDivisibleSubset(nums: list) -> list:
    """L368 (Medium)

    Args:
        nums (list): Set of distinct positive integers

    Returns:
        (list) Largest subset such that every pair of elements can be divisible
    """
    size, top = len(nums), 0
    dp, pred, ans = [1] * size, [-1] * size, []
    nums.sort()
    for i in range(1, size):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                pred[i] = j
        if dp[i] > dp[top]:
            top = i
    while top >= 0:
        ans.append(nums[top])
        top = pred[top]
    ans.sort()
    return ans


if __name__ == "__main__":
    test(largestDivisibleSubset([1, 2, 4, 8, 9]), [1, 2, 4, 8])
