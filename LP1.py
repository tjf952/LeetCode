#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def term_count(molecule: str) -> int:
    """Helper function to count atoms in a single term
    ex: C6H12O6

    Args:
        molecule (str): A single term

    Returns:
        int: Number of atoms in molecule
    """
    stack = []
    term = ""
    alpha = False
    for i in range(len(molecule)):
        v = molecule[i]
        if v.isupper() and not alpha:
            if term:
                stack.append(int(term))
            alpha = True
            term = v
        elif v.isupper() and alpha:
            stack.append(1)
            term = v
        elif v.isnumeric() and alpha:
            alpha = False
            term = v
        elif v.isnumeric() and not alpha:
            term += v
    if term.isnumeric():
        stack.append(int(term))
    else:
        stack.append(1)
    return sum(stack)


def term_count_2(molecule: str) -> int:
    """Helper function to count atoms in a single term
    ex: C6H12O6 or H2O or CaO

    Args:
        molecule (str): A single term

    Returns:
        int: Number of atoms in molecule
    """
    if molecule[-1].isalpha():
        molecule += "1"
    total = 0
    i = 1
    while i < len(molecule):
        while molecule[i].islower():
            i += 1
        number = ""
        while i < len(molecule) and molecule[i].isnumeric():
            number += molecule[i]
            i += 1
        total += int(number) if number else 1
        i += 1
    return total


def atom_count(side: str) -> int:
    """Helper function to count atoms
    ex: C6H12O6 + 6 O2

    Args:
        side (str): One side of a chemical reaction equation

    Returns:
        int: Number of atoms in side
    """
    estack = side.replace("+", "").split()
    total = 0
    i = 0
    while i < len(estack):
        mult = 1
        if estack[i].isnumeric():
            mult = int(estack[i])
            i += 1
        atoms = term_count_2(estack[i])
        total += atoms * mult
        i += 1
    return total


def chemical_balanced(reaction: str) -> bool:
    """LP1

    Args:
        reaction (str): String representing chemical reaction

    Returns:
        bool: True if the reaction is balanced
    """
    print(f"REACTION: {reaction}")
    left, right = [side.strip() for side in reaction.split("->")]
    left_count, right_count = atom_count(left), atom_count(right)
    print(f"*** LEFT: {left_count}, RIGHT: {right_count} ***")
    return left_count == right_count


if __name__ == "__main__":
    test(chemical_balanced("2 H2 + O2 -> 2 H2O"), True)
    test(chemical_balanced("O2 -> NaCl"), True)
    test(chemical_balanced("C6H12O6 + 6 O2 -> 6 CO2 + 6 H2O"), True)
    test(chemical_balanced("10 NH3 + 10 H2O -> 10 NH4 + OH"), False)
    test(chemical_balanced("O100 -> 50 NCl"), True)
    test(chemical_balanced("Fake100 -> 25 NoCap + 25 SameStuff"), True)
