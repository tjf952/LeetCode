#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def findMedianSortedArrays(nums1: list, nums2: list) -> float:
    """L4 (Hard)

    Args:
        nums1 (list): sorted array of ints
        nums2 (list): sorted array of ints

    Returns:
        int: Median of two sorted arrays
    """
    nums = sorted(nums1 + nums2)
    size = len(nums1) + len(nums2)

    if size % 2:
        return nums[int(size / 2)]

    return (nums[int(size / 2)] + nums[int(size / 2) - 1]) / 2


if __name__ == "__main__":
    test(findMedianSortedArrays([1, 2], [3, 4]), 2.5)
