#!/usr/bin/env python3

### Import Statements ###

from test import test

### Classes ###


class F1:
    def __init__(self):
        pass

    def f(self, x, y):
        return x + y


class F2:
    def __init__(self):
        pass

    def f(self, x, y):
        return x * y


class F3:
    def __init__(self):
        pass

    def f(self, x, y):
        return 2 * x + y


class F4:
    def __init__(self):
        pass

    def f(self, x, y):
        return y**x + x


class F5:
    def __init__(self):
        pass

    def f(self, x, y):
        return x**x + y**y


### Functions ###


def find_solution(customfunction: "CustomFunction", z: int) -> list:
    """L1287 (Medium)

    Args:
        customfunction (class): Some class with function f

    Returns:
        list: A list of all possible solutions of function f using positive x,y
    """
    sol = []
    for x in range(1, 1001):
        for y in range(1, 1001):
            ans = customfunction.f(x, y)
            if ans == z:
                sol.append([x, y])
            if ans > z:
                break
    print(sol)
    return sol


if __name__ == "__main__":
    ci = F1()
    find_solution(ci, 5)
    ci = F2()
    find_solution(ci, 5)
    ci = F3()
    find_solution(ci, 5)
    ci = F4()
    find_solution(ci, 5)
    ci = F5()
    find_solution(ci, 5)
