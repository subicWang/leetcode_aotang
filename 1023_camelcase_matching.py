# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/10/29: 9:49
"""
import re
class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        根据条件判断，如果搜索对象是大写但不是模板的顺序则为False.
        """
        res = []
        for q in queries:
            val = True
            start = 0
            for i in range(0, len(q)):
                if start < len(pattern) and q[i] == pattern[start]:
                    start += 1
                    continue
                if q[i].isupper():
                    val = False
                    break
            if start < len(pattern):
                val = False
            res.append(val)
        return res

    def camelMatch1(self, queries, pattern):
        """
        模式匹配的题，正则表达。
        """
        P ="^[a-z]*"
        for i, v in enumerate(pattern):
            P += v
            P += "[a-z]*"
        P += "$"
        result = []
        for query in queries:
            r = re.search(P, query)
            if r is None:
                result.append(False)
                continue
            rg = query[len(r.group()):]
            if len(rg)==0 or rg.islower():
                result.append(True)
            else:
                result.append(False)
        return result

if __name__ == '__main__':
    # queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
    # pattern = "FB"
    # queries = ["aksvbjLiknuTzqon", "ksvjLimflkpnTzqn", "mmkasvjLiknTxzqn", "ksvjLiurknTzzqbn", "ksvsjLctikgnTzqn",
    #  "knzsvzjLiknTszqn"]
    # pattern = "ksvjLiknTzqn"
    queries = ["CompetitiveProgramming", "CounterPick", "ControlPanel"]
    pattern = "CooP"
    solver = Solution()
    r = solver.camelMatch1(queries, pattern)
    print(r)
