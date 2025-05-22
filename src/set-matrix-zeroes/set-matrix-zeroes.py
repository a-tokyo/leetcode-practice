class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        row_zero = any(matrix[0][j] == 0 for j in range(m))
        col_zero = any(matrix[i][0] == 0 for i in range(n))

        for i in range(1, n):
            for j in range(1, m):
                element = matrix[i][j]
                if element == 0:
                    if i == 0:
                        temp = True
                    else:
                        matrix[0][j] = 0
                        matrix[i][0] = 0

        for i in range(1, n):
            for j in range(1, m):
                if (matrix[0][j] == 0 or matrix[i][0] == 0):
                    matrix[i][j] = 0
        
        if row_zero:
            for j in range(m):
                matrix[0][j] = 0

        if col_zero:
            for i in range(n):
                matrix[i][0] = 0