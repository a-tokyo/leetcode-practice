class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = sorted([int(x) for x in str(n)], reverse=True)
        return nums[0] * nums[1]