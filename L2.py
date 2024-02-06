#!/usr/bin/env python3

### Import Statements ###

from test import success, fail


### Classes ###


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


### Functions ###


def create_ll(l: list) -> ListNode:
    """Helper function to create LL"""
    if len(l) == 0:
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
        print(f"{ll.val}->", end="")
        ll = ll.next
    print("None")


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


def addTwoNumbers(l1: list, l2: list) -> list:
    """L2 (Medium)

    Args:
        l1 (list): linked list representing number in reverse order
        l2 (list): linked list representing number in reverse order

    Returns:
        (list): linked list representing sum in reverse order
    """

    l1 = create_ll(l1)
    l2 = create_ll(l2)

    ll = l1
    carry = 0

    while l1 or l2:
        first = l1.val if l1 else 0
        second = l2.val if l2 else 0
        total = first + second + carry

        l1.val = total % 10
        carry = total // 10

        if not l1.next and (carry or l2 and l2.next):
            l1.next = ListNode()

        l1 = l1.next

        if l2:
            l2 = l2.next

    return ll


if __name__ == "__main__":
    test_ll(addTwoNumbers([2, 4, 3], [5, 6, 4]), create_ll([7, 0, 8]))
    test_ll(addTwoNumbers([0], [0]), create_ll([0]))
    test_ll(
        addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]),
        create_ll([8, 9, 9, 9, 0, 0, 0, 1]),
    )
    test_ll(
        addTwoNumbers([9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9]),
        create_ll([8, 9, 9, 9, 0, 0, 0, 1]),
    )
    test_ll(addTwoNumbers([0], [7, 3]), create_ll([7, 3]))
