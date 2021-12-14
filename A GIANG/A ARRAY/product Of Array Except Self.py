"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""


# https://leetcode.com/problems/product-of-array-except-self/
# time O(N), space O(N)
def twoArray(array):
    length = len(array)
    left, right, answer = [0] * length, [0] * length, [0] * length
    left[0] = right[length - 1] = 1

    for i in range(1, length):
        left[i] = array[i - 1] * left[i - 1]
        right[length - i - 1] = array[length - i] * right[length - i]
    for i in range(length):
        answer[i] = left[i] * right[i]
    return answer


# time O(N), space O(1)
# do not use array left and right
def twoArray2(array):
    length = len(array)
    answer = [0] * length

    answer[0] = 1
    for i in range(1, length):
        answer[i] = array[i - 1] * answer[i - 1]
    R = 1
    for i in range(1, length+1):
        answer[length - i] = answer[length - i] * R
        # R nhan tung value mot
        R *= array[length - i]

    return answer


print(twoArray2([1, 2, 3, 4]))
