# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/10/14: 21:12
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        Runtime: 12 ms, faster than 96.41% of Python online submissions for Reverse Words in a String.
        Memory Usage: 13.1 MB, less than 51.22% of Python online submissions for Reverse Words in a String.
        """
        s = [i for i in s.split(" ") if len(i)>0]
        return " ".join(s[::-1])

if __name__ == "__main__":
    # Input: "the sky is blue"
    # Output: "blue is sky the"
    # Input: "  hello world!  "
    # Output: "world! hello"
    Input = "  hello world!  "
    solver = Solution()
    r = solver.reverseWords(Input)
    print("Output: ", r)