#!/usr/bin/env python3


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        """Initializes iterator class

        Args:
            characters (string): list of sorted distinct lowercase letters
            combinartionLength (int): number representing length of iterator
        """
        self.chars = characters
        self.size = combinationLength
        self.curr = ""

    def next(self) -> str:
        """Returns the next combination of length in lexicographical order"""
        if self.curr == "":
            self.curr = self.chars[: self.size]
        else:
            cut = 0
            while self.chars[-cut - 1] == self.curr[-cut - 1] and cut < self.size:
                cut += 1
            letter = self.curr[-cut - 1]
            idx = self.chars.index(letter)
            first = self.curr[: -cut - 1]
            second = self.chars[idx + 1 : idx + 2 + cut]
            self.curr = first + second
        return self.curr

    def hasNext(self) -> bool:
        """Returns true if and only if there exists a next combination"""
        return self.curr != self.chars[-self.size :]
