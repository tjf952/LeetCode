#!/usr/bin/env python3

### Import Statements ###

import random
from test import test

### Functions ###


def guess(num: int) -> int:
    """Helper function

    Args:
        num (int): Guess

    Returns:
        int: -1 if number is lower, 1 if number is higher, otherwise 0
    """
    global random_number
    if num < random_number:
        return 1
    elif num > random_number:
        return -1
    return 0


def guessNumber(n: int) -> int:
    """L374 (Easy)
    Binary Search

    Args:
        n (int): Creates range from 1 to n for random number

    Returns:
        int: Guesses the correct number
    """
    global random_number
    random_number = random.randint(1, n)
    print(f"The secret number is {random_number}")
    l, c = 0, n
    while l <= n:
        r = guess(c)
        if r == 0:
            return c
        elif r < 0:
            n = c - 1
        else:
            l = c + 1
        c = (n + l) // 2
    return -1


if __name__ == "__main__":
    global random_number
    test(guessNumber(100), random_number)
