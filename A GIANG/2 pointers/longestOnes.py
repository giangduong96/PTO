def longestOnewithoutK(array):
    count = maxcount = 0
    for num in array:
        if num == 1:
            count += 1
        else:
            maxcount = max(count, maxcount)
            count = 0
    return maxcount


# print(longestOnewithoutK([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]))


"""
Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

Input: nums = [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the maximum number of consecutive 1s. After flipping, the maximum number of consecutive 1s is 4.
"""


# flip at most 1 time
# Time O(n) space O(1)
def longestOneFlipOne(array):
    left, right = 0, 0
    longest = 0
    numzero = 0

    # while our window is in bound
    while right < len(array):
        # add the right most element in our window
        if array[right] == 0:
            numzero += 1

        # if our window is invalid, contract our window
        while numzero == 2:
            if array[left] == 0:
                numzero -= 1
            left += 1

        longest = max(longest, right - left + 1)  # update longest sequence answer
        right += 1

    return longest


nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
# print(longestOneFlipOne(nums))

# same as above
def longestOnes(A, K):
    i = 0
    for j in range(len(A)):
        K -= 1 - A[j]
        # print(i, j, K)
        if K < 0:
            K += 1 - A[i]
            i += 1
    return j - i + 1


print(longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
