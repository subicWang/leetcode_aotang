# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/11/7: 9:09
"""
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        Runtime: 36 ms, faster than 74.39% of Python online submissions for Integer to Roman.
        Memory Usage: 11.8 MB, less than 22.86% of Python online submissions for Integer to Roman.
        """
        num_dict = {1: "I",
                    4: "IV",
                    5: "V",
                    9: "IX",
                    10: "X",
                    40: "XL",
                    50: "L",
                    90: "XC",
                    100: "C",
                    400: "CD",
                    500: "D",
                    900: "CM",
                    1000: "M"}
        r = ""
        for i in range(3, -1, -1):
            key = int(10**i)
            n = num // key
            num %= key
            if n == 0:
                continue
            elif n < 4:
                r += num_dict[key]*n
            elif 5 < n < 9:
                r += num_dict[5*key]+num_dict[key]*(n-5)
            else:
                r += num_dict[key*n]
        return r


if __name__ == '__main__':
    Input = 58
    solver = Solution()
    r = solver.intToRoman(Input)
    print(r)