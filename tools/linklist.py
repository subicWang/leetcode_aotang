# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/9/20: 21:47
"""

class Node(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insertToFront(self, data):
        if data is None:
            return None
        new_node = Node(data, self.head)
        self.head = new_node
        return new_node

    def append(self, data):
        if data is None:
            return None
        node = Node(data)
        if self.head is None:
            self.head = node
            return node
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = node
        return self.head

    def find(self, data):
        if data is None:
            return None
        cur_node = self.head
        while cur_node.next:
            if cur_node.val == data:
                return cur_node
            cur_node = cur_node.next
        return None

    def delete(self, data):
        if data is None:
            return None
        if self.head is None:
            return None
        if self.head.val == data:
            self.head = self.head.next
            return self.head
        pre_node = self.head
        cur_node = self.head.next
        while cur_node:
            if cur_node.val == data:
                pre_node.next = cur_node.next
                return self.head
            else:
                pre_node = cur_node
                cur_node = cur_node.next
        return self.head

    def printLinkList(self, node):
        while node:
            print(node.val, "->")
            node = node.next

