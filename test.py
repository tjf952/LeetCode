#!/usr/bin/env python3

"""Testing Functionality

Holds any classes or functions for testing leet problems

Usage: *FOR IMPORT IN PROBLEMS*
"""

### Import Statements ###

from termcolor import colored, cprint

### Functions ###


def success(s):
    cprint(s, "green", attrs=["bold"])


def fail(s):
    cprint(s, "red", attrs=["bold", "reverse", "blink"])


def test(output, expected) -> bool:
    """Simple Test Function

    Args:
        output (template): Output of given function
        expected (template): Expected answer

    Returns:
        bool: Pass or fail based on assertion
    """
    if output == expected:
        success(f"[+] Output {output} is correct.")
        return True
    fail(f"[!] Incorrect!\n    Output: {output}\n  Expected: {expected}")
    return False
