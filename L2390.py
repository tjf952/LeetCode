#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def removeStars(st: str) -> str:
    """L2390 (Medium)

    Args:
        st (str): A string with * symbols

    Returns:
        str: String after all stars are removed with the following:
            - remove the closest non-star character to the left
            - remove the star
    """
    s = []
    for x in st:
        if x == "*":
            s.pop()
        else:
            s.append(x)
    return "".join(s)


if __name__ == "__main__":
    test(removeStars("hello**wor*ld"), "helwold")
