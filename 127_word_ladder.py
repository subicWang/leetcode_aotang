# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/10/22: 9:08
"""
from collections import deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        Time Limit Exceeded
        """
        if endWord not in wordList:
            return 0
        queue = deque([(beginWord, 1)])
        visted = set([beginWord])
        chars = [chr(ord('a')+i) for i in range(26)]
        while queue:
            word, step = queue.popleft()
            if word == endWord:
                return step
            for i in range(len(word)):
                for c in chars:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in wordList and new_word not in visted:
                        visted.add(new_word)
                        print(new_word, step+1)
                        queue.append((new_word, step+1))
        return 0
    def ladderLength1(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        Runtime: 388 ms, faster than 47.79% of Python online submissions for Word Ladder.
        Memory Usage: 13.1 MB, less than 59.46% of Python online submissions for Word Ladder.
        """
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        queue = deque([(beginWord, 1)])
        visted = set([beginWord])
        chars = [chr(ord('a')+i) for i in range(26)]
        while queue:
            word, step = queue.popleft()
            if word == endWord:
                return step
            for i in range(len(word)):
                for c in chars:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in wordList and new_word not in visted:
                        visted.add(new_word)
                        print(new_word, step+1)
                        queue.append((new_word, step+1))
                        # wordList.remove(new_word)
        return 0



if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    solver = Solution()
    r = solver.ladderLength(beginWord, endWord, wordList)
    print(r)