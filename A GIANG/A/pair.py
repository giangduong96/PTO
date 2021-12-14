def numberPairInList(n, array):
    pair = 0
    newArray = []
    for i in array:
        if i not in newArray:
            newArray.append()
        else:
            newArray.remove(i)
            pair += 1
    return pair