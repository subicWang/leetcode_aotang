# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/10/15: 19:29
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        #first_edition.Time Limit Exceeded
        """
        L = len(s)
        if L <= 1:
            return L
        else:
            dp = [1 for _ in range(L)]
            for i in range(L):
                tmp = ""
                for j in range(i, L-1):
                    tmp += str(s[j])
                    if str(s[j+1]) not in tmp:
                        dp[i] += 1
                    else:
                        break
            # print(dp)
            return max(dp)
    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        #second_edition.前一个数已经统计了它后面有多少个不重复的数，此时直接利用这个数，而不是重新统计。
        #TODO: time limited exceeded.
        """
        L = len(s)
        if L <= 1:
            return L
        else:
            dp = [0 for _ in range(L)]
            tmp = ''
            for i in range(L):
                if i > 0:
                    dp[i] += dp[i - 1] - 1
                index_start = dp[i]+i
                for j in range(index_start, L):
                    if str(s[j]) in tmp:
                        break
                    tmp += str(s[j])
                dp[i] = len(tmp)
                tmp = tmp[1:]
            print(dp)
            return max(dp)

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        #second_edition.前一个数已经统计了它后面有多少个不重复的数，此时直接利用这个数，而不是重新统计。
        #TODO: time limited exceeded.
        """
        L = len(s)
        if L <= 1:
            return L
        else:
            dp = [0, 0]
            n_max = 0
            for i in range(L):
                tmp = set(s[i:i + dp[0]])
                if i > 0:
                    dp[1] += dp[0] - 1
                index_start = dp[1] + i
                for j in range(index_start, L):
                    if s[j] in set(tmp):
                        break
                    tmp.add(s[j])
                dp = [len(tmp), 0]
                n_max = max(n_max, len(tmp))
            return n_max

    def lengthOfLongestSubstring3(self, s):
        """
        一次遍历, 利用hashmap(字典对)来搜索左指针,即遇到重复char时，则记录该char之前的位置。
        Runtime: 32 ms, faster than 96.28% of Python online submissions for Longest Substring Without Repeating Characters.
        Memory Usage: 12.9 MB, less than 12.50% of Python online submissions for Longest Substring Without Repeating Characters.
        """
        s_dict = {}
        left = 0
        r = 0
        for i in range(len(s)):
            if s[i] in s_dict and s_dict[s[i]]>left:
                left = s_dict[s[i]]
            s_dict[s[i]] = i
            r = max(r, i - left)
        return r



if __name__ == '__main__':
    s = "ohomm"
    solver = Solution()
    r = solver.lengthOfLongestSubstring3(s)
    print(r)