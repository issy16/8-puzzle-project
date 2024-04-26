import heapq

class Frontier:
    def __init__(self):
        self.heap = []
        self.states = set()  

    def insert(self, node):
        """Add a new node or update the priority of an existing node."""
        heapq.heappush(self.heap, node)
        self.states.add(tuple(node.state))

    def pop(self):
        """Remove and return the lowest cost node from the heap."""
        node = heapq.heappop(self.heap)
        self.states.remove(tuple(node.state)) 
        return node

    def is_empty(self):
        """Return True if the frontier is empty."""
        return len(self.heap) == 0

    def contains_state(self, state):
        """Check if a specific state is in the frontier."""
        return tuple(state) in self.states