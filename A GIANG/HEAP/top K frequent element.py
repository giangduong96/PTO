"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""
# use Counter and heapq
import random
from collections import Counter
import heapq


# with heap and counter
# time O(N log K) Space: O(N+ k)
def topKFrequent(array, k):
    # best case O(1)
    if k == len(array):
        return array

    # O(N) time
    count = Counter(array)

    return heapq.nlargest(k, count.keys(), key=count.get())


# with counter
def topKFrequent1(array, k):
    if k == len(array):
        return array

    counter = Counter(array)
    heap = [(c, counter[c]) for c in counter]
    heapq.heapify(heap)
    ans = []
    for i in range(len(counter) + 1):
        if k == 0:
            return ans
        ans.append(heap[i][0])
        k -= 1


# quick select
# time: O(N), space O(N)
def topKFrequentWithQuickSelect(array, k):
    counter = Counter(array)
    unique = list(counter.keys())

    def partition(left, right, pivot_index):
        pivot_freq = counter[unique[pivot_index]]

        # move pivot to the end
        unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

        # move all less freq element to the left
        store_index = left
        for i in range(left, right):
            if counter[unique[i]] < pivot_freq:
                unique[store_index], unique[i] = unique[i], unique[store_index]
                store_index += 1

        # move pivot in it final place
        unique[right], unique[store_index] = unique[store_index], unique[right]
        return store_index

    def quickselect(left, right, k):
        # base case if list contains only 1 element
        if left == right:
            return

        # select random pivot index
        pivot_index = random.randint(left, right)

        # find the pivot position in sorted list
        pivot_index = partition(left, right, pivot_index)

        # if the pivot is in its final sorted position
        if k == pivot_index:
            return
        # go left
        elif k < pivot_index:
            quickselect(left, pivot_index-1, k)
        # go right
        else:
            quickselect(pivot_index +1, right, k)
    n = len(unique)

    quickselect(0, n-1, n-k)

    return unique[n-k:]





array = [1, 1, 1, 2, 2, 3]
k = 3
print(topKFrequentWithQuickSelect(array, k))
