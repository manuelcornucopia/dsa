from queue import Queue
from stack import Stack


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = TreeNode(value)

        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search(self, value):
        current = self.root
        while current:
            if value == current.value:
                return True
            current = current.left if value < current.value else current.right
        return False

    def delete(self, value):
        parent, current = None, self.root

        # Find the node and its parent.
        while current and current.value != value:
            parent = current
            current = current.left if value < current.value else current.right
        if current is None:
            return  # Not found.

        has_left = current.left is not None
        has_right = current.right is not None

        # Case 0: no children (leaf).
        if not has_left and not has_right:
            if parent is None:
                self.root = None
            elif parent.left is current:
                parent.left = None
            else:
                parent.right = None
            return

        # Case 1: exaclty one child.
        if has_left ^ has_right:
            child = current.left if has_left else current.right
            if parent is None:
                self.root = child