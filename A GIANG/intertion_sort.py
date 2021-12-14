"""
Best    O(n)
Worst   O(n^2)
Space   O(1)
Stable  Yes
"""
def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i -1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(arr)


"""
Best    O(n log(n))
Worst   O(n log(n))
Space   O(n)
Stable  Yes
"""
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2      # find the middle of the array
        left = arr[:mid]        # left array
        right = arr[mid:]       # right array

        mergeSort(left)         # sort the left array
        mergeSort(right)        # sort the right array

        i, j,k = 0, 0, 0

        # copy data to temp array left[] and R[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # check if any element left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def heapify(arr, n, i ):
    """
    :param n: size of array
    :param i: largest position
    """
    largest = i             # initial the largest as root

    if len(arr) > 1:
        left = 2*i + 1      # left position
        right = 2*i + 2     # right position

    # if exists left and left is greater than larger then larger = left
    if left < n and arr[i] < arr[left]:
        largest= left

    # if exists right and right is greater than larger then larger= right
    if right < n and arr[largest] < arr[right]:
        largest = right
    # if needs, swap larger with correct position
    if i != largest:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


"""
Best    O(n log(n))
Worst   O(n log(n))
Space   O(1)
Stable  No Stable means if the two elements have the same key, 
they remain in the same order or positions. But that is not the case for Heap sort.
"""
def heap_sort(arr):
    n = len(arr)

    # building the max heap first
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)

    # one by one exact elements
    for i in range(n -1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


def partition(arr, low, high):
    i = low -1              # index of smaller element
    pivot = arr[high]       # pivot

    for j in range(low, high):
        # if current element is smaller than the pivot
        if arr[j] < pivot:

            # increase index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high]= arr[high], arr[i+1]
    return (i+1) # because we done with i, so the next should be i +1



"""
Best    O(n log(n))
Worst   O(n^2)
Space   O(n)
Stable  No
"""
def quickSort(arr, low, high):
    if low< high:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi +1, high)

# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-10.php
def counting_sort(array1, max_val):
    m = max_val + 1
    count = [0] * m

    for a in array1:
        # count occurences
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            array1[i] = a
            i += 1

    """
    OR WE CAN DO
    i = 0 
    for a in range(m):
        buck = count[a]
        for c in buck:
            arr[i] = a
            i+=1
    
    """
    return array1

"""
Best    O(n k)
Worst   O(n ^2)
Space   O(n + k)
Stable  Yes
"""
def radix_sort(nums):
    RADIX = 10
    placement = 1
    max_digit = max(nums)

    while placement < max_digit:
      buckets = [list() for _ in range( RADIX )]
      for i in nums:
        tmp = int((i / placement) % RADIX)
        buckets[tmp].append(i)
      a = 0
      for b in range( RADIX ):
        buck = buckets[b]
        for i in buck:
          nums[a] = i
          a += 1
      placement *= RADIX
    return nums

"""
    array so thap phan su dung
Best    O(n + k)
Worst   O(n + k)
Space   O(n^2)
Stable  Yes
"""
def bucketsort(arr):
    # create a bucket
    bucket = []
    # create empty buckets
    for i in range(len(arr)):
        bucket.append([])

    # insert elements into their respective buckets
    for j in arr:
        index_b = int(j /10)
        bucket[index_b].append(j)

    # sort the elements of each bucket
    for i in range(len(arr)):
        bucket[i] = sorted(bucket[i])

    k = 0
    for i in range(len(arr)):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
    return arr






if __name__ == '__main__':
    arr = [4,10,3,5,1]
    so_thap_phan = [0.1, 0.42, 0.4244, 0.5, 0.55, 0.875, 0.9823]
    n = len(arr)

    #insertion(arr)             #stable
    mergeSort(arr)             #stable
    # print(heap_sort(arr))          # not stable
    #quickSort(arr, 0, n -1)     # not stable


    #counting_sort(arr, max(arr))   #stable
    #radix_sort(arr)                #stable
    #bucketsort(so_thap_phan)       #stable

    print(so_thap_phan)

# search 1 element not SORT
def binary_search_recursive(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search_recursive(array, element, start, mid-1)
    else:
        return binary_search_recursive(array, element, mid+1, end)