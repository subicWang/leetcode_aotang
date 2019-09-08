# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/9/4: 9:35
"""
import math
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        N = len(points)
        if N < 1:
            return
        points = sorted(points)
        zone = [points[0][0], points[0][1]]
        nums = 1
        for i in range(1, N):
            point = points[i]
            if point[0] > zone[0]:
                zone[0] = point[0]
            if point[1] < zone[1]:
                zone[1] = point[1]
            if point[0] > zone[1]:
                nums += 1
                zone = point
        return nums




if __name__ == "__main__":
    input = [[10, 16], [2, 8], [1, 6], [7, 12]]
    s = Solution()
    res = s.findMinArrowShots(input)
    print(res)