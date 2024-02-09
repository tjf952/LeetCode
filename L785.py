#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def isBipartite(graph: list) -> bool:
    """L785 (Medium)

    Args:
        graph (list): 2-d array undirected graph where each node is between 0 and n-1
            graph[u] is an array of nodes that node u is adjacent to

    Returns:
        bool: True if the graph is bipartite i.e.
            nodes can be partitioned into two independent sets A and B
            such that every edge connects a node in set A and a node in set B
    """
    b = {}
    for i in range(len(graph)):
        if i not in b and graph[i]:
            b[i] = 1
            q = [i]
            while q:
                curr = q.pop()
                for n in graph[curr]:
                    if n not in b:
                        b[n] = -b[curr]
                        q.append(n)
                    elif b[n] == b[curr]:
                        return False
    return True


if __name__ == "__main__":
    graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    test(isBipartite(graph), False)
    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    test(isBipartite(graph), True)
