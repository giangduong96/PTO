"""
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9].
8 is the missing number in the range since it does not appear in nums.
"""


# Gauss Formula
# (n * (n+1) ) //2 == 0 +1 +....n
def missingNumber(array):
    n = len(array)
    gauss = (n * (n + 1)) // 2
    return gauss - sum(array)


print(missingNumber([0, 1, 2, 4, 5, 6, 7]))
