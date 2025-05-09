function searchRange(nums: number[], target: number): number[] {
    const n = nums.length;

    function getTargetIndex(left) {
        let low = 0, high = n;
        while (low < high) {
            const mid = Math.floor((low + high) / 2);
            if (nums[mid] > target || (left && nums[mid] === target)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    const leftIndex = getTargetIndex(true);
    const rightIndex = getTargetIndex(false) - 1;

    if (leftIndex <= rightIndex && leftIndex < n && rightIndex < n && nums[leftIndex] === target && nums[rightIndex] === target) {
        return [leftIndex, rightIndex];
    } 

    return [-1, -1];
};