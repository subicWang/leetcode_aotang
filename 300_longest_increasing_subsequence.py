# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/10/10: 19:08
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        当新来一个数时，它前面的数比它小时，则这个数对应的最长子序列数加1.
        Runtime: 1012 ms, faster than 31.44% of Python online submissions for Longest Increasing Subsequence.
        Memory Usage: 11.9 MB, less than 75.00% of Python online submissions for Longest Increasing Subsequence.
        """
        L = len(nums)
        if L==0:
            return 0
        if L==1:
            return 1
        else:
            dp = [1 for _ in range(L)]
            dp_v = nums
            res = 0
            for i in range(L):
                for j in range(i):
                    if nums[j]<nums[i]:
                        dp[i] = max(dp[i], dp[j] +1)
                res = max(res, dp[i])
        return res


if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    solver = Solution()
    r = solver.lengthOfLIS(nums)
    print(r)