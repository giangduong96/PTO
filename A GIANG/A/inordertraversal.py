class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# brute force
res = []


def inorderTraversal(root, res):
    if root:
        if root.left:
            inorderTraversal(root.left, res)

            res.append(root.val)

        if root.right:
            inorderTraversal(root.right, res)
    return res


# use stack
def inorderTraversal2(root):
    res = []
    stack = []
    current = root
    while stack or current is not None:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        res.append(current.val)
        current = current.right
    return res


# morris traversal
def inorderTraversal3(root):
    res = []
    current = root

    while (current is not None):
        if (current.left == None):
            res.append(current.val)
            current = current.right  # move to the right node
        else:  # has a left subtree
            pre = current.left
            while pre.right is not None:  # find the right most
                pre = pre.right
            pre.right = current  # put current after the pre node
            temp = current  # store current node
            current = current.left  # move current to the top of the new tree, khó ở chổ này nè, current left still there in current
            temp.left = None  # original current left be null, avoid infinity loops
    return res
