class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        final_pos =  -1
        for i in range(n-1, -1, -1):
            if (i + nums[i] >= final_pos):
                final_pos = i
        return True if final_pos == 0 else False
        