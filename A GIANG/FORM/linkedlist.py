class Node:
    def __init__(self, data= None):
        self.data = data
        self.next = None
    @property
    def getNode(self):
        return self.data
    def getNext(self):
        return self.next
    def setNex(self, new_next):
        self.next = new_next

class linked_list:
    def __init__(self):
        # create an empty list
        self.tail = None
        self.head = None
        self.count = 0
    def iterate_item(self):
        current_item = self.tail
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val

    def append_item(self, data):
        # append items on the list
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            # cai dau
            self.tail= node
            self.head= node
        self.count +=1

