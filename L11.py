#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def max_area(height: list) -> int:
    """L11 (Medium)

    Args:
        height (list): Integer array of heights positioned at i on an x-axis

    Returns:
        int: The maximum area that a rectangular box can have using such heights
    """
    left = 0
    right = len(height) - 1
    maxarea = 0
    while left < right:
        minheight = min(height[left], height[right])
        maxarea = max(maxarea, minheight * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return maxarea


def max_area_brute(height: list) -> int:
    """Solution in O(n^2)"""
    result = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            current_area = min(height[i], height[j]) * (j - i)
            result = max(result, current_area)
    return result


if __name__ == "__main__":
    test(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
    test(max_area([1, 71, 70, 8, 6, 2, 5, 4, 8, 3, 7]), 70)
    test(max_area([1, 1]), 1)
