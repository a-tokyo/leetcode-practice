class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numset = set(nums)
        max_global = 0
        for num in numset:
            if num - 1 not in numset:
                max_curr = 1
                next_num = num + 1
                while (next_num in numset):
                    max_curr+=1
                    next_num+=1
                max_global = max(max_global, max_curr)
        return max_global