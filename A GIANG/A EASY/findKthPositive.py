"""Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
"""


def findKthSolution(array, k):
    # if Kth missing is less than arr[0]
    if k < array[0] - 1:
        return k

    # decrease k by the number of positive integer which are missing before the array starts
    k -= array[0] - 1
