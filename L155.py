#!/usr/bin/env python3

### Import Statements ###

from test import test

### Classes ###


class MinStack:
    """L155 (Medium)

    MinStack implemented with O(1) time complexity for each function
    """

    def __init__(self):
        """Initializes the stack object"""
        self.stack = [(0, float("inf"))]

    def push(self, val: int) -> None:
        """Pushes the element val onto the stack"""
        self.stack.append((val, min(val, self.stack[-1][1])))

    def pop(self) -> None:
        """Removes the top element on the top of the stack"""
        self.stack.pop()

    def top(self) -> int:
        """Gets the top element of the stack"""
        return self.stack[-1][0]

    def getMin(self) -> int:
        """Retrieves the minimum element in the stack"""
        return self.stack[-1][1]


if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    test(obj.getMin(), -3)
    obj.pop()
    test(obj.top(), 0)
    test(obj.getMin(), -2)
