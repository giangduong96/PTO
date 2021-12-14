
# return position of target in array list
def binarySearch(array, target):
    left, right = 0 , len(array) - 1
    while left <= right:
        pivot = (right - left) // 2
        if array[pivot] == target:
            return pivot

        if array[pivot] < target:
            left = pivot + 1
        else:
            right = pivot - 1
    # cannot find
    return -1
