# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/9/3: 9:44
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        第一个和最后一个不能同时抢
        """
        N = len(nums)
        if N <= 1:
            return sum(nums)
        res0 = [0, nums[1]]
        for i in range(2, N):
            res0 = [res0[1], max(res0[1], res0[0] + nums[i])]
        res1 = [nums[0], max(nums[0], nums[1])]
        for i in range(2, N -1):
            res1 = [res1[1], max(res1[1], res1[0] + nums[i])]

        return max(res0[-1], res1[-1])


if __name__ == "__main__":
    nums = [1, 2, 1, 1]
    solver = Solution()
    res = solver.rob(nums)
    print(res)