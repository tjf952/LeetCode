#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def mask_str(self, s: str) -> int:
    mask = 0
    for c in s:
        mask |= 1 << ord(c) - ord('a')
    return mask

def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
    result = []
    bitmasks = Counter(self.mask_str(w) for w in words)
    for puzzle in puzzles:
        mask = self.mask_str(puzzle)
        first = 1 << ord(puzzle[0]) - ord('a')
        submask = mask
        cnt = 0
        while submask:
            if submask & first:
                cnt += bitmasks[submask]
            submask = mask & (submask - 1)
        result.append(cnt)
    return result


if __name__ == "__main__":
    pass
