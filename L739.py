#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def dailyTemperatures(temps: list) -> list:
    """L739 (Medium)

    Args:
        temps: An array of daily temperatures represented as integers

    Returns:
        list: An array where ith element is number of days before a warmer temperature
    """
    result = [0] * len(temps)
    stack = []
    for idx, temp in enumerate(temps):
        while stack and temps[stack[-1]] < temp:
            curr = stack.pop()
            result[curr] = idx - curr
        stack.append(idx)
    return result


if __name__ == "__main__":
    test(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])
