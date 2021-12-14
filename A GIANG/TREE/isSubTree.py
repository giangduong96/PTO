# https://leetcode.com/problems/subtree-of-another-tree/

# dfs
def isSubTree(tree1, tree2):
    def dfs(tree1, tree2):
        # if 2 trees are same
        if not tree1 and not tree2: return True
        # if one of them are None
        if not tree1 or not tree2: return False
        # recursive check the value
        return tree1.val == tree2.val and dfs(tree1.left, tree2.left) and dfs(tree1.right, tree2.right)

    stack = [tree1]
    while stack:
        node = stack.pop()
        if node.val == tree2.val and dfs(node, tree2):
            return True

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return False

# recursive
def isSubTree2(tree1, tree2):
    def dfs(tree1, tree2):
        if not tree1 and not tree2: return True
        if not tree1 or not tree2: return False
        return  tree1.val == tree2.val and dfs(tree1.left, tree2.left) and dfs(tree1.right, tree2.right)

    if not tree1: return False
    if tree1.val == tree2.val and dfs(tree1, tree2): return True

    return isSubTree2(tree1.left, tree2) or isSubTree(tree1.right, tree2) # quan trong khuc nay

