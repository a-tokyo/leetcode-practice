// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
// https://leetcode.com/submissions/detail/1604496716/

function removeDuplicates(nums: number[]): number {
    if (nums.length < 2) {
        return nums.length;
    }
    let currItemCount = 1;
    let lastValidIndex = 0;
    for (let i=1; i < nums.length; i++) {
        if (nums[i] === nums[i-1]) {
            currItemCount +=1;
        } else {
            currItemCount = 1;
        }
        if (currItemCount === 1 || currItemCount === 2) {
            lastValidIndex +=1;
            nums[lastValidIndex] = nums[i];
        }
    }
    return lastValidIndex + 1;
};