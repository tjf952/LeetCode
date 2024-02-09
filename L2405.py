#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def partitionString(s: str) -> int:
    """L2405 (Medium)

    Args:
        s (str): A string

    Returns:
        int: The minimum number of substring in such a partition where:
            - there are one or more substrings
            - the characters in each substring are unique
    """
    cnt = 1
    d = set()
    for c in s:
        if c in d:
            cnt += 1
            d = set()
        d.add(c)
    return cnt


if __name__ == "__main__":
    test(partitionString("abacaba"), 4)
