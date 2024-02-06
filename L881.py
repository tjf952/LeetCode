#!/usr/bin/env python3

### Import Statements ###

from collections import deque

from test import test

### Functions ###


def num_rescue_boats(people: list, limit: int) -> int:
    """L881

    Args:
        people (list): An array of people where people[i] is the weight of ith person
        limit (int): The maxmimum weight a boat can carry

    Returns:
        Minimum number of boats to carry every given person
    """
    boats = 0
    people = deque(sorted(people))
    while people:
        if people[-1] + people[0] <= limit:
            people.popleft()
        people.pop()
        boats += 1
    return boats


if __name__ == "__main__":
    test(num_rescue_boats([5, 8, 3, 6], 11), 2)
