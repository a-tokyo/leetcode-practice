import math

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            row = []
            for k in range(i + 1):
                row.append(math.comb(i, k))
            res.append(row)
        return res