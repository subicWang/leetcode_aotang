# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/9/29: 21:41
"""
from functools import lru_cache

class Solution(object):

    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        dp问题，转移关系为dp[i][t] = sum(dp[i-1][t-j]) for j in range(1, min(t, f))
        dp[i][t] 表示 i个筛子和为t的方法种类。
        初始化dp[0][0] = 1
        :return dp[d][target]
        """
        mod = 10**9+7

        @lru_cache(maxsize=None)
        def dp(i, t):
            if i == 0: return 1 if t == 0 else 0
            # pruning time
            if t > i*f or t < i:
                return 0
            r = 0
            for j in range(1, f+1):
                r = (r + dp(i-1, t-j)) % mod
            return r
        return dp(d, target)



if __name__ == "__main__":
    d = 1
    f = 5
    target = 2
    solver = Solution()
    r = solver.numRollsToTarget(d, f, target)
    print(r)


