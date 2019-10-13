# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/10/11: 9:21
"""
import collections

class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        怎样找出island呢？ DFS搜索，找到island1和island2。
        然后将island1向外阔，看看是否和island2有交集，直到有交集，输出阔了多少圈。
        Runtime: 448 ms, faster than 46.60% of Python online submissions for Shortest Bridge.
        Memory Usage: 15.4 MB, less than 12.50% of Python online submissions for Shortest Bridge.
        """
        n = len(A)
        island1 = set()
        island2 = set()
        f = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        used = [[0 for _ in range(n)] for _ in range(n)]

        def dfs(island, x, y):
            for i, j in f:
                cur_x, cur_y = x + i, y + j
                if n > cur_x >= 0 and n > cur_y >= 0 and used[cur_x][cur_y] == 0:
                    used[cur_x][cur_y] = 1
                    if A[cur_x][cur_y] == 1 and (cur_x, cur_y) not in island:
                        island.add((cur_x, cur_y))
                        dfs(island, cur_x, cur_y)

        def get_island():
            flag = 0
            for i in range(n):
                for j in range(n):
                    if A[i][j] == 1:
                        if (i, j) not in island1:
                            if flag == 0:
                                island1.add((i, j))
                                dfs(island1, i, j)
                                flag = 1
                            else:
                                island2.add((i, j))
                                dfs(island2, i, j)
                                return island1, island2

        island1, island2 = get_island()
        Q = collections.deque(island1)
        l = 0
        while Q:
            for _ in range(len(Q)):
                x, y = Q.popleft()
                if (x, y) in island2:
                    return l - 1
                for i, j in f:
                    cur_x, cur_y = x + i, y + j
                    if n > cur_x >= 0 and n > cur_y >= 0 and (cur_x, cur_y) not in island1:
                        island1.add((cur_x, cur_y))
                        Q.append((cur_x, cur_y))
            l += 1


if __name__ == "__main__":
    # A = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
    A = [[0,1,0,0,0],[0,1,0,1,1],[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0]]
    solver = Solution()
    r = solver.shortestBridge(A)
    print(r)