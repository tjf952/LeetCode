#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def balanced_str_split(s: str) -> int:
    """L1221 (Easy)

    Args:
        s (str): A string with equal 'L's and 'R's

    Returns:
        int: Maximum number of balanced substrings
    """
    cnt = 0
    balance = 0
    for c in s:
        if c == "R":
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            cnt += 1
    return cnt


if __name__ == "__main__":
    s = "RLRRLLRLRL"
    test(balanced_str_split(s), 4)
    s = "RLRRRLLRLL"
    test(balanced_str_split(s), 2)
    s = "LLLLRRRR"
    test(balanced_str_split(s), 1)
