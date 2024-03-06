#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def count_palindromes(s: str) -> int:
    """L647 (Medium)

    Args:
        s (str): A string of letters

    Returns:
        int: Number of substring palindromes
    """
    cnt = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = s[i : j + 1]
            if substr == substr[::-1]:
                cnt += 1
    return cnt


if __name__ == "__main__":
    test(count_palindromes("abc"), 3)
    test(count_palindromes("aaa"), 6)
