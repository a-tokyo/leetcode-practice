from itertools import accumulate

class Solution(object):
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        coverage = [0] * (n + 1)

        for l, r in queries:
            coverage[l] += 1
            coverage[r + 1] -= 1

        coverage = list(accumulate(coverage))

        for i in range(n):
            if coverage[i] < nums[i]:
                return False

        return True