#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def reorder_routes(n: int, connections: list) -> int:
    """L1466 (Medium)
    This works but it's too slow to pass the test cases
    Time Complexity: O(n^2) - 43 ms for testcases

    Args:
        n (int): Number of cities
        connections (list): List of pairs representing road from x to y

    Returns:
        int: Number of changes to connections so all cities have a path to city 0
    """
    stack = [0]
    change = 0
    while stack:
        current = stack.pop()
        leftover = []
        for conn in connections:
            if current in conn:
                if current == conn[0]:
                    change += 1
                    stack.append(conn[1])
                else:
                    stack.append(conn[0])
            else:
                leftover.append(conn)
        connections = leftover
    return change


def reorder_routes_faster(n: int, connections: list) -> int:
    """L1466 (Medium)
    Two things make this faster
    (1) The searching for the next layer of the BFS algorithm by using a preconstructed graph
    (2) The use of a set to represent visited markers instead of crafting a new layer

    Args:
        n (int): Number of cities
        connections (list): List of pairs representing road from x to y

    Returns:
        int: Number of changes to connections so all cities have a path to city 0
    """
    graph = [[] for _ in range(n)]
    for conn in connections:
        graph[conn[0]].append((conn[1], 1))
        graph[conn[1]].append((conn[0], 0))
    stack = [0]
    visited = set()
    change = 0
    while stack:
        current = stack.pop()
        visited.add(current)
        for conn, point in graph[current]:
            if conn not in visited:
                change += point
                stack.append(conn)
    return change



if __name__ == "__main__":
    # 5 <- 4 -> 0 -> 1 -> 3 <- 2
    n = 6
    connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    test(reorder_routes_faster(n, connections), 3)
    # 0 <- 1 -> 2 <- 3 -> 4
    n = 5
    connections = [[1,0],[1,2],[3,2],[3,4]]
    test(reorder_routes_faster(n, connections), 2)
