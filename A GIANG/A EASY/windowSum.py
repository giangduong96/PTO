"""
Given an array of integers of size ‘n’.
Our aim is to calculate the maximum sum of ‘k’
consecutive elements in the array.

Input  : arr[] = {100, 200, 300, 400}
         k = 2
Output : 700
"""


# O^2N
def windowSum1(array, consecutive_element):
    maxSum = 0
    length = len(array)

    for start in range(length - consecutive_element + 1):
        currentSum = 0
        for element in range(consecutive_element):
            currentSum = currentSum + array[start + element]
        maxSum = max(currentSum, maxSum)

    return maxSum


# O (n*k), better using slice window
def window2(array, consecutive):
    maxSum = 0
    length = len(array)
    if length < consecutive:
        raise Exception("Invalid")
        return -1

    window = sum(array[:consecutive])
    maxSum = window

    for start in array(length-consecutive):
        window = window - array[start] + array[start + consecutive]
        maxSum = max(window, maxSum)
    return maxSum



array = [100, 200, 300, 400]
print(windowSum1(array, 2))
