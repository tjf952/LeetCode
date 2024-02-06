#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def convert(s: str, num_rows: int) -> str:
    """L6 (Medium)

    Args:
        s (str): A string
        num_rows (int): Number of rows for zigzag conversion

    Returns:
        str: An encoded string

        Ex: Given s = PAYPALISHIRING, num_rows = 3
            P   A   H   N
            A P L S I I G
            Y   I   R
            This becomes > PAHNAPLSIIGYIR
    """
    if num_rows < 2 or len(s) <= num_rows:
        return s

    result = ["" for _ in range(num_rows)]
    idx = 0
    sign = 1

    for c in s:
        result[idx] += c
        idx += sign
        if idx == num_rows - 1 or idx == 0:
            sign = -sign

    return "".join(result)


if __name__ == "__main__":
    test(convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
