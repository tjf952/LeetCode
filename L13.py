#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def roman_to_int(s: str) -> int:
    """L13 (Easy)

    Args:
        s (str): String representing roman numeral

    Returns:
        int: Converted roman numeral
    """
    convert = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    val = 0
    idx = 0
    while idx < len(s):
        if (
            s[idx] in "IXC"
            and idx + 1 < len(s)
            and convert[s[idx + 1]] > convert[s[idx]]
        ):
            val += convert[s[idx + 1]] - convert[s[idx]]
            idx += 1
        else:
            val += convert[s[idx]]
        idx += 1
    return val


def roman_to_int(s: str) -> int:
    """L13 (Easy)

    Args:
        s (str): String representing roman numeral

    Returns:
        int: Converted roman numeral
    """
    convert = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    val = 0
    for idx in range(len(s)):
        if idx + 1 < len(s) and convert[s[idx + 1]] > convert[s[idx]]:
            val -= convert[s[idx]]
        else:
            val += convert[s[idx]]
    return val


if __name__ == "__main__":
    test(roman_to_int("III"), 3)
    test(roman_to_int("LVIII"), 58)
    test(roman_to_int("MCMXCIV"), 1994)
    test(roman_to_int("CMLII"), 952)
    test(roman_to_int("I"), 1)
    test(roman_to_int("DCXXI"), 621)
