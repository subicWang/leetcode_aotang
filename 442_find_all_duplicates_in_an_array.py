# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/9/18: 9:53
"""
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        遍历，将值对应index位置取负号，再遍历一次，如果为正，则出现了两次。由于1<=a[i]<=n, n=size of array.
        """
        output = []
        for n in nums:
            if nums[abs(n)-1] < 0:
                output.append(abs(n))
            # nums[abs(n) - 1] *= -1
            else:
                nums[abs(n)-1] *= -1
        return output




if __name__ =="__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    s = Solution()
    r = s.findDuplicates(nums)
    print(r)