# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/10/26: 9:10
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows > len(s) or numRows == 1:
            return s
        L = [""]*numRows
        index, step = 0, 1
        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows-1:
                step = -1
            index += step
        return "".join(L)


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 4
    solver = Solution()
    r = solver.convert(s, numRows)
    print(r)