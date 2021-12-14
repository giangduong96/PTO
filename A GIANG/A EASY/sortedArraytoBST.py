class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(array):
    if len(array) == 0:
        return None

    return TreeNode(val=array[len(array) // 2],
                    left=sortedArrayToBST(array[:(len(array)) // 2]),
                    right=sortedArrayToBST(array[(len(array) // 2) + 1:]))

def sortedArrary(array):
    if len(array) == 0:
        return None
    return TreeNode(val= array[len(array)//2],
                    left= sortedArrary(array[:(len(array)) //2 ]),
                    right= sortedArrary(array[(len(array))//2 +1:]))



def outputTree(rootTree):
    res = []
    stack = [rootTree]

    while stack:
        first = stack.pop(0)
        if first is not None:
            res.append(first.val)
            stack.append(first.left)
            stack.append(first.right)
        else:
            res.append(None)
    return res


array = [0, 5, 9, 10, 11, 12]
k = sortedArrayToBST(array)
print(k)


print(outputTree(k))


