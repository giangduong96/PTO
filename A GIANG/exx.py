def findPairs( a, b, target):
    a.sort(key=lambda x: x[1])
    b.sort(key=lambda x: x[1])
    l, r = 0, len(b) - 1
    ans = []
    curDiff = float('inf')
    while l < len(a) and r >= 0:
        id1, i = a[l]
        id2, j = b[r]
        if (target - i - j == curDiff):
            ans.append([id1, id2])
        elif (i + j <= target and target - i - j < curDiff):
            ans.clear()
            ans.append([id1, id2])
            curDiff = target - i - j
        if (target > i + j):
            l += 1
        else:
            r -= 1
    return ans

print(findPairs([[1,2], [2,4], [3,6]], [[1,2]], 7))