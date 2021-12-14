"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
"""

"""
brute force: traverse all the linked list and collect the values of the nodes into array
sort and iterate over this array to get the proper value of nodes
create a new sorted list and extend it with the new node
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKList(lists: ListNode):
    node = []
    head = point = ListNode(0)
    for l in lists:
        while l:
            node.append(l.val)
            l = l.next

    for x in sorted(node):
        point.next= ListNode(x)
        point = point.next
    return head.next
