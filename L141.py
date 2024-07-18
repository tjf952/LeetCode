#!/usr/bin/env python3

### Import Statements ###

from test import test

from list import *

### Functions ###


def has_cycle(head: ListNode) -> bool:
    """L141 (Easy)

    Args:
        head (ListNode): First node of linked list

    Returns:
        bool: True if there is a cycle
    """
    if not head:
        return False
    while head.next:
        if head.val == "-":
            return True
        head.val = "-"
        head = head.next
    return False


if __name__ == "__main__":
    ll = create_ll([1, 2, 3, 4, 5])
    tail = ll.next.next.next.next
    tail.next = ll  # 5 points to 1 for cycle
    test(has_cycle(ll), True)
