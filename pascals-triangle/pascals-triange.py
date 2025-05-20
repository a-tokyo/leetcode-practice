class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for i in range(1, numRows):
            prev = res[-1]
            curr = [1]
            for j in range(1, i): curr.append(prev[j-1] + prev[j])
            curr.append(1)
            res.append(curr)
        return res