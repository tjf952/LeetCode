#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def nextGreaterElement(nums1: list, nums2: list) -> list:
    """L496 (Easy)

    Args:
        nums1 (list): List of unique integers >= to 0
        nums2 (list): List that at least contains all values of nums1

    Returns:
        list: A list such that the ith element is the next greater element of nums2[j]
    """
    result = []
    for i in nums1:
        next_greater = -1
        for j in nums2[nums2.index(i) + 1 :]:
            if j > i:
                next_greater = j
                break
        result.append(next_greater)
    return result


if __name__ == "__main__":
    test(nextGreaterElement2([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1])
