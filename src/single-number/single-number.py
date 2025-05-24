from functools import reduce
from operator import xor

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # result = 0
        # for num in nums:
        #     result ^= num
        # return result
        return reduce(xor, nums)