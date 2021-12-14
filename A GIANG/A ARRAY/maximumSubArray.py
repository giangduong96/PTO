"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""


def maximumSubArray(array):
    # init our variable using the first element
    currrent_subarray = maxSubArray = array[0]
    #Initialize 2 integer variables. Set both of them equal to the first value in the array.

    # currentSubarray will keep the running count of the current subarray we are focusing on.
    # maxSubarray will be our final return value. Continuously update it whenever we find a bigger subarray.
    for num in array[1:]:
        # Iterate through the array, starting with the 2nd element (as we used the first element to initialize
        # our variables). For each number, add it to the currentSubarray we are building.
        # If currentSubarray becomes negative, we know it isn't worth keeping, so throw it away.
        # Remember to update maxSubarray every time we find a new maximum.
        currrent_subarray = max(num, currrent_subarray + num)
        maxSubArray = max(maxSubArray, currrent_subarray)
        # print(currrent_subarray, maxSubArray)
    return maxSubArray


print(maximumSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

