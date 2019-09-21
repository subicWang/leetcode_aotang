# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/9/20: 10:08
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in nums[i+1:]:
                for j in range(i+1, len(nums)):
                    if nums[j] == dif:
                        return [i, j]
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        hash索引
        **厉害**
        """
        N = len(nums)
        kv = {}
        for i in range(N):
            if nums[i] in kv:
                return [kv[nums[i]], i]
            else:
                kv[target -nums[i]] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print(s.twoSum1(nums, target))