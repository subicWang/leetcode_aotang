# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/10/28: 9:26
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tools.binarytree import BinaryTree


class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        这是二叉树的问题，应先想到递归。判断条件：当前点如果在to_delete里，则返回none。如果父节点在to_delete里且当前节点不在则将
        当前节点增加到返回列表里。
        Runtime: 40 ms, faster than 98.67% of Python online submissions for Delete Nodes And Return Forest.
        Memory Usage: 12.2 MB, less than 100.00% of Python online submissions for Delete Nodes And Return Forest.
        # TODO: 好好理解
        """
        if root is None or len(to_delete) == 0:
            return root
        to_delete = set(to_delete)
        res = []
        def pre_order(root, flag):
            if root:
                if root.val not in to_delete and flag:
                    res.append(root)
                root.left = pre_order(root.left, root.val in to_delete)
                root.right = pre_order(root.right, root.val in to_delete)
                return None if root.val in to_delete else root
        pre_order(root, True)
        return res


def print_level_bt(root):
    res = []
    if root is None:
        return None
    q = [root]
    while len(q):
        r = q.pop(0)
        if r.left:
            q.append(r.left)
        if r.right:
            q.append(r.right)
        res.append(r.val)
    return res




if __name__ == '__main__':
    solver = Solution()
    root = [1, 2, 3, 4, 5, 6, 7]
    to_delete = [3, 5]
    bt = BinaryTree()
    bt.create_level_tree(*root)
    res = solver.delNodes(bt.root, to_delete)
    for r in res:
        print(print_level_bt(r))


