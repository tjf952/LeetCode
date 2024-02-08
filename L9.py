#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def isPalindrome(x: int) -> bool:
    """L9 (Easy)

    Args:
        x (int): A positive or negative integer

    Returns:
        bool: True if x is palindrome
    """
    # return str(x) == str(x)[::-1]
    if x < 0:
        return False

    st = []

    while x > 0:
        st.append(x % 10)
        x = x // 10

    return st == st[::-1]


if __name__ == "__main__":
    pass
