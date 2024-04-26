
class Node: # Represents a single state(node) in the search space(tree)
    def __init__(self, algo, state, parent,level=0, puzzle_size=3):
        self.algo = algo
        self.puzzle_size = puzzle_size
        self.state = state
        self.parent = parent
        self.level = level
        self.cost = self.compute_cost()
        
    def __lt__(self, other):
        """Define less than for Node to compare based on cost for heapq."""
        return self.cost < other.cost
    
    def compute_cost(self):  
        """Calculate the total cost based on the chosen heuristic and level (depth). """
        heuristic_cost = 0
        if self.algo == 'misplaced':
            heuristic_cost = self.misplaced_tiles()
        elif self.algo == 'euclidean':
            heuristic_cost = self.euclidean_distance()

        return self.level + heuristic_cost
    
    def misplaced_tiles(self):
        """ Calculate the number of misplaced tiles excluding the blank space (0). """
        return 0

    def euclidean_distance(self):
        """ Calculate the Euclidean distance of the tiles from their goal positions. """
        return 0
    
    def __str__(self):
        """ Return a readable string representation of the node. """
        return 0

    def expand(self):
        """ Return a list of children nodes. """
        children = []
        new_state = self.state[:] 
        child_node = Node(algo=self.algo, state=new_state, parent=self, level=self.level + 1, puzzle_size=self.puzzle_size)
        children.append(child_node)
        return children
        
    