# Intuition
By sorting the intervals by their start times, any overlapping intervals become neighbors. Once sorted, we can scan the list once—merging overlaps as soon as we see them—because any future interval will only start later.

# Approach
1. **Sort** the list of intervals in ascending order by their start value.
2. Initialize a result list `merged` with the first interval.
3. **Iterate** through each subsequent interval:
   - If the current interval’s start is **≤** the end of the last merged interval, we have an overlap. **Extend** the last merged interval’s end to the maximum of its own end and the current interval’s end.
   - Otherwise, **append** the current interval to `merged` (no overlap).
4. **Return** the `merged` list.

# Complexity
- **Time complexity:** $$O(n log(n))$$
$$O(n log(n))$$ for sorting plus $$O(n)$$ for the one-pass merge.
- **Space complexity:** $$O(n)$$
to hold the output list (ignoring in-place sort).

# Code
```python3 []
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by their start value
        intervals.sort()
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            if merged[-1][1] >= intervals[i][0]:
                # Overlap: extend the last interval
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                # No overlap: push the current interval
                merged.append(intervals[i])
        
        return merged
```
```typescript []
function merge(intervals: number[][]): number[][] {
    if (intervals.length === 0) return [];

    // Sort intervals by their start value
    intervals.sort((a, b) => a[0] - b[0]);

    const merged: number[][] = [intervals[0]];

    for (let i = 1; i < intervals.length; i++) {
        const [start, end] = intervals[i];
        const last = merged[merged.length - 1];

        if (start <= last[1]) {
            // Overlap: extend the last interval
            last[1] = Math.max(last[1], end);
        } else {
            // No overlap: push the current interval
            merged.push([start, end]);
        }
    }

    return merged;
};
```

