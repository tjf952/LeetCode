#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def mergeAlternately(word1: str, word2: str) -> str:
    """L1768 (Easy)

    Args:
        word1 (str): A string
        word2 (str): A string

    Returns:
        str: Merged string alternating word1 and word2
    """
    merged = []
    len1, len2 = len(word1), len(word2)
    i, j = 0, 0
    while i < len1 or j < len2:
        if i < len1:
            merged.append(word1[i])
            i += 1
        if j < len2:
            merged.append(word2[j])
            j += 1
    return "".join(merged)


if __name__ == "__main__":
    test(mergeAlternately("abc", "pqr"), "apbqcr")
