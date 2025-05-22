class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left<=right:
            mid = (left + right) // 2

            # imagine we had an array and we split each n items into a new row
            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                left = mid + 1
            if matrix[row][col] > target:
                right = mid -1

        return False