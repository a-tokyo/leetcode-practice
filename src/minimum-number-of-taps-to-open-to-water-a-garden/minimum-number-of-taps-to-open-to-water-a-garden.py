# similar to jump game II
class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        max_ranges = [0] * (n+1)
        for i in range(n+1):
            left = max(0, i - ranges[i])
            right = min(n, i + ranges[i])
            max_ranges[left] = max(max_ranges[left], right)

        # now window ranges greedy algorithm

        taps=0
        curr_max=0
        max_max=0
        for i in range(n):
            max_max = max(max_max, max_ranges[i])
            if i == curr_max:
                curr_max = max_max
                taps+=1
            if i == max_max and i != n:
                return -1

        return taps