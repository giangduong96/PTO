"""
enqueue             O(1)
dequeue             O(1)
first               O(1)
isempty             O(1)
lent                O(1)

"""
class ArrayQueue:
    """FIFO queue using Python list as underlying storage"""
    DEDAULT_CAPACITY = 10
    def __init__(self):
        """create an empty queue"""
        self._data = [None] * ArrayQueue.DEDAULT_CAPACITY
        self._size = 0
        self._front = 0
    def __len__(self):
        """ return the length of the queue"""
        return self._size
    def isEmpty(self):
        """return True if the queue is Empty"""
        return self._size == 0
    def first(self):
        """ return the first element at the front of the QUEUE
        and raise Empty Exception if the queue is empty"""
        if self.isEmpty():
            raise ("The queue is empty")
        else:
            return self._data[self._front]
    def dequeue(self):
        """ remove and return the first element in the queue """
        if self.isEmpty():
            raise ("The Queue is empty.\n")
        else:
            first = self._data[self._front]
            self._data[self._front] = None
            self._front= (self._front+1) % len(self._data)
            self._size -= 1
            return first

    def enqueue(self, elements):
        """ add an element to the back of the queue """
        if self._size == len(self._data):
            self._resize(2 * len(self._data)) # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = elements
        self._size += 1

    def _resize(self, cap):
        """resize to a new list of capacity >= len(self) """
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):         # only consider existing elements
            self._data[k]= old[walk]        # intentionally shift indices
            walk = (1 +walk)% len(old)      # use old size as modulus
        self._front = 0                     # front has been realigned

if __name__ == '__main__':
    queue = ArrayQueue()
    queue.enqueue("a")
    queue.enqueue("b")
    queue.enqueue("c")
    print(queue.dequeue())


