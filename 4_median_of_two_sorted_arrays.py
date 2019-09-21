# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/9/17: 9:33
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        Num_1 = len(nums1)
        Num_2 = len(nums2)
        Num_all = Num_1 + Num_2
        flage = Num_all % 2
        Num_stop = Num_all//2
        i = 0
        j = 0
        nums = []
        for _ in range(Num_stop+1):
            if i<Num_1 and j<Num_2:
                if nums1[i] < nums2[j]:
                    nums.append(nums1[i])
                    i += 1
                else:
                    nums.append(nums2[j])
                    j += 1
            elif i>= Num_1:
                nums.append(nums2[j])
                j += 1
            else:
                nums.append(nums1[i])
                i += 1
        if flage:
            return nums[-1]
        else:
            return (nums[-1] + nums[-2])/2.


if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    s = Solution()
    r = s.findMedianSortedArrays(nums1, nums2)
    print(r)

