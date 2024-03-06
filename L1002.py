#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def common_chars(words: list) -> list:
    """L1002 (Easy)

    Args:
        words (list): A list of words

    Returns:
        list: A list of all characters that show up in all words
    """
    result = []

    for c in set(words[0]):
        result.extend([c] * min(word.count(c) for word in words))

    return result


def counter(word: str) -> map:
    """Helper function

    Args:
        word (str): A string

    Returns:
        map: A counter dictionary item
    """
    m = {}
    for c in word:
        if c in m:
            m[c] += 1
        else:
            m[c] = 1
    return m


def common_chars_faster(words: list) -> list:
    """Improved Function"""
    result = []
    words_maps = []

    for word in words:
        words_maps.append(counter(word))

    for c in set(words[0]):
        if all([c in m for m in words_maps]):
            result.extend([c] * min(m[c] for m in words_maps))

    return result


if __name__ == "__main__":
    words = ["bella", "label", "roller"]
    output = ["e", "l", "l"]
    test(sorted(common_chars(words)), sorted(output))
