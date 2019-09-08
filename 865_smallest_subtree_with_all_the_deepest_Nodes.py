# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/8/29: 14:57
"""
from tools.binarytree import BinaryTree, draw


class Solution(object):
    def __init__(self):
        pass

    def subtreeWithAllDeepest(self, root):
        # 返回所有子树和其根节点的深度
        def sub(root):
            if root is None or root.value is None:
                # print(root, 0)
                return [root, 0]
            left_list = sub(root.left)
            right_list = sub(root.right)
            if left_list[1] == right_list[1]:
                # print(root.value, left_list[1]+1)
                return [root, left_list[1] + 1]
            elif left_list[1] < right_list[1]:
                # print(root.value, right_list[1]+1)
                return [right_list[0], right_list[1] + 1]
            else:
                # print(root.value, left_list[1] + 1)
                return [left_list[0], left_list[1] + 1]
        list = sub(root)
        return list[0]

    def subtreeWithAllDeepest1(self, root):
        res = [[root]]
        index = []
        q = [[root]]
        index = []
        while len(q) > 0 and len(q[0]) > 0:
            p = q.pop(0)
            t = []
            ind = []
            while len(p):
                r = p.pop(0)
                if r.left:
                    t.append(r.left)
                    ind.append(r.left.value)
                else:
                    ind.append(None)
                if r.right:
                    t.append(r.right)
                    ind.append(r.right.value)
                else:
                    ind.append(None)
            res.append(t)
            q.append(t)
            index.append(ind)

        return res, index

if __name__ == "__main__":
    s = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    tree = BinaryTree()
    tree.create_level_tree(*s)
    # draw(tree.root)
    print(tree.level_order())
    solver = Solution()
    res, index = solver.subtreeWithAllDeepest1(tree.root)
    # draw(res)