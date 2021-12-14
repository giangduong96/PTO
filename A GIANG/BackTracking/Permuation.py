"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


# any order, array has no duplicate
# this technique hold the first element and switch 2 others elements
def permute(array):
    result = []
    n = len(array)

    def backtracking(first=0):
        # if all integers are used up
        if first == n:
            result.append(array[:])  # we modified on array itself
        for i in range(first, n):  # beauty in i and range(first)
            # place i-th integer first in the current permutation
            array[first], array[i] = array[i], array[first]
            # use next integer to complete the permutation
            backtracking(first + 1)
            # backtrack
            array[first], array[i] = array[i], array[first]

    backtracking()
    return result


print(permute([1, 2, 3]))

"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
"""
# any order, with duplicate # use Counter for Duplicate element because in counter they dont count duplicate.
# https://leetcode.com/problems/permutations-ii/solution/

from collections import Counter


def permuteUniqe(array):
    result = []

    def backtracking(combination, counter):
        if len(combination) == len(array):
            result.append(list(combination))
            return

        for num in counter:
            if counter[num] > 0:
                # add this number into the current combination
                combination.append(num)
                counter[num] -= 1
                backtracking(combination, counter)
                counter[num] += 1
                combination.pop()

    backtracking([], Counter(array))
    return result
