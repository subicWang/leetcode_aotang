# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/8/30: 18:35
"""
class Solution(object):

    def __init__(self):
        pass

    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        res[i][j] = min(A[i-1][j-1], A[i-1][j], A[i-1][j+1]) + res[i-1][j]
        倒三角求最小路径
        """
        N = len(A)
        if N == 0:
            return None
        if N == 1:
            return A[0][0]
        for i in range(N - 1):
            for j in range(N):
                if j == 0:
                    A[i + 1][j] += min(A[i][j], A[i][j + 1])
                elif j == N - 1:
                    A[i + 1][j] += min(A[i][j - 1], A[i][j])
                else:
                    A[i + 1][j] += min(A[i][j - 1], A[i][j], A[i][j + 1])

        return min(A[-1])


if __name__ == "__main__":
    s = Solution()
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    res = s.minFallingPathSum(A)
    print(res)

