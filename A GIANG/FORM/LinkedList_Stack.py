"""
"""
class LinkedStack:
    """
    LIFO Stack implementation using a single linked list for storage
    """
    # nested class
    class _Node:
        """
        Why we use nested class
        lightweight, NON PUBLIC class
        """
        # create static amount of memory at object creation to store all attributes
        __slots__ = '_element', '_next'
        def __init__(self, element, next):     # initialize node's fields
            self._element = element             # reference to user's element
            self._next = next                   # reference to next node

    def __init__(self):
        """ Create an empty stack   """
        self._head = None                       # reference to the head node
        self._size = 0                          # number of stack element

    def __len__(self):
        """ return the number of elements in the stack """
        return self._size

    def isEmpty(self):
        """ return True if the stack is empty """
        return self._size == 0

    def push(self, elements):
        """ add element to the top of the stack """
        self._head = self._Node(elements, self._head)
        self._size += 1

    def top(self):
        """ return but do not remove the element at the top of the stack """
        if self.isEmpty():
            raise (" Stack is empty\n")
        return self._head._element
    def pop(self):
        """ remove and return the element from the top of the stack """
        if self.isEmpty():
            raise ("Stack is empty.\n")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer



