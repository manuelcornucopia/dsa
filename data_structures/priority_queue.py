from heap import MinHeap, MaxHeap


class MinPriorityQueue:
    def __init__(self):
        self.heap = MinHeap()
        self._count = 0  # Tie-braker to guarantee FIFO for equal priorities.

    def push(self, priority, value):
        # Store (priority, count, value) so ties are resolved by insertion order.
        self.heap.insert((priority, self._count, value))
        self._count += 1

    def pop(self):
        node = self.heap.extract_min()
        return node[2] if node is not None else None

    def is_empty(self):
        return len(self.heap.heap) == 0


class MaxPriorityQueue:
    def __init__(self):
        self.heap = MaxHeap()
        self._count = 0

    def push(self, priority, value):
        # Negate count so that earlier items come out first when priorities tie.
        self.heap.insert((priority, -self._count, value))
        self._count += 1

    def pop(self):
        node = self.heap.extract_max()
        return node[2] if node is not None else None

    def is_empty(self):
        return len(self.heap.heap) == 0
