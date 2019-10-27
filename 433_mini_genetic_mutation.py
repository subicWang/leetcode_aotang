# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/10/21: 9:27
"""
from collections import deque

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        bfs思想,队列中保持每个遍历的有效字符串和其突变的基因个数元组，即（start, step）元组。类似走迷宫，四个方向就是可变的四
        个字母"ACGT"，当突变后的字符串在bank中就step+1，终止条件就是突变后的字符串==end。其中增加visited来保存已经遇到过的有效
        突变字符串，以增加运算速度。

        Runtime: 12 ms, faster than 88.32% of Python online submissions for Minimum Genetic Mutation.
        Memory Usage: 11.7 MB, less than 100.00% of Python online submissions for Minimum Genetic Mutation.
        """
        if end not in bank:
            return -1
        queue = deque([(start, 0)])
        visited = set([start])
        while queue:
            v, step = queue.popleft()
            if v == end:
                return step
            for i in range(8):
                for c in "ACGT":
                    n = v[:i] + c + v[i+1:]
                    if n in bank and n not in visited:
                        visited.add(n)
                        print(n, step+1)
                        queue.append((n, step+1))
                        # bank.remove(n)
        return -1

    def minMutation_ori(self, start, end, bank):
        """
        :param start: "AACCGGTT"
        :param end: "AACCGCTA"
        :param bank: ["AACCGGTA","AACCGCTA","AAACGGTA"]
        :return: expected 2 output 3
        Error!
        要以元组的形式存入队列，这样每次遍历如果有多个在bank里，也就分别增加1。这样写会使得，在一次遍历中，后面突变的有效字符串count叠加,
        使得一次遍历突变两个基因时，count增加2。
        """
        if end not in bank:
            return -1
        queue = deque([start])
        visited = set([start])
        count = 0
        while queue:
            v = queue.popleft()
            if v == end:
                return count
            for i in range(8):
                for c in "ACGT":
                    n = v[:i] + c + v[i + 1:]
                    if n in bank and n not in visited:
                        count += 1
                        visited.add(n)
                        queue.append(n)

        return -1


if __name__ == '__main__':
    solver = Solution()
    start = "AACCGGTT"
    end = "AACCGCTA"
    bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    r = solver.minMutation(start, end, bank)
    print(r)