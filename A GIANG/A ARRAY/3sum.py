"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""


# time: O(n^2) Space: O(n)
# sort array take O(n log n), two sum is O(n) but we call n time ==> O(n^2)
def threeSum1(arr):
    result = []
    arr.sort()

    for index in range(len(arr)):
        # condition a + b + c == 0
        if arr[index] > 0:
            break
        if index == 0 or arr[index - 1] != arr[index]: # first element and check duplicate element
            twoSum1(arr, index, result)
    return result


def twoSum1(arr, index, result):
    low, high = index + 1, len(arr) - 1
    while low < high:
        sum = arr[index] + arr[low] + arr[high]
        if sum < 0:
            low += 1
        elif sum > 0:
            high -= 1
        else:
            result.append([arr[index], arr[low], arr[high]])
            low += 1
            high -= 1
            # check if there any duplicate value in front, note: arr[low] da dc +1
            while low < high and arr[low] == arr[low - 1]:
                low += 1


# hashset
def threeSum2(array):
    result = []
    array.sort()

    for i in range(len(array)):
        if array[i] > 0:
            break
        if i == 0 or array[i - 1] != array[i]:
            twoSum2(array, i, result)
    return result


def twoSum2(array, i, result):
    seen = set()
    j = i + 1
    while j < len(array):
        complement = array[i] + array[j]
        if complement in seen:
            result.append([array[i], array[j], complement])
            while j + 1 < len(array) and array[j] == array[j + 1]:
                j += 1
        seen.add(-array[j])
        j += 1


print(threeSum2([-1, 0, 1, 2, -1, -4]))
