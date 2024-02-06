#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def removeElement(nums: list, val: int) -> int:
    """L27 (Easy)

    Args:
        nums (list): Integer array
        val (int): Value to be removed

    Returns:
        int: Returns number of elements not equal to val
             Also modifies array in place
    """
    idx = 0
    for i in range(len(nums)):
        nums[idx] = nums[i]
        if nums[i] != val:
            idx += 1
    return idx


if __name__ == "__main__":
    pass
