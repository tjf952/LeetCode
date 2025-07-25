#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###

def equal_team_skill(team_a: list, team_b: list) -> int:
    """LP3

    Args:
        team_a (list): Skill levevls of team A players
        team_b (list): Skill levels of team B players

    Returns:
        int: True if the reaction is balanced
    """
    sum_a = sum(team_a)
    sum_b = sum(team_b)
    count_a = team_a.count(0)
    count_b = team_b.count(0)
    print(sum_a, count_a)


if __name__ == "__main__":
    a, b = [5, 10, 0, 4], [2, 4, 0, 5, 0]
    test(equal_team_skill(a, b), 20)
    a, b = [1, 2, 3, 0], [5, 0, 0]
    test(equal_team_skill(a, b), 7)