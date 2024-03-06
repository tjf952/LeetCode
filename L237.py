#!/usr/bin/env python3

### Import Statements ###

from test import test

from list import *

### Functions ###


def delete_node(node: ListNode) -> None:
    """L237 (Medium)

    Args:
        node (ListNode): An exisitng node in a list

    Returns:
        None, but the list is modified to delete the passed node
    """
    prev = None
    while node.next != None:
        node.val = node.next.val
        prev = node
        node = node.next
    prev.next = None


def delete_node_fast(node: ListNode) -> None:
    """Improved function"""
    node.val = node.next.val
    node.next = node.next.next


if __name__ == "__main__":
    # Constraint: node != tail and len(list) > 1

    ll = create_ll([4, 5, 1, 9])
    expected = create_ll([4, 9])

    node_5 = ll.next
    delete_node(node_5)
    node_1 = ll.next
    delete_node(node_1)

    print_ll(ll)
    print_ll(expected)
    test_ll(ll, expected)
