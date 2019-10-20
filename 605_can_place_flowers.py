# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/10/15: 9:33
"""
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        条件判断：1.只有零时：n = (len(f)+1)//2
                 2. 两边的零： n = len(f)//2
                 3. 两个1中间的零： n = (len(f)-1)//2
        Runtime: 156 ms, faster than 24.75% of Python online submissions for Can Place Flowers.
        Memory Usage: 11.8 MB, less than 100.00% of Python online submissions for Can Place Flowers.
        """
        N = 0
        f = "".join(str(i) for i in flowerbed)
        fs = [i for i in f.split("1") if len(i) > 0]
        if len(fs)==1 and sum(flowerbed)==0:
            N += (len(fs[-1])+1) // 2
            if n<=N:
                return True
            else:
                return False
        if len(fs)>0:
            if flowerbed[0] == 0:
                N += len(fs[0])//2
                fs = fs[1:]
        if len(fs) > 0:
            if flowerbed[-1] == 0:
                N += len(fs[-1]) // 2
                fs = fs[:-1]
        for i in fs:
            N += (len(i)-1)//2
            if N>=n:
                return True
        if N >= n:
            return True
        return False

    def canPlaceFlowers1(self, flowerbed, n):
        """
        在flowerbed两边加0，可以减少一种讨论情况。现在只有两种：1.只有零时：n = (len(f)+1)//2
                                                             2. 两个1中间的零： n = (len(f)-1)//2
        Runtime: 148 ms, faster than 55.39% of Python online submissions for Can Place Flowers.
        Memory Usage: 12 MB, less than 80.00% of Python online submissions for Can Place Flowers.
        """
        N = 0
        if sum(flowerbed) == 0:
            N += (len(flowerbed)+1) // 2
            if N >= n:
                return True
            else:
                return False
        flowerbed = [0] + flowerbed + [0]
        for i in "".join(map(str, flowerbed)).split("1"):
            N += (len(i)-1)//2
            if N>=n:
                return True
        if N >= n:
            return True
        return False


    def canPlaceFlowers_simple(self, flowerbed, n):
        if n==0:
            return True
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1]==flowerbed[i]==flowerbed[i+1]==0:
                flowerbed[i]=1
                n-=1
                if n==0:
                    return True
        return False

if __name__ == '__main__':
    flowerbed = [1,0,0,0,1]
    n = 2
    solver = Solution()
    r = solver.canPlaceFlowers1(flowerbed, n)
    print(r)
    # a = ["1", "2", "3"]
    # print("".join(a))