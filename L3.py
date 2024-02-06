#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def length_longest_substring(s: str) -> int:
    """L3 (Medium)

    Args:
        s: string of characters

    Returns:
        Longest substring length
    """
    substr = {}
    max_len = 0
    start = 0
    for i in range(0, len(s)):
        if s[i] in substr:
            start = max(start, substr[s[i]] + 1)
        max_len = max(max_len, i - start + 1)
        substr[s[i]] = i
    return max_len


if __name__ == "__main__":
    test(length_longest_substring("abcabcbb"), 3)
    test(length_longest_substring("bbbbb"), 1)
    test(length_longest_substring("pwwkew"), 3)
