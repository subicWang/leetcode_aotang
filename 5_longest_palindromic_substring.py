# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/10/18: 11:58
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        暴力遍历
        """
        def isPalindrome(s):
            if s == s[::-1]:
                return True
            else:
                return False
        L = len(s)
        # if L <= 1:
        #     return s
        res = ""
        for i in range(L):
            for j in range(i+1, L+1):
                if isPalindrome(s[i:j]):
                    if len(s[i:j])>len(res):
                        res = s[i:j]
        return res
    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        如果长度低于之前的最长字符串，则可以跳过
        Runtime: 5052 ms, faster than 17.12% of Python online submissions for Longest Palindromic Substring.
        Memory Usage: 11.9 MB, less than 50.68% of Python online submissions for Longest Palindromic Substring.
        """
        def isPalindrome(s):
            if s == s[::-1]:
                return True
            else:
                return False
        L = len(s)
        L_sub = 0
        res = ""
        for i in range(L):
            for j in range(i+1+L_sub, L+1):
                if isPalindrome(s[i:j]):
                    if len(s[i:j]) > len(res):
                        res = s[i:j]
                        L_sub = len(s[i:j])
        return res
    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        如果剩余字符串的长度低于之前的最长字符串，则可以退出
        """
        def isPalindrome(s):
            if s == s[::-1]:
                return True
            else:
                return False

        L = len(s)
        L_sub = 0
        res = ""
        for i in range(L):
            if L-i < L_sub:
                break
            for j in range(i+1+L_sub, L+1):
                if isPalindrome(s[i:j]):
                    if len(s[i:j]) > len(res):
                        res = s[i:j]
                        L_sub = len(s[i:j])
        return res
    def longestPalindrome3(self, s):
        """
        :type s: str
        :rtype: str
        定义start, maxlen, 表示最长回文串的起点和长度，
        """
        pass



if __name__ == '__main__':
    # Input: "babad"
    # Output: "bab"
    s = "babad"
    solver = Solution()
    r = solver.longestPalindrome2(s)
    print(r)