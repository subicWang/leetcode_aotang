# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/8/28: 9:40
"""
from tools.binarytree import BinaryTree, draw


class Solution(object):
    def __init__(self):
        pass

    def convertBST(self, root):
        Sum = 0

        def inorder(root, Sum):
            if root:
                Sum = inorder(root.left, Sum)
                Sum += root.value
                Sum = inorder(root.right, Sum)
            return Sum
        Sum = inorder(root, Sum)

        def inorder_create(root, Sum):
            if root:
                Sum = inorder_create(root.left, Sum)
                temp = root.value
                root.value = Sum
                Sum -= temp
                print(root.value)
                print(Sum)
                Sum = inorder_create(root.right, Sum)
            return Sum
        inorder_create(root, Sum)

        return root


if __name__ == "__main__":
    s = [5, 2, 13]
    tree = BinaryTree()
    tree.create_level_tree(*s)
    # draw(tree.root)
    solver = Solution()
    draw(solver.convertBST(tree.root))