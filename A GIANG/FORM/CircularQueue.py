"""

"""
class CircularQueue:
    class _Node:
        __slots__ = "_next", "_element"
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0
    def __len__(self):
        return self._size
    def isEmpty(self):
        return self._size == 0
    def first(self):
        if self.isEmpty():
            raise ("Empty.")
            head = self._tail._next
        return head._element
    def dequeue(self):
        if self.isEmpty():
            raise ("Empty.")
        old_head = self._tail._next
        # special case when remove one will leave queue empty
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = old_head._next
        self._size -= 1
        return old_head._element
    def enqueue(self, element):
        newNode = self._Node(element, None)
        if self.isEmpty():
            newNode._next = newNode
        else:
            newNode._next = self._tail._next
            self._tail._next = newNode
        self._tail = newNode
        self._size +=1
    def rotate(self):
        if self._size > 0 :
            self._tail = self._tail._next


