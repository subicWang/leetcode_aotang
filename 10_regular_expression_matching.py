# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/11/5: 10:00
"""
import re
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        r = re.search(p, s)
        if r is None:
            return False
        if r.group() == s:
            return True
        else:
            return False


if __name__ == '__main__':
    s = "ab"
    p = ".*c"
    solver = Solution()
    r = solver.isMatch(s, p)
    print(r)