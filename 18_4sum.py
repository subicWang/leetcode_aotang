# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/11/15: 9:50
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        Runtime: 640 ms, faster than 54.10% of Python online submissions for 4Sum.
        Memory Usage: 11.9 MB, less than 22.73% of Python online submissions for 4Sum.
        """
        nums = sorted(nums)
        L = len(nums)
        if L < 4:
            return []
        if L == 4 and sum(nums) == target:
            return [nums]
        res4 = []
        def threeSum(nums3, target):
            res3 = []
            for i in range(len(nums3) - 2):
                n1 = nums3[i]
                if n1 > target>0:
                    return res3
                if i > 0 and nums3[i] == nums3[i - 1]:
                    continue
                j = i + 1
                k = len(nums3) - 1
                while j < k:
                    sum = n1 + nums3[j] + nums3[k]
                    if sum < target:
                        j += 1
                    elif sum > target:
                        k -= 1
                    else:
                        res3.append([n1, nums3[j], nums3[k]])
                        while j < k and nums3[j] == nums3[j + 1]:
                            j += 1
                        while j < k and nums3[k] == nums3[k - 1]:
                            k -= 1
                        j += 1
                        k -= 1
            return res3
        for i in range(L-3):
            if nums[i] > target > 0:
                return res4
            if i==0 or nums[i-1] != nums[i]:
                res3 = threeSum(nums[i+1:], target - nums[i])
                if len(res3) > 0:
                    for r in res3:
                        r.append(nums[i])
                        res4.append(r)
        return res4



if __name__ == '__main__':
    nums = [1,-2,-5,-4,-3,3,3,5]
    target = -11
    solver = Solution()
    r = solver.fourSum(nums, target)
    print(r)