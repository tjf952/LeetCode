#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def numIslands(grid: list) -> int:
    """L200 (Medium)

    Args:
        grid: An mxn binary grid with 1's (land) and 0's (water)

    Returns:
        int: The number of islands within the grid
    """

    def remove_island(r, c) -> None:
        """Recursive algorithm to remove islands by changing to 0's

        Args:
            r (int): Current row index
            c (int): Current column index
        """
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0":
            return
        grid[r][c] = "0"
        remove_island(r, c - 1)
        remove_island(r - 1, c)
        remove_island(r, c + 1)
        remove_island(r + 1, c)
        return

    total = 0
    for m in range(len(grid)):
        for n in range(len(grid[0])):
            if grid[m][n] == "1":
                total += 1
                remove_island(m, n)
    return total


if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    test(numIslands(grid), 3)
