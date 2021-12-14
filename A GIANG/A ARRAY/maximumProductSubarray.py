"""Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a CONTIGUOUS / ke tiep subsequence of the array.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6."""
# same as max subarray
def maxProductSubarray(array):
    currentProduct = maxProduct = array[0]

    for num in array[1:]:
        currentProduct = max(num, currentProduct * num)
        maxProduct = max(currentProduct, maxProduct)
    return maxProduct

print(maxProductSubarray([2,3,-2, 4]))