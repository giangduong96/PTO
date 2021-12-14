# https://leetcode.com/problems/invert-binary-tree/
import collections
from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive
# time O(N) Space O(N)
def invertBinaryTree(root):
    if root is None:
        return None

    if root:
        root.left, root.right = invertBinaryTree(root.right), invertBinaryTree(root.left)

    return root

# BFS
# Time O(N), Space O(N)
def invertBinaryDFS(root):
    queue = collections.deque([root])

    while queue:
        node = queue.popleft()
        if node:
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)
    return root


def DFS(root):
    stack = [root]

    while stack:
        node = stack.pop()
        if node:
            node.right, node.left = node.left, node.right
            stack.append(node.right)
            stack.append(node.left)
    return root
