# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/9/28: 19:50
"""
class Solution(object):

    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = ['']
        for c in s:
            if c == '(':
                stack.append('')
            elif c == ')':
                a = stack.pop()[::-1]
                stack[-1] += a
            else:
                stack[-1] += c
        return stack



if __name__=="__main__":
    s = "aa(bcdefghijkl(mno)p)q"
    solver = Solution()
    r = solver.reverseParentheses(s)
    print(r)