class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        col = set()
        diagPos = set()
        diagNeg = set()

        matrix = [['.'] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                result.append([''.join(row) for row in matrix])
                return
            for j in range(n):
                if j in col or r + j in diagPos or r - j in diagNeg:
                    continue
                matrix[r][j] = 'Q'
                col.add(j)
                diagPos.add(r + j)
                diagNeg.add(r - j)

                backtrack(r+1)

                matrix[r][j] = '.'
                col.remove(j)
                diagPos.remove(r + j)
                diagNeg.remove(r - j)

        backtrack(0)
        return result