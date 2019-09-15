# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/9/12: 9:33
"""
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = sorted(nums, reverse=True)
        s = sum(nums)
        if s % 2 != 0:
            return False
        len_nums = len(nums)
        capacity = s // 2
        mem = [False] * (capacity + 1)

        for i in range(capacity + 1):
            mem[i] = (nums[0] == i)

        for k in range(1, len_nums):
            for j in range(capacity, nums[k] - 1, -1):
                mem[j] = mem[j] or mem[j - nums[k]]

        return mem[capacity]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    s = Solution()
    print(s.canPartition(nums))