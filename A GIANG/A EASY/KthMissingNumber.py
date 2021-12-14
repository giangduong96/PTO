"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.



Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
"""


# best
def kthMissingNumber1(array, k):
    i = 1
    j = 0
    ans = 0
    n = len(array)
    while True:
        if j == n:
            break
        if i == array[j]:
            j += 1
        else:
            ans += 1
            if ans == k:
                return i # for normal case
        i += 1
    return (i - 1) + (k - ans) # for the edge case


# better
def kthMissingNumber(array, k):
    outset = set(range(0, max(array) + k + 2))
    return sorted(list(outset.difference(set(array))))[k - 1]


# range from 0 to last element of array + k +2
def findKthPositive(arr, k):
    full = [x for x in range(0, arr[-1] + 1 + k + 2)]
    print(full)
    for i in arr:
        if i in full:
            print(i)
            full.remove(i)
    print(full)
    return full[k]


arr = [2, 3, 4, 7, 11]

k = 5
print(kthMissingNumber1(arr, k))
print(len(arr))
# arr2 = [1,2,3,4,5,6]
# k1 = 2
# print(kthMissingNumber1(arr2, k1))
