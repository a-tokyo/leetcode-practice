function longestConsecutive(nums: number[]): number {
    if (nums.length === 0) return 0;

    const numSet = new Set(nums);
    let maxGlobal = 0;

    for (const num of numSet) {
        if (!numSet.has(num - 1)) {
            let maxCurr = 1;
            let nextNum = num + 1;

            while (numSet.has(nextNum)) {
                maxCurr++;
                nextNum++;
            }

            maxGlobal = Math.max(maxGlobal, maxCurr);
        }
    }

    return maxGlobal;
};