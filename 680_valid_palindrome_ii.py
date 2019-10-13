# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/10/13: 19:18
"""
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        Time Limit Exceeded
        """
        N = len(s)
        if N == 0:
            return True
        def isPalindrome(s, N):
            flag = True
            n = int(N / 2)
            for i in range(n):
                flag = flag and s[i] == s[-(i+1)]
            return flag

        s = list(s)
        if not isPalindrome(s, N):
            for i in range(N):
                s0 = s[:i] + s[i+1:]
                if isPalindrome(s0, N-1):
                    return True
            return False
        return True

    def validPalindrome1(self, s):
        """
        :type s: str
        :rtype: bool
        使用索引的方法从两边往中间走，如果不等则跳过,如果左右两边跳过后有一边回文，则返回True否则返回False.
        """
        N = len(s)
        if N == 0:
            return True
        l = 0
        r = N-1
        while l<r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                one, two = s[l: r], s[l+1: r+1]
                return one == one[::-1] or two == two[::-1]
        return True

if __name__ == "__main__":
    s = "ABC"
    solver = Solution()
    r = solver.validPalindrome1(s)
    print(r)