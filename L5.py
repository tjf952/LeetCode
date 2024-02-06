#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def longestPalindrome(s: str) -> str:
    """L5 (Hard)

    Args:
        s (string): string of characters

    Returns:
        string: Longest palindromic substring
    """
    m = s[0]
    for i, c in enumerate(s[:-1]):
        c_odd = s[i]
        l, h = i, i
        while l >= 0 and h < len(s) and s[l] == s[h]:
            c_odd = s[l : h + 1]
            l, h = l - 1, h + 1
        c_even = ""
        l, h = i, i + 1
        while l >= 0 and h < len(s) and s[l] == s[h]:
            c_even = s[l : h + 1]
            l, h = l - 1, h + 1
        c_odd = c_odd if len(c_odd) > len(c_even) else c_even
        if len(c_odd) > len(m):
            m = c_odd
    return m


if __name__ == "__main__":
    test(longestPalindrome("fdskjnfdskjasdfghgfdsaefnif"), "asdfghgfdsa")
