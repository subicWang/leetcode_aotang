# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/8/28: 10:08
"""
from collections import Iterable
import networkx as nx
import matplotlib.pyplot as plt


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self, seq=()):
        assert isinstance(seq, Iterable)
        self.root = None
        self.seq = []

    def _create_balance_binary_tree(self, *args):
        if not args:
            return
        if not self.root:
            self.root = Node(args[0])
            args = args[1:]
        for i in args:
            seed = self.root
            while True:
                if i > seed.val:
                    if not seed.right:
                        node = Node(i)
                        seed.right = node
                        break
                    else:
                        seed = seed.right
                else:
                    if not seed.left:
                        node = Node(i)
                        seed.left = node
                        break
                    else:
                        seed = seed.left

    def level_order(self):
        res = []
        if self.root is None:
            return res
        q = [self.root]
        while len(q):
            r = q.pop(0)
            if r.left:
                q.append(r.left)
            if r.right:
                q.append(r.right)
            res.append(r.value)
        return res

    def first_order(self, root):
        if not root:
            return None
        self.seq.append(root.val)
        self.first_order(root.left)
        self.first_order(root.right)

    def mid_order(self, root):
        if not root:
            return None
        self.mid_order(root.left)
        self.seq.append(root.val)
        self.mid_order(root.right)

    def last_order(self, root):
        if not root:
            return None
        self.last_order(root.left)
        self.last_order(root.right)
        self.seq.append(root.val)

    def create_level_tree(self, *args):
        args = list(args)
        if not args:
            return None
        if not self.root:
            self.root = Node(args[0])
            args = args[1:]
        Nodes = [self.root]
        while len(args) != 0:
            r = Nodes.pop(0)
            if r:
                if r.left is None:
                    node = Node(args.pop(0))
                    r.left = node
                    Nodes.append(node)
                if r.right is None:
                    node = Node(args.pop(0))
                    r.right = node
                    Nodes.append(node)


def create_graph(G, node, pos, x=0, y=0, layer=1):
    pos[node.value] = (x, y)
    if node.left:
        G.add_edge(node.val, node.left.val)
        l_x, l_y = x - 1/2 ** layer, y-1
        l_layer = layer + 1
        create_graph(G, node.left, pos, l_x, l_y, layer=l_layer)
    if node.right:
        G.add_edge(node.val, node.right.val)
        r_x, r_y = x + 1/2 ** layer, y-1
        r_layer = layer + 1
        create_graph(G, node.right, pos, r_x, r_y, layer=r_layer)
    return G, pos


def draw(node):
    graph = nx.DiGraph()
    graph, pos = create_graph(graph, node, pos={})
    fig, ax = plt.subplots(figsize=(8, 8))
    nx.draw_networkx(graph, pos, ax, node_size=500)
    plt.show()


if __name__ == "__main__":
    s = [10, 20, 30, 40, 50]
    tree = BinaryTree()
    tree.create_level_tree(*s)
    draw(tree.root)
    # tree.first_order(tree.root)
    # print(tree.seq)
