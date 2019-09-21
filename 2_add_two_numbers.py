# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/9/20: 21:39
"""
from tools.linklist import ListNode, LinkList

class LinkList1:
    def __init__(self):
        self.head = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = LinkList1()
        i = 0
        L = []
        while l1 or l2 or i:
            l1val = 0
            l2val = 0
            if l1:
                l1val = l1.val
            if l2:
                l2val = l2.val
            j = (l1val + l2val + i) % 10
            L.append(j)
            i = (l1val + l2val + i) // 10
            if l1:
                l1 = l1.next
            else:
                l1 = None
            if l2:
                l2 = l2.next
            else:
                l2 = None
        for i in range(len(L)-1, -1, -1):
            node = ListNode(L[i])
            if l.head:
                node.next = l.head
                l.head = node
            else:
                l.head = node

        return l.head

if __name__ == "__main__":
    l1 = [5]
    l2 = [5]
    LL = LinkList(ListNode(l1[0]))
    for i in l1[1:]:
        LL.add(i)
    L1 = LL.head
    LL = LinkList(ListNode(l2[0]))
    for i in l2[1:]:
        LL.add(i)
    L2 = LL.head
    s = Solution()
    r = s.addTwoNumbers(L1, L2)
    print(LL.printLinkList(r))

