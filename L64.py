#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def minPathSum(grid: list) -> int:
    """L64 (Medium)

    Args:
        grid (list): mxn array

    Returns:
        int: Path from top left to bottom right that minimizes value
    """
    if not grid:
        return 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 and j > 0:
                grid[i][j] += grid[i][j - 1]
            elif j == 0 and i > 0:
                grid[i][j] += grid[i - 1][j]
            elif i > 0 and j > 0:
                grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
    return grid[-1][-1]


if __name__ == "__main__":
    test(minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]), 7)
