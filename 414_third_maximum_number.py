# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/9/26: 9:30
"""
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        N = len(nums)
        if N<3:
            return max(nums)
        for j in range(3):
            for i in range(N-1-j):
                if nums[i] > nums[i+1]:
                    nums[i+1], nums[i] = nums[i], nums[i+1]
        return nums[-3]

    def thirdMax1(self, nums):
        nums = list(set(nums))
        N = len(nums)
        if N < 3:
            return max(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)

    def fabulous(self, nums):
        v = [float('-inf'), float('-inf'), float('-inf')]
        for num in nums:
            if num not in v:
                if num > v[0]: v = [num, v[0], v[1]]
                elif num > v[1]: v = [v[0], num, v[1]]
                elif num > v[2]: v = [v[0], v[1], num]
        return max(nums) if float('-inf') in v else v[2]



if __name__ == "__main__":
    nums = [2, 2, 3, 1]
    s = Solution()
    r = s.fabulous(nums)
    print(r)
