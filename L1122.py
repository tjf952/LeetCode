#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def relativeSortArray(arr1: list, arr2: list) -> list:
    """L1122 (Easy)

    Args:
        arr1 (list): List of integers
        arr2 (list): List of distinct elements, all of which exist in arr1

    Returns:
        list: A sorted arr1 based on the relative ordering of arr2 and
            where elements not appearing in arr2 are at the end in ascending order
    """
    queue = []
    counter = {x: 0 for x in arr2}
    result = []
    for elem in arr1:
        if elem in arr2:
            counter[elem] += 1
        else:
            queue.append(elem)
    for key in counter:
        result.extend([key] * counter[key])
    return result + sorted(queue)


if __name__ == "__main__":
    test(
        relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]),
        [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19],
    )
