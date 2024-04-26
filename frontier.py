import heapq

class Frontier:
    def __init__(self):
        self.heap = []
      
    def insert(self, node):
        """Add a new node or update the priority of an existing node"""
        heapq.heappush(self.heap, node)

    def pop(self):
        """Remove and return the lowest cost node from the heap."""
        return heapq.heappop(self.heap)

    def is_empty(self):
        """Return True if the frontier is empty."""
        return len(self.heap) == 0
