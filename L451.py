#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def frequencySort(s: str) -> str:
    """L451 (Medium)

    Args:
        s (str): A string

    Returns:
        (str): A string sorted in decreasing order based on frequency of characters
    """
    freq = {}
    for c in s:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    return "".join(
        c * x for c, x in sorted(freq.items(), key=lambda item: item[1], reverse=True)
    )


if __name__ == "__main__":
    test(frequencySort("treere"), "eeerrt")
