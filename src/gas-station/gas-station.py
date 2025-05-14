class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start_index = 0
        curr_tank = 0
        max_tank = 0
        for i in range(len(gas)):
            curr_tank += gas[i] - cost[i]
            max_tank += gas[i] - cost[i]
            if curr_tank < 0:
                curr_tank = 0
                start_index = i+1
        return start_index if max_tank >=0 else -1
        