class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:        
        memo = {}

        def helper(target):
            if target in memo:
                return memo[target]
            if target < 0:
                return float('inf')
            if target == 0:
                return 0
            result = float('inf')
            for coin in coins:
                result = min(result, helper(target - coin) + 1)
            memo[target] = result
            return memo[target]

        result = helper(amount)
        return -1 if result == float('inf') else result

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], dp[a - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
    
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], dp[a - coin] + 1)

        return dp[amount] if dp[amount] <= amount else -1