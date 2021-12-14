# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowest(root, p , q):
    parent_val = root.val
    p_val = p.val
    q_val = q.val

    # if both p and q are greater than parent
    if p_val > parent_val and q_val > parent_val:
        return lowest(root.right, p,q)
    # if both p and q are less than parent
    if p_val < parent_val and q_val < parent_val:
        return lowest(root.left, p, q)
    else:
        return root