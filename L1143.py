#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def longestCommonSubsequence(text1: str, text2: str) -> int:
    """L1143 (Medium)

    Args:
        text1 (str): A string
        text2 (str): A string

    Returns:
        (int): The length of the longest common subsequence
    """
    row = len(text1) + 1
    col = len(text2) + 1
    prev = [0] * col
    for i in range(1, row):
        curr = [0] * col
        for j in range(1, col):
            if text1[i - 1] == text2[j - 1]:
                curr[j] = 1 + prev[j - 1]
            else:
                curr[j] = max(curr[j - 1], prev[j])
        prev = curr
    return prev[-1]


if __name__ == "__main__":
    test(longestCommonSubsequence("abcde", "ace"), 3)
