"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines
 are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the
 x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
"""


# 2 pointer approaching
# time O(n) Space O(1)

def maxContainer(array):
    left = 0
    right = len(array) - 1
    area = 0

    while left != right:

        long = right - left
        high = min(array[right], array[left])
        area = max(long * high, area)

        if array[left] < array[right]:
            left += 1
        else:
            right -= 1
    return area


print(maxContainer([1, 8, 6, 2, 5, 4, 8, 3, 7]))
