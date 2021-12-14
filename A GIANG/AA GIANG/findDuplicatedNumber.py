"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.



Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
"""


# same as entrance of the circle
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# https://leetcode.com/problems/linked-list-cycle-ii/solution/
def FloydCycle(head):
    if head is None:
        return None

    def getIntersect(head):
        hare = tortoise = head

        while hare is not None and hare.next is not None:
            hare = hare.next.next
            tortoise = tortoise.next
            if tortoise == hare:
                return tortoise  # return the intersection
        return None

    intersect = getIntersect(head)

    ptr1 = head
    ptr2 = intersect
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return ptr1
# T: O(N), S:O(1)
