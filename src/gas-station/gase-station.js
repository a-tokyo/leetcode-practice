/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {
    const n = gas.length;
    let startIndex = 0;
    let totalTank = 0;
    let currTank = 0;
    for (let i=0; i < n; i++) {
        totalTank += gas[i] - cost[i];
        currTank += gas[i] - cost[i];
        if (currTank < 0) {
            currTank = 0;
            startIndex = i + 1;
        }
    }

    return totalTank >= 0 ? startIndex : - 1;
};