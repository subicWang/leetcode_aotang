# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/11/13: 9:30
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        Runtime: 132 ms, faster than 34.04% of Python online submissions for 3Sum Closest.
        Memory Usage: 11.9 MB, less than 9.68% of Python online submissions for 3Sum Closest.
        """
        nums = sorted(nums)
        L = len(nums)
        r = float('inf')
        if L<3:
            return sum(nums)
        for i in range(L-2):
            j = i+1
            k = L-1
            while j<k:
                Sum = nums[i] + nums[j] + nums[k]
                if abs(r - target) > abs(Sum - target):
                    r = Sum
                if Sum == target:
                    return r
                elif Sum < target:
                    j += 1
                else:
                    k -= 1
        return r
    def threeSumClosest1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        剪枝
        Runtime: 100 ms, faster than 64.00% of Python online submissions for 3Sum Closest.
        Memory Usage: 11.8 MB, less than 61.29% of Python online submissions for 3Sum Closest.
        """
        nums = sorted(nums)
        L = len(nums)
        r = sum(nums[:3])
        if L<3:
            return sum(nums)
        for i in range(L-2):
            if nums[i] > target > 0:
                return r
            j = i+1
            k = L-1
            while j<k:
                Sum = nums[i] + nums[j] + nums[k]
                if abs(r - target) > abs(Sum - target):
                    r = Sum
                if Sum == target:
                    return r
                elif Sum < target:
                    j += 1
                else:
                    k -= 1
        return r
    def threeSumClosest2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        剪枝
        Runtime: 72 ms, faster than 96.61% of Python online submissions for 3Sum Closest.
        Memory Usage: 12 MB, less than 6.45% of Python online submissions for 3Sum Closest.
        """
        nums = sorted(nums)
        L = len(nums)
        r = sum(nums[:3])
        if L<3:
            return r
        for i in range(L-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > target > 0:
                return r
            j = i+1
            k = L-1
            while j<k:
                Sum = nums[i] + nums[j] + nums[k]
                if abs(r - target) > abs(Sum - target):
                    r = Sum
                if Sum == target:
                    return r
                elif Sum < target:
                    j += 1
                else:
                    k -= 1
        return r


if __name__ == '__main__':
    nums = [6,-18,-20,-7,-15,9,18,10,1,-20,-17,-19,-3,-5,-19,10,6,-11,1,-17,-15,6,17,-18,-3,16,19,-20,-3,-17,-15,-3,12,1,-9,4,1,12,-2,14,4,-4,19,-20,6,0,-19,18,14,1,-15,-5,14,12,-4,0,-10,6,6,-6,20,-8,-6,5,0,3,10,7,-2,17,20,12,19,-13,-1,10,-1,14,0,7,-3,10,14,14,11,0,-4,-15,-8,3,2,-5,9,10,16,-4,-3,-9,-8,-14,10,6,2,-12,-7,-16,-6,10]
    target = -52
    solver = Solution()
    r = solver.threeSumClosest1(nums, target)
    print(r)
