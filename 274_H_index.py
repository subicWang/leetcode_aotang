# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/10/9: 9:39
"""
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        先逆向排序，然后找出h
        """
        L = len(citations)
        if sum(citations) < 1:
            return 0
        citations = sorted(citations, reverse=True)
        for i in range(1, len(citations)+1):
            if citations[i-1] >= i and (i == L or citations[i] <= i):
                return i


if __name__ == "__main__":
    citations = [11, 15]
    solver = Solution()
    r = solver.hIndex(citations)
    print(r)