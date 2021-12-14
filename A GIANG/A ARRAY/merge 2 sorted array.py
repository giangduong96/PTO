# https://leetcode.com/problems/merge-two-sorted-lists/solution/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# best
# time O(n+m) space O(1)
def mergeSortList(l1, l2):
    head = ListNode(-1)
    # travel node
    prev = head

    while l1 and l2:
        if l1.val < l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next

        prev = prev.next
    # the last elements prob in one of 2 lists
    prev.next = l1 if l1 is not None else l2

    return head.next

# recursive
# time O(n+m) space O(n+m)
def mergeSortedLinkedList(l1, l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = mergeSortedLinkedList(l1.next, l2)
        return l1
    else:
        l2.next - mergeSortedLinkedList(l1, l2.next)
        return l2




def mergeSortedArray(l1, l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    i, j = 0, 0
    result = []
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            result.append([l1[i]])
            i += 1
        else:
            result.append([l2[j]])
            j += 1
    while i < len(l1):
        result.append([l1[i]])
        i += 1
    while j < len(l2):
        result.append([l2[j]])
        j += 1

    return result


print(mergeSortedArray([1, 2, 4], [1, 1, 3]))
