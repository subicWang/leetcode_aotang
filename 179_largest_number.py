# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/10/14: 9:20
"""
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        归并排序失败，不能比较所有数据。
        """
        def compare(left, right):
            s1 = left+right
            s2 = right+left
            if s1>s2:
                return 0
            else:
                return 1
        def merge(left, right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if compare(left[i], right[j]):
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result += left[i:]
            result += right[j:]
            return result

        nums = [str(i) for i in nums]
        N = len(nums)
        if N <= 1:
            return nums[0]
        middle = int(N/2)
        left = nums[:middle]
        right = nums[middle:]
        result = merge(left, right)
        return ''.join(result[::-1])

    def largestNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        插入排序。 比较慢。O(n2)
        Runtime: 36 ms, faster than 28.00% of Python online submissions for Largest Number.
        Memory Usage: 11.6 MB, less than 62.50% of Python online submissions for Largest Number.
        """
        def compare(left, right):
            if left+right<right+left:
                return 0
            else:
                return 1

        def insert_sort(alist):
            for j in range(1, len(alist)):
                for i in range(j, 0, -1):
                    if compare(alist[i], alist[i-1]):
                        alist[i], alist[i-1] = alist[i-1], alist[i]
                    else:
                        break
            return alist

        if sum(nums) == 0:
            return "0"
        nums = list(map(str, nums))
        N = len(nums)
        if N <= 1:
            return nums[0]
        result = insert_sort(nums)
        return ''.join(result)

    def largestNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        排序问题，不过得重新定义大小比较方法，快速排序O(nlog(2n))
        Runtime: 28 ms, faster than 59.82% of Python online submissions for Largest Number.
        Memory Usage: 11.6 MB, less than 62.50% of Python online submissions for Largest Number.
        """
        def quickSort(nums):  # 这种写法的平均空间复杂度为 O(nlogn)
            if len(nums) <= 1:
                return nums
            pivot = nums[0]  # 基准值
            left = [nums[i] for i in range(1, len(nums)) if nums[i]+pivot < pivot+nums[i]]
            right = [nums[i] for i in range(1, len(nums)) if nums[i]+pivot >= pivot+nums[i]]
            return quickSort(left) + [pivot] + quickSort(right)

        nums = list(map(str, nums))
        result = quickSort(nums)
        return ''.join(result[::-1]).lstrip('0') or '0' ##############Beautiful!#################

    def so_simple(self, nums):
        nums = [str(x) for x in nums]
        # nums.sort(cmp=lambda x, y: cmp(x + y, y + x)) python2
        # from functools import cmp_to_key
        # sorted(nums, key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)))
        return ''.join(nums).lstrip('0') or '0'




if __name__ == "__main__":
    nums = [1,2,3,1]
    solver = Solution()
    r = solver.so_simple(nums)
    print(r)
