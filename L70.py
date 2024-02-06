#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


class Solution:
    fib = [1,2]
    
    def __init__(self):
        for i in range(2, 46):
            self.fib.append(self.fib[-1] + self.fib[-2])
        
    def climbStairs(self, n: int) -> int:
        """L70 (Easy)
        Recognized problem as fibonacci, used static memory

        Args:
            n (int): The nth step to the top

        Returns:
            The number of distinct ways to climb to the top with 1 or 2 step moves
        """
        return self.fib[n-1]


if __name__ == "__main__":
    test_case = Solution()
    test(test_case.climbStairs(3), 3)
