#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def dutch_sort(nums: list) -> list:
    """L75 (Medium)

    Args:
        nums (list): Array of integers with values 0, 1, and 2

    Returns:
        list: Sorted array
    """
    zero = 0
    one = 0
    two = len(nums) - 1
    while one <= two:
        if nums[two] == 2:
            two -= 1
        elif nums[two] == 1:
            nums[two] = nums[one]
            nums[one] = 1
            one += 1
        else:
            nums[two] = nums[zero]
            nums[zero] = 0
            if zero == one:
                one += 1
            zero += 1
    return nums


if __name__ == "__main__":
    test(dutch_sort([1]), [1])
    test(dutch_sort([]), [])
    test(dutch_sort([2, 1, 0, 1, 2, 0, 1, 0, 2]), [0, 0, 0, 1, 1, 1, 2, 2, 2])
