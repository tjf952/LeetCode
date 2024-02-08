#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###

threes = [3**x for x in range(15)]


def isPowerOfThree(n: int) -> bool:
    """L326 (Easy)

    Args:
        n (int): An integer

    Returns:
        True if power of 3
        Use static memory to speed up successive calls
    """
    if n > threes[-1]:
        while 1:
            nextval = 3 ** len(threes)
            threes.append(nextval)
            if nextval >= n:
                break
    return n in threes


if __name__ == "__main__":
    test(isPowerOfThree(3**7), True)
