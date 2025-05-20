import math

class Solution(object):
    def climbStairs(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        # number of ways to arrange k two-steps and n - 2k one-steps in a sequence
        # if we take k two steps then our total steps are: 2*k + (n - 2*k) = n
        # • Number of 2-steps = k
        # •	Number of 1-steps = n - 2*k
        # •	Total moves = k + (n - 2*k) = n - k
        total = 0
        for k in range(n // 2 + 1):
            total += math.comb(n - k, k)
        return total