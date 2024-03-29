#!/usr/bin/env python3

### Import Statements ###

from test import fail, success

### Classes ###


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"[{self.val}]->"


### Functions ###


def create_ll(l: list) -> ListNode:
    """Helper function to create LL"""
    if not l or len(l) == 0:
        return None
    ll = ListNode(l[0])
    curr = ll

    for i in l[1:]:
        newnode = ListNode(i)
        curr.next = newnode
        curr = newnode
    return ll


def print_ll(ll: ListNode):
    """Helper function to print LL"""
    while ll:
        print(ll, end="")
        ll = ll.next
    print("None")


def reverse_ll(ll: ListNode) -> ListNode:
    """Reverses Linked List

    Args:
        ll (ListNode): Root of LL

    Returns:
        ListNode: Reversed linked list
    """
    prev_ = None
    next_ = None
    while ll:
        next_ = ll.next
        ll.next = prev_
        prev_ = ll
        ll = next_
    return prev_


def test_ll(output, expected) -> bool:
    """Simple Test Function

    Args:
        output (template): Output of given function
        expected (template): Expected answer

    Returns:
        bool: Pass or fail based on assertion
    """
    flag = True
    while output or expected:
        try:
            if output.val != expected.val:
                fail("[-] Value mismatch")
                flag = False
            output = output.next
            expected = expected.next
        except:
            fail("[-] Length mismatch")
            flag = False
            break
    if flag:
        success(f"[+] Output is correct.")
    return flag
