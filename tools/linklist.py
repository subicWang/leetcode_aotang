# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/9/20: 21:47
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkList:
    def __init__(self, node):
        self.head = node

    def add(self, data):
        node = ListNode(data)
        self.head = node
        return node


    # def _reverse(self, nodelist):
    #     list = []
    #     while nodelist:
    #         list.append(nodelist.val)
    #         nodelist = nodelist.next
    #     result = Node(list[0])
    #     linkhandle = LinkList()
    #     for i in list[1:]:
    #         result = linkhandle.add(i)
    #     return result

    def printLinkList(self, node):
        while node:
            print(node.val, "->")
            node = node.next

