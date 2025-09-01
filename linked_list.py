class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    
class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(aelf):
        return self.head is None

    def append(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        if not self.head:
            return
        if self.head.data == key:
            self.head = self.head.next
            return
        previous, current = None, self.head
        while current and current.data != key:
            previous, current = current, current.next
        if current:
            previous.next = current.next
