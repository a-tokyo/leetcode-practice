MOD = 10**9 + 7

class Solution(object):
    def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :rtype: int
        """
        dp = [[0] * (t + 1) for _ in range(26)]

        for c in range(26):
            dp[c][0] = 1

        for j in range(1, t + 1):
            for c in range(25, -1, -1):
                if c == 25:  # z
                    dp[c][j] = (dp[0][j-1] + dp[1][j-1]) % MOD
                else:
                    dp[c][j] = dp[c+1][j-1]
        result = 0
        for c in s:
            result = (result + dp[ord(c) - ord('a')][t]) % MOD

        return result