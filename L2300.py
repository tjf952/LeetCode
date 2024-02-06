#!/usr/bin/env python3

### Import Statements ###

import math
from test import test

### Functions ###


def successful_pairs(spells: list, potions: list, success: int) -> list:
    """L2300
    Uses binary search (binsearch) to do a logn search on potions

    Args:
        spells (list): List of integers representing strength of ith spell
        potions (list): List of integers representing strength of jth potion

    Returns:
        int: Minimum cost you need to travel every day in given list of days
    """

    def binsearchmax(nums, target):
        b, e = 0, len(nums) - 1
        while b <= e:
            m = b + (e - b) // 2
            if nums[m] >= target:
                e = m - 1
            else:
                b = m + 1
        return b

    potions.sort()
    for i in range(len(spells)):
        """
        spell[i] * potion[j] >= success
        potion[j] >= success/spell[i]
        find ceil(success/spell[i]) = idx --> len(potions[idx:]) = answer
        """
        idx = math.ceil(success / spells[i])
        idx = binsearchmax(potions, idx)
        spells[i] = len(potions) - idx
    return spells


if __name__ == "__main__":
    test(successful_pairs([5, 1, 3], [1, 2, 3, 4, 5], 7), [4, 0, 3])
