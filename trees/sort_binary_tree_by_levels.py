# code: utf-8


class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node):
    if node is None:
        return []

    top_level = []
    top_level.append(node)

    out = []

    def cut_head(top_level):
        if top_level == []:
            return
        next_top_level = []
        for n in top_level:
            out.append(n.value)
            if n.left is not None:
                next_top_level.append(n.left)
            if n.right is not None:
                next_top_level.append(n.right)
        print(out)
        cut_head(next_top_level)

    cut_head(top_level)

    return out


t1 = None

t2 = Node(Node(None, Node(None, None, 4), 2), Node(
    Node(None, None, 5), Node(None, None, 6), 3), 1)

tree_by_levels(t2)
