class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        jumps = 0
        min_next_pos = 0
        max_next_pos = 0
        for i in range(n-1):
            max_next_pos = max(max_next_pos, i+nums[i])
            if i == min_next_pos:
                min_next_pos = max_next_pos
                jumps+=1
        return jumps
        