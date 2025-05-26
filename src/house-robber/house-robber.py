# bottom up dynamic programming solution
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            curr = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = curr

        return prev1
    
# top down dynamic programming solution
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(i):
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(dp(i - 1), dp(i - 2) + nums[i])
            return memo[i]

        return dp(len(nums) - 1)