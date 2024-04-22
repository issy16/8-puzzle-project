class Node: # Represents a single state in the search space
    def __init__(self, state, parent, goal, operator=None, heuristic_type='none',level=0, puzzle_size=3):
        self.puzzle_size = puzzle_size
        self.state = state
        self.parent = parent
        self.goal = goal
        self.operator = operator
        self.heuristic_type = heuristic_type
        self.cost = self.calculate_cost()
        self.level = level

    def calculate_cost(self):  
        """Calculate the total cost based on the chosen heuristic and level (depth). """
        heuristic_cost = 0
        if self.heuristic_type == 'misplaced':
            heuristic_cost = self.misplaced_tiles()
        elif self.heuristic_type == 'euclidean':
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

class Tree: # Represents the search space
    def __init__(self, root):
        self.root = root
        self.nodes = [root]
    