# https://leetcode.com/problems/maximum-depth-of-binary-tree/

root = [3, 9, 20, None, None, 15, 7]


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursive
# Time O(N), space (log N)
def maxDepth(root):
    if root is None:
        return 0
    else:
        left = maxDepth(root.left)
        right = maxDepth(root.right)
        return max(left, right) + 1


# DFS
def maxDepthDFS(root):
    stack = []
    depth = 0

    if root is not None:
        stack.append((1, root))

    while stack:
        currentDepth, root = stack.pop()
        if root is not None:
            depth = max(depth, currentDepth)
            stack.append((currentDepth + 1, root.left))
            stack.append((currentDepth + 1, root.right))

    return depth
