MOD = 10**9 + 7

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        f = [1] * 26
        for _ in range(t):
            f_next = f[:]
            f_next[25] = (f[0] + f[1]) % MOD
            for i in range(25):
                f_next[i] = f[i+1]
            f = f_next
        return sum(f_next[ord(ch) - ord('a')] for ch in s) % MOD