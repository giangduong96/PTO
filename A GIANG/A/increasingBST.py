# Definition for a binary tree node.
"""
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree
is now the root of the tree, and every node has no left child and only one right child.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def increasingBST(root):
    # Definition for a binary tree node.
    def inorder(node):
        # if node.left != None:
        #     for v in self.inorder_gen(node.left):
        #         yield v
        # yield node.val
        # if node.right != None:
        #     for v in self.inorder_gen(node.right):
        #         yield v
        if node:
            yield from inorder(node.left)
            yield node.val
            yield from inorder(node.right)

    ans = cur = TreeNode(None)
    for v in inorder(root):
        cur.right = TreeNode(v)
        cur = cur.right
    return ans.right


def increase(root):
    def inorder(node):
        yield from inorder(node.left)
        yield node.val
        yield from inorder(node.right)

    ans = cur = TreeNode(None)
    for v in inorder(root):
        cur.right = TreeNode(v)
        cur = cur.right