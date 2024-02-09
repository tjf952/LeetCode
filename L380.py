#!/usr/bin/env python3

### Import Statements ###

from random import choice
from test import test

### Functions ###


class RandomizedSet:
    """L380 (Medium)
    All actions have an average O(1) time complexity
    """

    def __init__(self):
        self.vals = set()

    def insert(self, val: int) -> bool:
        if val in self.vals:
            return False
        self.vals.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.vals:
            self.vals.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return choice(tuple(self.vals))


if __name__ == "__main__":
    obj = RandomizedSet()
    test(obj.insert(1), True)
    test(obj.remove(2), False)
    test(obj.insert(2), True)
    obj.getRandom()
    test(obj.remove(1), True)
    test(obj.insert(2), False)
    test(obj.getRandom(), 2)
