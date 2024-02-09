#!/usr/bin/env python3

### Import Statements ###

from collections import Counter
from test import test

### Functions ###


def mask_str(s: str) -> int:
    """Helper function

    Args:
        s (str): A string

    Returns:
        int: A mask represented in bytes
    """
    mask = 0
    for c in s:
        mask |= 1 << ord(c) - ord("a")
    return mask


def findNumOfValidWords(words: list, puzzles: list) -> list:
    """L1178 (Hard)

    Args:
        words (list): List of strings to act as solutions for each puzzle
        puzzles (list): List of strings to act as puzzles where:
            - word contains the first letter of the puzzle
            - for each letter in word, that letter is in puzzle

    Returns:
        list: Array where answer[i] is number of words that are valid to puzzle[i]
    """
    result = []
    bitmasks = Counter(mask_str(w) for w in words)
    for puzzle in puzzles:
        mask = mask_str(puzzle)
        first = 1 << ord(puzzle[0]) - ord("a")
        submask = mask
        cnt = 0
        while submask:
            if submask & first:
                cnt += bitmasks[submask]
            submask = mask & (submask - 1)
        result.append(cnt)
    return result


if __name__ == "__main__":
    words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]
    puzzles = ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]
    test(findNumOfValidWords(words, puzzles), [1, 1, 3, 2, 4, 0])
