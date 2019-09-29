# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/9/27: 9:25
"""

class MinHeap(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.data = []
        self.count = len(self.data)

    def __sizeof__(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def insert(self, item):
        if self.__sizeof__() >= self.maxsize:
            raise Exception('full')
        self.data.append(item)
        self.count += 1
        self.shiftup(self.count-1)

    def shiftup(self, ndx):
        # 将插入的元素放到合适的位置，保持最小堆
        if ndx:
            ndx_p = int((ndx-1) / 2)
            if self.data[ndx] < self.data[ndx_p]:
                self.data[ndx], self.data[ndx_p] = self.data[ndx_p], self.data[ndx]
                self.shiftup(ndx_p)

    def delete(self):
        if self.__sizeof__() <=0:
            raise Exception('empty')
        item = self.data[0]
        self.data[0] = self.data[-1]
        self.shiftdown(0)
        self.data.pop(-1)
        return item

    def shiftdown(self, ndx):
        left = 2 * ndx + 1
        right = 2 * ndx + 2
        if left < self.count:
            if self.data[left] <= self.data[ndx] and self.data[left] <= self.data[right]:
                self.data[ndx], self.data[left] = self.data[left],  self.data[ndx]
                self.shiftdown(left)
            elif self.data[right] <= self.data[ndx] and self.data[right] <= self.data[left]:
                self.data[ndx], self.data[right] = self.data[right], self.data[ndx]
                self.shiftdown(right)


if __name__ == "__main__":
    minheap = MinHeap()
    data = [1, 3, 4, 5, 2, 5, 6, 4]
    for i in data:
        minheap.insert(i)
