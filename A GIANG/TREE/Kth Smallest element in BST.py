# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# inOrder
# O(N) O(N)
def KthSmallestinBST(root, k):
    result = []
    def inOrder(root):
        if root:
            inOrder(root.left)
            result.append(root.val)
            inOrder(root.right)
    inOrder(root)
    return result[k-1]

# optima by using LRU cache