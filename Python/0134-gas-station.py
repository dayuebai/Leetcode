# Time: O(N)
# Space: O(1)
class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        res = 0
        total = 0
        res_total = 0

        for i in range(n):
            tmp = gas[i] - cost[i]
            total += tmp
            res_total += tmp
            if res_total < 0:
                res_total = 0
                res = i + 1
        if total < 0:
            return -1
        else:
            return res