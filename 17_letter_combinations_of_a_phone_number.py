# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/11/14: 9:26
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        Runtime: 16 ms, faster than 76.95% of Python online submissions for Letter Combinations of a Phone Number.
        Memory Usage: 11.7 MB, less than 61.90% of Python online submissions for Letter Combinations of a Phone Number.
        """
        if len(digits)<1:
            return []
        s = ["", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = [""]
        for i in digits:
            if i != "1":
                cur_s = s[int(i)-1]
                tmp = []
                for c in cur_s:
                    tmp.extend([i+c for i in res])
                res = tmp
        return res


if __name__ == '__main__':
    Input = "23"
    solver = Solution()
    r = solver.letterCombinations(Input)
    print(r)