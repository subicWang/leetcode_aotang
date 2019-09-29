# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/9/26: 10:16
"""
from tools.min_heap import MinHeap
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        v = [float('-inf') for _ in range(k)]
        for num in nums:
            for i in range(k):
                if num > v[i]:
                    v[i+1:] = v[i:-1]
                    v[i] = num
                    break
        return v[-1]

    def findKthLargest1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        flag = True
        N = len(nums)
        if k<N/2:
            v = [float('-inf') for _ in range(k)]
        else:
            v = [float('inf') for _ in range(N-k+1)]
            flag = False
        if flag:
            for num in nums:
                for i in range(len(v)):
                    if num > v[i]:
                        v[i+1:] = v[i:-1]
                        v[i] = num
                        break
        else:
            for num in nums:
                for i in range(len(v)):
                    if num < v[i]:
                        v[i+1:] = v[i:-1]
                        v[i] = num
                        break
        return v[-1]
    def findKthLargest2(self, nums, k):
        """
        如果k< n/2最大堆，否则最小堆
        """
        N = len(nums)
        if k<=N/2:
            nums = [-i for i in nums]
            heapq.heapify(nums)
            res = float('inf')
            for _ in range(k):
                res = heapq.heappop(nums)
            return -res
        else:
            heapq.heapify(nums)
            res = float('-inf')
            for _ in range(len(nums) - k + 1):
                res = heapq.heappop(nums)
            return res
    def findKthLargest_minheap(self, nums, k):
        """
        将v = nums[:k]，然后最小堆排序，对新的值替换最小堆堆顶值。
        """
        heapq.heapify(nums)
        res = float('-inf')
        for _ in range(len(nums)-k+1):
            res = heapq.heappop(nums)
        return res

    def findKthLargest_maxheap(self, nums, k):
        nums = [-i for i in nums]
        heapq.heapify(nums)
        res = float('inf')
        for _ in range(k):
            res = heapq.heappop(nums)
        return -res

    def findKthLargest_maxheap2(self, it, n):
        """
        只创建k个元素的最大堆,后面的如果大于最大堆的最后一个元素则插入
        """
        result = [(elem, i) for i, elem in zip(range(0, -n, -1), it)]
        if not result:
            return result
        heapq.heapify(result)
        top = result[0][0]
        order = -n
        _heapreplace = heapq.heapreplace
        for elem in it[n:]:
            if top < elem:
                _heapreplace(result, (elem, order))
                top = result[0][0]
                order -= 1
        return result[0][0]


if __name__ == "__main__":
    nums = [2,1]
    s = Solution()
    r = s.findKthLargest_maxheap2(nums, 2)
    print(r)