# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/11/5: 9:07
"""
import re
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        正则表达
        Runtime: 16 ms, faster than 93.99% of Python online submissions for String to Integer (atoi).
        Memory Usage: 11.7 MB, less than 56.67% of Python online submissions for String to Integer (atoi).
        """
        str = str.strip()
        Pattern = "^[+,-]?\d+"
        r = re.findall(Pattern, str)
        if len(r) == 0:
            return 0
        else:
            rint = int(r[0])
            if -2 ** 31 <= rint <= 2 ** 31 - 1:
                return rint
            elif -2 ** 31 > rint:
                return -2 ** 31
            else:
                return 2 ** 31 - 1

if __name__ == '__main__':
    Input = "  +42"
    # Output: -42
    solver = Solution()
    r = solver.myAtoi(Input)
    print(r)