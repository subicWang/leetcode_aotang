# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/10/24: 9:24
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from tools.linklist import LinkedList
class Solution(object):
    def printLinkList(self, node):
        while node:
            print(node.val, "->")
            node = node.next
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        空间复杂度不满足O(1)
        执行用时 :64 ms, 在所有 python 提交中击败了93.87%的用户
        内存消耗 :31 MB, 在所有 python 提交中击败了16.28%的用户
        """
        if head is None or head.next is None:
            return True
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]

    def isPalindrome1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        该题中是链表回文，和其他字符串回文不同，字符串回文可以通过坐标直接访问，而链表只能从头开始遍历。
        不用全局比较整个链表，只需前半个链表和后半个链表相等就是回文。
        如何找到前后两个半链表呢？首先得找到链表中点，由于链表特性无法直接获取链表中点，需要使用快慢指针来找到链表中点。
        找到中点后将后半段链表反转后，就可以对前后半段链表进行比较了。
        执行用时 :52 ms, 在所有 python 提交中击败了99.80%的用户
        内存消耗 :30.8 MB, 在所有 python 提交中击败了36.99%的用户
        """
        # 快慢指针找中点
        if head is None or head.next is None:
            return True
        fast = slow =head
        while fast.next:
            slow = slow.next
            if fast.next.next:
                fast = fast.next.next
            else:
                break
        last = None
        while slow:
            tmp = slow.next
            slow.next = last
            last = slow
            slow = tmp
        # self.printLinkList(last)
        while last:
            if head.val != last.val:
                return False
            head = head.next
            last = last.next
        return True


if __name__ == '__main__':
    Input = [1, 2, 2, 1]
    # Output: false
    linklist = LinkedList()
    for i in range(len(Input)):
        # Head = linklist.insertToFront(Input[i])
        Head = linklist.append(Input[i])
    # linklist.printLinkList(Head)
    solver = Solution()
    r = solver.isPalindrome1(Head)
    print(r)
