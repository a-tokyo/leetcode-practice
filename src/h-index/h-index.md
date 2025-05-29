# Intuition
The H-Index is defined as the maximum value h such that the researcher has published h papers that have each been cited at least h times.
To determine this, we need a way to compare citation counts against paper ranks (number of papers with at least that many citations).

# Approach
1.	Sort citations in descending order so that the most cited papers come first.
2.	Iterate through the sorted list. For each paper at index i, check:
	•	If citations[i] <= i, it means there are i papers with at least i citations.
	•	Return i as the H-Index.
3.	If we never return inside the loop, then all papers have more citations than their rank.
	•	So the H-Index is len(citations).

This method leverages the sorted order to directly compare citation counts against ranks, which is exactly what the H-index definition requires.

# Complexity
- Time complexity:
$$O(nlog(n))$$ 

- Space complexity:
$$O(1)$$

# Code
```python []
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i] <= i:
                return i
        return len(citations)
```
```typescript []
function hIndex(citations: number[]): number {
    citations.sort((a,b) => b-a); // note that the default sort and reverse in JS wont work as it does in py.
    for (let i = 0; i < citations.length; i++) {
        if (citations[i] <= i) return i
    }
    return citations.length
};
```