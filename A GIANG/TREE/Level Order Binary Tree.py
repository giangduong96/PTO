# https://leetcode.com/problems/binary-tree-level-order-traversal/
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursive
def levelOrder(root):
    levels = []
    if not root:
        return levels

    def helper(node, level):
        # start a new current level
        if len(levels) == level:
            levels.append([])
        # append current node value in same level
        levels[level].append(node.val)
        # process child node for the next level
        if node.left:
            helper(node.left, level + 1)
        if node.right:
            helper(node.right, level + 1)

    helper(root, 0)
    return levels

# BFS
# time O(N) Space O(N)
def levelBFS(root):
    levels = []
    if not root:
        return []

    level = 0
    queue = collections.deque([root])

    while queue:
        # start the current level
        levels.append([])
        # number of element in the current level
        level_length = len(queue)

        for i in range(level_length):
            node = queue.popleft()
            # fulfill the current level
            levels[level].append(node.val)
            # add child node to current level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1
    return levels

