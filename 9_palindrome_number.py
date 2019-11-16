# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/11/5: 9:52
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if x==x[::-1]:
            return True
        else:
            return False


if __name__ == '__main__':
    Input = 121
    solver = Solution()
    r = solver.isPalindrome(Input)
    print(r)