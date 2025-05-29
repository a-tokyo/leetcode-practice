class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0

        for row in grid:
            left = 0
            right = n - 1
            while (left <= right):
                mid = (left + right) // 2

                if (row[mid] < 0):
                    right = mid - 1
                else:
                    left = mid + 1
            count += n - left

        return count
