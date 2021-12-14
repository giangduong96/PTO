"""

"""
class LinkedQueue:
    """
    FIFO queue implementation using single linked list
    """
    class _Node:
        """
        Lightweight, NON public class
        """
        __slots__ = "_element", "_next"
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    def __len__(self):
        """ return the length of the linked list"""
        return self._size
    def isEmpty(self):
        """ return True if QUEUE is empty """
        return self._size  == 0
    def first(self):
        """
        return but not remove the element at the front of the queue
        """
        if self.isEmpty():
            raise ("Queue is empty. \n")
        return self._head._element
    def dequeue(self):
        """ remove and return the first element of the queue"""
        if self.isEmpty():
            raise ("Queue is empty. \n")
        else:
            first = self._head._element
            self._head._element = None                  # remove the node
            self._head= self._head._next
            self._size -= 1
        if self.isEmpty():
            # special case when queue is almost empty,
            self._tail = None
        return first
    def enqueue(self, element):
        newest = self._Node(element, None)          # create a new node
        if self.isEmpty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size +=1






