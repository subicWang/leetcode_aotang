# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/9/3: 9:16
"""
class Solution(object):
    def __init__(self):
        pass

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return sum(nums)
        res = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            res = [res[1], max(res[1], res[0] + nums[i])]
        return res[-1]


if __name__ == "__main__":
    nums = [2, 7, 9, 3, 1]
    solver = Solution()
    res = solver.rob(nums)
    print(res)