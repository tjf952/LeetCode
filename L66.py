#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def plusOne(arg: list) -> list:
    """L66 (Easy)

    Args:
        arg (list): An array of integers representing one large integer

    Returns:
        list: The large integer incremented by one
    """
    # return list(map(int, str(int("".join(str(i) for i in digits)) + 1)))
    idx = -1
    arg[idx] += 1
    while arg[idx] == 10:
        arg[idx] = 0
        if len(arg) + idx:
            idx -= 1
            arg[idx] += 1
        else:
            arg = [1] + arg
    return arg


if __name__ == "__main__":
    test(plusOne([1, 2, 3]), [1, 2, 4])
