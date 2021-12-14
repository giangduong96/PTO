# https://leetcode.com/problems/same-tree/
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
def sameTree(tree1, tree2):
    def check(tree1, tree2):
        # if both are None
        if not tree1 and not tree2:
            return True
        # one tree has None
        if not tree1 or not tree2:
            return False
        if tree1.val != tree2.val:
            return False
        return True

    deq = deque([tree1, tree2])
    while deq:
        tree1, tree2 = deq.popleft()
        if not check(tree1, tree2):
            return False

        if tree1:
            deq.append((tree1.left, tree2.left))
            deq.append((tree1.right, tree2.right))
    return True

