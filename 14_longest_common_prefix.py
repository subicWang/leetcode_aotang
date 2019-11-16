# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/11/11: 9:41
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        Runtime: 16 ms, faster than 91.88% of Python online submissions for Longest Common Prefix.
        Memory Usage: 11.9 MB, less than 70.00% of Python online submissions for Longest Common Prefix.
        """
        if len(strs) == 0:
            return ""
        i = 0
        com_pre = ""
        flag = False
        while i<len(strs[0]):
            tmp = strs[0][i]
            for s in strs:
                if i<len(s):
                    if s[i] == tmp:
                        continue
                    else:
                        flag = True
                        break
                else:
                    flag = True
                    break
            if flag:
                break
            else:
                com_pre += tmp
                i += 1
        return com_pre

    def longestCommonPrefix_simple(self, strs):
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest





if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    solver = Solution()
    r = solver.longestCommonPrefix(strs)
    print(r)