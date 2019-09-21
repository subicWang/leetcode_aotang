# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/9/16: 10:00
"""
class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        暴力遍历，然后求最值
        """
        arrayLM = []
        for i in range(L, len(A)-M+1):
            sL = sum(A[i-L:i])
            for j in range(M+i, len(A)+1):
                sM = sum(A[j-M:j])
                arrayLM.append(sL+sM)
        arrayML = []
        for i in range(M, len(A) - L+1):
            sM = sum(A[i - M:i])
            for j in range(L+i, len(A)+1):
                sL = sum(A[j - L:j])
                arrayML.append(sM+sL)
        return max(max(arrayML), max(arrayLM))
    def maxSumTwoNoOverlap2(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        尽量减少重复性劳动
        step1. 一次遍历生成累加和arrayACC
        step2. L长的数组和为arrayACC[i+L] - arrayACC[i]
        """
        arrayACC = [0]
        N = len(A)
        for a in A:
            arrayACC.append(arrayACC[-1] + a)
        arrayLM = []
        for i in range(L, len(A) - M + 1):
            sL = arrayACC[i] - arrayACC[i-L]
            sL_ = sum(A[i - L:i])
            for j in range(M + i, len(A) + 1):
                sM = arrayACC[j] - arrayACC[j-M]
                sM_ = sum(A[j - M:j])
                arrayLM.append(sL + sM)
        arrayML = []
        for i in range(M, len(A) - L + 1):
            sM = arrayACC[i] - arrayACC[i-M]
            sM_ = sum(A[i - M:i])
            for j in range(L + i, len(A) + 1):
                sL = arrayACC[j] - arrayACC[j-L]
                sL_ = sum(A[j - L:j])
                arrayML.append(sM + sL)
        print(arrayLM)
        print(arrayML)
        return max(max(arrayML), max(arrayLM))
    def maxSumTwoNoOverlap3(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        尽量减少重复性劳动
        step1. 一次遍历生成累加和arrayACC
        step2. L长的数组和为arrayACC[i+L] - arrayACC[i]
        step3. L 后面的 M数组和依然有可以避免重复的地方
        """
        arrayACC = [0]
        N = len(A)
        for a in A:
            arrayACC.append(arrayACC[-1] + a)
        arrayM = []
        arrayL = []
        arrayLM = []
        arrayML = []
        for i in range(N-M+1):
            arrayM.append(arrayACC[i+M] - arrayACC[i])
        for i in range(N-L+1):
            arrayL.append(arrayACC[i+L] - arrayACC[i])
        for i in range(N-L-M+1):
            for j in range(i, N-M-L+1):
                arrayLM.append(arrayL[i] + arrayM[j+L])
                arrayML.append(arrayM[i] + arrayL[j+M])
        return max(max(arrayML), max(arrayLM))
    def maxSumTwoNoOverlap4(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        尽量减少重复性劳动
        step1. 一次遍历生成累加和arrayACC
        step2. L长的数组和为arrayACC[i+L] - arrayACC[i]
        step3. L 后面的 M数组和依然有可以避免重复的地方
        """
        arrayACC = [0]
        N = len(A)
        for a in A:
            arrayACC.append(arrayACC[-1] + a)
        arrayM = [arrayACC[i + M] - arrayACC[i] for i in range(N - M + 1)]
        arrayL = [arrayACC[i + L] - arrayACC[i] for i in range(N - L + 1)]
        arrayLM = []
        arrayML = []
        for i in range(N - L - M + 1):
            for j in range(i, N - M - L + 1):
                arrayLM.append(arrayL[i] + arrayM[j + L])
                arrayML.append(arrayM[i] + arrayL[j + M])
        return max(max(arrayML), max(arrayLM))

    def maxSumTwoNoOverlap5(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        尽量减少重复性劳动
        step1. 一次遍历生成累加和arrayACC
        step2. L长的数组和为arrayACC[i+L] - arrayACC[i]
        step3. L 后面的 M数组和依然有可以避免重复的地方
        """
        arrayACC = [0]
        N = len(A)
        for a in A:
            arrayACC.append(arrayACC[-1] + a)
        arrayM = [arrayACC[i + M] - arrayACC[i] for i in range(N - M + 1)]
        arrayL = [arrayACC[i + L] - arrayACC[i] for i in range(N - L + 1)]
        arrayMax = 0
        for i in range(N - L - M + 1):
            for j in range(i, N - M - L + 1):
                arrayMax = max(arrayL[i] + arrayM[j + L], arrayM[i] + arrayL[j + M], arrayMax)
        return arrayMax
    def maxSumTwoNoOverlap6(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        尽量减少重复性劳动
        step1. 一次遍历生成累加和arrayACC
        step2. L长的数组和为arrayACC[i+L] - arrayACC[i]
        step3. L 后面的 M数组和依然有可以避免重复的地方
        """
        arrayACC = [0]
        N = len(A)
        arrayMax = 0
        for a in A:
            arrayACC.append(arrayACC[-1] + a)
        if M+L == N:
            return arrayACC[-1]
        else:
            arrayM = [arrayACC[i + M] - arrayACC[i] for i in range(N - M + 1)]
            arrayL = [arrayACC[i + L] - arrayACC[i] for i in range(N - L + 1)]
            print(arrayM)
            print(arrayL)
            for i in range(1, N - L - M + 2):
                arrayMax = max(max(arrayL[:i]) + max(arrayM[i + L-1:]), max(arrayM[:i]) + max(arrayL[i + M-1:]), arrayMax)
        return arrayMax


if __name__ == "__main__":
    A = [4,5,14,16,16,20,7,13,8,15]
    L = 3
    M = 5
    # A = [1, 0, 3]
    # L = 1
    # M =2
    # A = [3, 8, 1, 3, 2, 1, 8, 9, 0]
    # L = 3
    # M = 2
    # A = [0, 6, 5, 2, 2, 5, 1, 9, 4]
    # L = 1
    # M = 2
    s = Solution()
    result = s.maxSumTwoNoOverlap6(A, L, M)
    print(result)