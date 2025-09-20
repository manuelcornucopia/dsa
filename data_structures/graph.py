from queue import Queue
from stack import Stack


class Graph:
    def __init__(self, directed=False, weighted=False):
        self.graph = {}
        self.directed = directed
        self.weighted = weighted

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            self.graph.pop(vertex)

        for u in self.graph:
            if self.weighted:
                self.graph[u] = [(node, w) for (node, w) in self.graph[u] if node != vertex]
            else:
                if vertex in self.graph[u]:
                    self.graph[u].remove(vertex)

    def add_edge(self, u, v, weight=1):
        if u not in self.graph:
            self.add_vertex(u)
        if v not in self.graph:
            self.add_vertex(v)
        
        if self.weighted:
            self.graph[u].append((v, weight))
            if not self.directed:
                self.graph[v].append((u, weight))
        else:
            self.graph[u].append(v)
            if not self.directed:
                self.graph[v].append(u)

    def remove_edge(self, u, v):
        if u in self.graph:
            if self.weighted:
                self.graph[u] = [(node, w) for (node, w) in self.graph[u] if node != v]
            else:
                if v in self.graph[u]:
                    self.graph[u].remove(v)

        if not self.directed and v in self.graph:
            if self.weighted:
                self.graph[v] = [(node, w) for (node, w) in self.graph[v] if node != u]
            else:
                if u in self.graph[v]:
                    self.graph[v].remove(u)

    def bfs(self, start):
        visited = set()
        result = []
        queue = Queue()

        queue.enqueue(start)

        while not queue.is_empty():
            vertex = queue.dequeue()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)

                neighbors = self.graph.get(vertex, [])
                if self.weighted:
                    neighbors = [n for (n, w) in neighbors]

                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.enqueue(neighbor)

        return result

    def dfs(self, start):
        visited = set()
        result = []
        stack = Stack()

        stack.push(start)

        while not stack.is_empty():
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)

                neighbors = self.graph.get(vertex, [])
                if self.weighted:
                    neighbors = [n for (n, w) in neighbors]

                for neighbor in reversed(neighbors):
                    if neighbor not in visited:
                        stack.push(neighbor)

        return result