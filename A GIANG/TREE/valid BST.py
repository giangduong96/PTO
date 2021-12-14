# https://leetcode.com/problems/validate-binary-search-tree/
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive
# O(N) and O(N)
def validBST(root):
    def validate(root, low= -math.inf, high= math.inf):
        if root is None:
            return True

        if root <= low or root >= high:
            return False

        return (validate(root.right, root.val, high) and validate(root.left, root.val, low))
    return validate(root)

def validBST_Range(root):
    if not root:
        return True

    stack = [(root, -math.inf, math.inf)]

    while stack:
        root, low, high = stack.pop()
        if not root:
            continue

        val = root.val
        if val <= low or val >= high:
            return False
        stack.append((root.right, val, high))
        stack.append((root.left, low, val))

    return True

