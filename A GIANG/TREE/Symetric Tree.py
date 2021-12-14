# https://leetcode.com/problems/symmetric-tree/description/
import collections


def isSymmetric(root):
    queue = collections.deque([(root, root)])

    while queue:
        node1, node2 = queue.popleft()
        if not node1 and not node2: return True
        if not node1 or not node2: return False
        if node1.val != node2.val: return False
        
        # quan trong o day
        queue.append(node1.left, node2.right)
        queue.append(node1.right, node2.left)

    return True
