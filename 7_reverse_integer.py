# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/11/4: 9:08
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        numeric=>str=>numeric
        Runtime: 28 ms, faster than 8.41% of Python online submissions for Reverse Integer.
        Memory Usage: 11.8 MB, less than 39.78% of Python online submissions for Reverse Integer.
        """
        if x<0:
            r = -1*int(str(-x)[::-1])
        else:
            r = int(str(x)[::-1])
        if 2**31-1 < r < -2**31:
        # if 2**31-1> r or r < -2**31:  TODO 上面那种表达会比下面注释的这行快很多。
            return r
        else:
            return 0


if __name__ == '__main__':
    Input = 1534236469
    solver = Solution()
    r = solver.reverse(Input)
    print(r)


