#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def findDisappearedNumbers(nums: list) -> list:
    """L448 (Easy)

    Args:
        nums (list): Array of n integers where nums[i] is in range [1, n]

    Returns:
        list: Array of integers in range [1, n] that don't appear in nums

    This solution take O(n) time complexity and space complexity

    ran = set(range(1, len(nums)+1)) # n space, n time
    nums = set(nums) # n time
    return list(ran-nums) # 1 time since return is ignored

    Below solution takes 2n > O(n) time complexity and O(1) space complexity
    """
    ans = []
    for val in nums:
        nums[abs(val) - 1] = -abs(nums[abs(val) - 1])
    for i in range(len(nums)):
        if nums[i] > 0:
            ans.append(i + 1)
    return ans


if __name__ == "__main__":
    test(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]), [5, 6])
