# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/11/8: 9:16
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        i = 0
        while i<len(s)-1:
            if (s[i]=='I' and s[i+1] in ['V', 'X']) or (s[i]=='X' and s[i+1] in ['L', 'C']) or (s[i]=='C' and s[i+1] in ['D', 'M']):
                num -= roman_dict[s[i]]
            else:
                num += roman_dict[s[i]]
            i += 1
        num += roman_dict[s[-1]]
        return num


if __name__ == '__main__':
    Input = 'IX'
    solver = Solution()
    r = solver.romanToInt(Input)
    print(r)