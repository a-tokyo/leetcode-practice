/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    let finalPos = nums.length - 1;
    for (let i = nums.length -1; i > -1; i-=1) {
        if (nums[i] + i >= finalPos) {
            finalPos = i
        }
    }
    return finalPos === 0;
};