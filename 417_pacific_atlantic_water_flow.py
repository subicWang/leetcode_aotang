# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/9/23: 9:43
"""

class Solution(object):
    def pacificAtlantic_noAC1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        寻找数组中的行最大或者列最大的值的索引。每一个数都在其横向和纵向比较。【too young to simple】
        """
        results = []
        for i in range(len(matrix)):
            m = max(matrix[i])
            flag = False
            loc = 0
            for j in range(len(matrix[i])):
                if matrix[i][j] == m:
                    if flag == False:
                        loc = j
                        flag = True
                        results.append([i, j])
                    elif j - loc == 1:
                        results.append([i, j])

        for j in range(len(matrix[0])):
            m_col = [matrix[i][j] for i in range(len(matrix))]
            m = max(m_col)
            for i in range(len(m_col)):
                if m_col[i] == m:
                    if [i,j] not in results:
                        results.append([i, j])
        return results

    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        分别从四边出发，上左两边为太平洋，下右两边为大西洋，并记录每个位置的点能到达的位置， 最后对太平洋和大西洋能够到达的点集合求交集。
        """
        if not matrix or not matrix[0]: return []
        m, n = len(matrix), len(matrix[0])
        p_visited = [[False]*n for _ in range(m)]
        a_visited = [[False]*n for _ in range(m)]
        for i in range(m):
            self.dfs(p_visited, matrix, m, n, i, 0)
            self.dfs(a_visited, matrix, m, n, i, n-1)
        for j in range(n):
            self.dfs(p_visited, matrix, m, n, 0, j)
            self.dfs(a_visited, matrix, m, n, m-1, j)
        res = []
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    res.append([i, j])
                    print([i, j], matrix[i][j])
        return res

    def dfs(self, visited, matrix, m, n, i, j):
        visited[i][j] = True
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for dire in directions:
            x, y = i + dire[0], j + dire[1]
            if x<0 or y<0 or x>=m or y>=n or visited[x][y] or matrix[x][y] < matrix[i][j]:
                continue
            self.dfs(visited, matrix, m, n, x, y)


if __name__ == "__main__":
    matrix = [[1,2,2,3,5],
              [3,2,3,4,4],
              [2,4,5,3,1],
              [6,7,1,4,5],
              [5,1,1,2,4]]
    s = Solution()
    r = s.pacificAtlantic(matrix)
    print(r)



