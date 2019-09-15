# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/9/9: 10:06
"""
class Solution(object):
    def __init__(self):
        pass

    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        1. 跑完一圈必须sum(gas)>=sum(cost)
        2. 到下一个节点时，当前气体为cur_gas += gas[i] - cost[i]
        3. 如果当前气体大于0，则起始点为该点，否则cur_gas=0且起始点为下一个点。
        4. 如果遍历一遍之后，cur_gas>=0则返回起始点，否则返回-1.
        """
        if sum(gas) < sum(cost):
            return -1
        cur_gas = 0
        cur_point = 0
        start_point = 0
        N = len(gas)
        for i in range(N):
            cur_gas += gas[i] - cost[i]
            if cur_gas > 0:
                start_point = cur_point
            else:
                cur_gas = 0
                cur_point = i+1
        if cur_gas >= 0:
            return start_point
        else:
            return -1


if __name__ == "__main__":
    solver = Solution()
    gas = [3, 1, 1]
    cost = [1, 2, 2]

    res = solver.canCompleteCircuit(gas, cost)
    print(res)
