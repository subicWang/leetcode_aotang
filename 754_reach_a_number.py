# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/9/15: 17:00
"""
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        i = 0
        sum = 0
        if target < 0:
            target = -target
        while sum < target:
            i += 1
            sum += i
        k = sum - target
        if k == 0:
            return i
        if k % 2 == 0:
            return i
        if k%2!=0 and i%2==0:
            return i+1
        if k%2!=0 and i%2 !=0:
            return i+2


if __name__ == "__main__":
    solver = Solution()
    input = 3
    print(solver.reachNumber(input))