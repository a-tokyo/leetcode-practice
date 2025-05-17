class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = {}

        def search(m, n):
            if m == 0 or n == 0: return 0
            if m == 1 and n == 1: return 1
            # key = tuple(sorted((m, n))) # not needed but speeds up since transpose is same
            key = (m, n)
            if key in memo: return memo[key]
            memo[key] = search(m - 1, n) + search(m, n - 1)
            return memo[key]

        return search(m, n)