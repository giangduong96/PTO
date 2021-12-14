def FloydCycle(graph):
    pass


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def FloyCycle(head):
    hare = tortoise = head

    while hare and hare.next:
        hare = hare.next.next       # 2 steps
        tortoise = tortoise.next    # 1 step
        if hare == tortoise:
            return True
    return False