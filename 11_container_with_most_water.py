# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/11/6: 9:26
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        暴力遍历 Time Limit Exceeded
        """
        L = len(height)
        maxA = 0
        for i in range(L):
            for j in range(i+1, L):
                h = min(height[i], height[j])
                l = j-i
                maxA = max(maxA, h*l)
        return maxA

    def maxArea1(self, height):
        """

        :param height:
        :return:
        一次遍历：从两端i，j开始，如果最左比最右小，则如果遍历所有，其中有值大于最左，h依然等于最左，但l不变。如果有值小于最左，则h更小。
        所以只需计算两端和距离的乘积。此时如果左小则i+1，如果右小则j-1。
        参考：https://leetcode.com/problems/container-with-most-water/discuss/6099/Yet-another-way-to-see-what-happens-in-the-O(n)-algorithm
        Runtime: 104 ms, faster than 72.03% of Python online submissions for Container With Most Water.
        Memory Usage: 13.2 MB, less than 22.03% of Python online submissions for Container With Most Water.
        """
        i = 0
        j = len(height)-1
        maxA = 0
        while i < j:
            if height[i] <= height[j]:
                maxA = max(maxA, height[i] * (j - i))
                i += 1
            else:
                maxA = max(maxA, height[j] * (j - i))
                j -= 1
        return maxA


if __name__ == '__main__':
    Input = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # Output: 49
    solver = Solution()
    r = solver.maxArea1(Input)
    print(r)