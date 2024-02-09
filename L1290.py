#!/usr/bin/env python3

### Import Statements ###

from test import test

from list import *

### Functions ###


def getDecimalValue(head: ListNode) -> int:
    """L1290 (Easy)

    Args:
        head (ListNode): Linked list representing a binary number where head is MSB

    Returns:
        int: Integer representation of binary number
    """
    val = ""
    while head:
        val += str(head.val)
        head = head.next
    return int(val, 2)


if __name__ == "__main__":
    head = create_ll([1, 0, 1])
    test(getDecimalValue(head), 5)
