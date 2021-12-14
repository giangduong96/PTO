class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# pre order always choose left middle node as root
def sortedArrayToBinaryTree(array):
    def helper(left, right):
        if left > right:
            return None
        # always choose left middle node as root
        p = (left + right) // 2
        # pre order traversal: node -> left -> right
        root = TreeNode(array[p])
        root.left = helper(left, p - 1)
        root.right = helper(p + 1, right)
        return root

    return helper(0, len(array) - 1)


# print(sortedArrayToBinaryTree([-10, -3, 0, 5, 9]))


# cach 2 insert from pre order array to binary
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertLevelOrder(arr, root, i, n):
    if i < n:
        root = TreeNode(arr[i])
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)
        root.right = insertLevelOrder(arr, root.left, 2 * i + 2, n)
    return root


def inOder(root):
    if root is not None:
        inOder(root.left)
        print(root.val, end=" ")
        inOder(root.right)


arr = [1, 2, 3, 4, 5, 6, 6, 6, 6]
n = len(arr)
root = None
root = insertLevelOrder(arr, root, 0, n)
inOder(root)
