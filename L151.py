#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def reverseWords(s: str) -> str:
    """L151 (Medium)

    Args:
        s (str): Sequence of words

    Returns:
        str: Sequence of words in reverse order
    """
    # return " ".join(s.split()[::-1])
    st = []

    for word in s.split():
        st.append(word)

    seq = st.pop(-1)

    while st:
        seq += " " + st.pop(-1)

    return seq


if __name__ == "__main__":
    test(reverseWords("the sky is blue"), "blue is sky the")
