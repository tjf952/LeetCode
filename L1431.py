#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def kidsWithCandies(candies: list, extraCandies: int) -> list:
    """L1431 (Easy)

    Args:
        candies (list): Candy amounts for each kid
        extraCandies (int): Candies to give

    Returns:
        list: Array where result[i] is true if kid i has most candies with extraCandies
    """
    bar = max(candies) - extraCandies
    return [x >= bar for x in candies]


if __name__ == "__main__":
    test(kidsWithCandies([2, 3, 5, 1, 3], 3), [True, True, True, False, True])
