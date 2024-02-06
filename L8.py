#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def myAtoi(s: str) -> int:
    """L8 (Medium)

    Args:
        s (str): string of alphanumeric chars

    Returns:
        Performs myAtoi function which converts str to int
    """
    result = ""
    while s and s[0] == " ":
        s = s[1:]
    if s and s[0] in "+-":
        result += s[0]
        s = s[1:]
    while s and s[0] in "0123456789":
        result += s[0]
        s = s[1:]
    try:
        s = int(result)
        if s < 0:
            return s if s > -(2**31) else -(2**31)
        return s if s < 2**31 - 1 else 2**31 - 1
    except:
        return 0


if __name__ == "__main__":
    test(myAtoi("  41932 with words"), 41932)
