class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j,k):
            if k == len(word):
                return True

            if (i>=n or i <0 or j>=m or j<0 or board[i][j] != word[k]):
                return False
            
            temp = board[i][j]
            board[i][j] = '_'
            # check all neighbors for next in ORd fashion
            found = (
                dfs(i-1, j, k+1)
                or
                dfs(i+1, j, k+1)
                or
                dfs(i, j-1, k+1)
                or
                dfs(i, j+1, k+1)
            )
            board[i][j] = temp
            return found

        m = len(board[0])
        n = len(board)
        for i in range(n):
            for j in range(m):
                if dfs(i,j,0):
                    return True
        return False