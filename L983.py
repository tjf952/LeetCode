#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def min_cost_tickets(days: list, costs: list) -> int:
    """L983

    Args:
        days (list): A list of integers representing days of a year
        costs (list): 3 different types off tickets for 1, 7, and 30 day passes

    Returns:
        int: Minimum cost you need to travel every day in given list of days
    """
    last = days[-1]
    cal = [0] * (last + 1)
    days = set(days)
    for i in range(1, len(cal)):
        if i in days:
            cal[i] = cal[i - 1] + costs[0]
            cal[i] = min(cal[max(0, i - 7)] + costs[1], cal[i])
            cal[i] = min(cal[max(0, i - 30)] + costs[2], cal[i])
        else:
            cal[i] = cal[i - 1]
    return cal[last]


if __name__ == "__main__":
    test(min_cost_tickets([0, 4, 5, 11, 13, 15, 19, 20, 21], [5, 20, 60]), 40)
