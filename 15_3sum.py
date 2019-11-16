# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/11/12: 9:21
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        fix一个数，其他两个数的和为这个数的负数。怎么找这两个数？遍历？或者用排序后双指针索引。
        Runtime: 2380 ms, faster than 5.04% of Python online submissions for 3Sum.
        Memory Usage: 16.3 MB, less than 9.61% of Python online submissions for 3Sum.
        没有TLE，不容易啊！想想怎么提个速？
        """
        r = set()
        L = len(nums)
        nums = sorted(nums)
        for i in range(L-2):
            n1 = nums[i]
            j = i+1
            k = L-1
            while j < k:
                sum = n1 + nums[j] + nums[k]
                if sum == 0:
                    r.add("_".join([str(s) for s in [n1, nums[j], nums[k]]]))
                    j += 1
                    k -= 1
                elif sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
        res = []
        for s in r:
            res.append([int(c) for c in s.split("_")])
        return res

    def threeSum1(self, nums):
        """
        加入剪枝，遍历到正数时就break
        Runtime: 2276 ms, faster than 5.04% of Python online submissions for 3Sum.
        Memory Usage: 16.3 MB, less than 9.61% of Python online submissions for 3Sum.
        提高了100ms，加油！
        """
        r = set()
        L = len(nums)
        nums = sorted(nums)
        for i in range(L-2):
            n1 = nums[i]
            if n1 > 0:
                break
            j = i+1
            k = L-1
            while j < k:
                sum = n1 + nums[j] + nums[k]
                if sum == 0:
                    r.add("_".join([str(s) for s in [n1, nums[j], nums[k]]]))
                    j += 1
                    k -= 1
                elif sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
        res = []
        for s in r:
            res.append([int(c) for c in s.split("_")])
        return res
    def threeSum2(self, nums):
        """
        Runtime: 528 ms, faster than 94.17% of Python online submissions for 3Sum.
        Memory Usage: 15.2 MB, less than 21.15% of Python online submissions for 3Sum.
        惊讶不惊讶？
        """
        r = []
        L = len(nums)
        if L<3:
            return []
        nums = sorted(nums)
        if nums[0] == nums[-1] == 0:
            return [[0, 0, 0]]
        for i in range(L-2):
            n1 = nums[i]
            if n1 > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = L-1
            while j < k:
                sum = n1 + nums[j] + nums[k]
                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    r.append([n1, nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
        return r


if __name__ == '__main__':
    nums = [1, 1, -2]
    solver = Solution()
    r = solver.threeSum2(nums)
    print(r)