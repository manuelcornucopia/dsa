class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return. self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, prev_data, data):
        current = self.head
        while current and current.data != prev_data:
            current = currnet.next
        if current is None:
            return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        current = self.head

        if current and current.data == data:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next
        current = None
