def binary_search(data, target, low, high):
    "return True if target is found in indicated portion of Python list "

    "The search only consider the portion from data[low] to data[high] inclusive"

    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid -1 )
        else:
            return binary_search(data, target, mid +1, high)

if __name__ == '__main__':
    arr = [0 + i for i in range(1,100, 4)]
    print(arr)
    print(binary_search(arr, 5, 0, len(arr) +1))