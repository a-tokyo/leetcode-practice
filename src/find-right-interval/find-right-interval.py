class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        sorted_intervals = sorted((start, i) for i, (start, _) in enumerate(intervals))
        result = []

        for interval in intervals:
            left = 0
            right = len(intervals) - 1
            val = -1
            
            while (left <= right):
                mid = (left + right) // 2
                if sorted_intervals[mid][0] >= interval[1]:
                    val = sorted_intervals[mid][1]
                    right = mid - 1
                else:
                    left = mid + 1
            result.append(val)
        return result