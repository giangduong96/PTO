"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= first < second <= numbers.length.

Return the indices of the two numbers, index1 and index2, as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

"""

# 2 pointer
# time O(n) Space O(1)
def twoSum(array, target):
    low, high = 0, len(array) - 1
    while low < high:
        s = array[low]+ array[high]
        if s > target:
            high -= 1
        elif s < target:
            low += 1
        else:
            return [array[low], array[high]]
    # if cannot find
    return -1


# 1 pass hash table
# time O(n), space O(1)
def twoSum2(array, target):
    for i in range(len(array)):
        complement = target - array[i]
        if complement in array:
            return [array[i], complement]
    # if cannot find
    return -1

print(twoSum2([2, 5, 6, 7],11))

