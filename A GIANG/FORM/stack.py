"""
push            O(1)
pop             O(1)
top             O(1)
isEmpty         O(1)
len()           O(1)

"""

class ArrayStack:
    "LIFO stack implementation using a Python list as underlying storage"
    def __init__(self):
        # create an empty stack
        self._data = []
    def __len__(self):
        # return the number of elements in stack
        return len(self._data)
    def is_empty(self):
        # return True if stack is empty
        return len(self._data) == 0
    def push(self, element):
        "add element to the top of stack"
        self._data.append(element)
    def top(self):
        "return but do not remove the element at the top of stack"
        if self.is_empty():
            raise ("Stack is empty\n")
        else:
            return self._data[-1]
    def pop(self):
        "remove and return the"
        if self.is_empty():
            raise ("Stack is empty\n")
        else:
            self._data.pop()
    def printStack(self):
        print(self._data)

if __name__ == '__main__':
    stack = ArrayStack()
    stack.push(44)
    stack.push(42)
    stack.push(4)
    stack.push(41)
    stack.push(432)
    stack.push(432)
    stack.push(441)
    stack.push(4422)
    stack.printStack()
    stack.pop()
    stack.printStack()