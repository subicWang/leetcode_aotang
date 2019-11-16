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
        通过一个index来将s分类到不同的行，通过step来调节index。调节条件是当index=0时，step=1,当index=numRows-1时，step=-1。
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
    # "PINALSIGYAHRPI"
    numRows = 4
    solver = Solution()
    r = solver.convert(s, numRows)
    print(r)