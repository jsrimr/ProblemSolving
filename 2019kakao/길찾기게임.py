import sys
sys.setrecursionlimit(10**6)
class Tree:
    def __init__(self, val, left, right):
        self.root = val
        self.left = left
        self.right = right


def solution(nodeinfo):
    def makeTree(num_list):
        if not num_list:
            return Tree(None, None,None)
        left_list = []
        right_list = []
        root = num_list.pop(0)
        for node in num_list: #node = (x,y,idx)
            if node[0] < root[0]:
                left_list.append(node)
            else:
                right_list.append(node)

        return Tree(root[2], makeTree(left_list), makeTree(right_list))

    for i, node in enumerate(nodeinfo):
        node.append(i+1)

    nodeinfo = sorted(nodeinfo, key=lambda x: x[1], reverse=True)
    tree = makeTree(nodeinfo)

    pre = []
    post = []
    def preorder(tree):
        if tree.root:
            pre.append(tree.root)
            preorder(tree.left)
            preorder(tree.right)

    def postorder(tree):
        if tree.root:
            postorder(tree.left)
            postorder(tree.right)
            post.append(tree.root)

    preorder(tree)
    postorder(tree)

    return [pre, post]

if __name__ == '__main__':
    nodeinfo = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
    print(solution(nodeinfo))