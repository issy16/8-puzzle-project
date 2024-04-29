
import math

class Node: # Represents a single state(node) in the search space(tree)
    def __init__(self, algo, state, goal_state, parent,level=0, puzzle_size=3):
        self.algo = algo
        self.puzzle_size = puzzle_size
        self.state = state
        self.goal_state = goal_state
        self.parent = parent
        self.level = level
        self.cost = self.compute_cost()
        self.heuristic_cost = self.cost - self.level
    
        
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
        """ Calculate the number of misplaced tiles """
        count = 0
        for i in range(len(self.state)):
            if self.state[i] != 0 and self.state[i] != self.goal_state[i]:
                count += 1
        return count

    def euclidean_distance(self):
        """ Calculate the Euclidean distance of the tiles from their goal positions """
        distance = 0
        for idx, tile in enumerate(self.state):
            if tile != 0: 
                target_idx = self.goal_state.index(tile)
                row, col = divmod(idx, self.puzzle_size)
                # Calculate target position (row, col)
                target_row, target_col = divmod(target_idx, self.puzzle_size)
                # Calculate Euclidean distance for this tile
                distance += math.sqrt((target_row - row)**2 + (target_col - col)**2)
        return distance
    
    def __str__(self):
        output = ""
        for i in range(0, len(self.state), self.puzzle_size):  
            row = self.state[i:i + self.puzzle_size]
            row_str = ""
            for num in row:
                row_str += str(num) + " "
            output += row_str.strip() + "\n" 
        if self.algo == 'misplaced' or self.algo == 'euclidean':
            return f"The best state to expand with g(n) = {self.level} and h(n) = {self.heuristic_cost} is:\n{output}"
        else:
            return f"The state to expand with f(n) = {self.cost} is:\n{output}"

    def _swap_positions(self, idx1, idx2):
        """Swap two positions in the state and return the new state."""
        new_state = list(self.state)
        new_state[idx1], new_state[idx2] = new_state[idx2], new_state[idx1]
        return new_state
    
    def expand(self):
        """ Return a list of children nodes """
        children = []
        empty_idx = self.state.index(0)  # Find the index of the empty space (0)
        row, col = divmod(empty_idx, self.puzzle_size)
        
        """ Helper to swap positions in the state """
        def swap_(idx1, idx2):
            new_state = list(self.state)
            new_state[idx1], new_state[idx2] = new_state[idx2], new_state[idx1]
            return new_state
        
        moves = []
        """ Define valide conditions and move """
        if(col > 0):
            moves.append(empty_idx - 1) # move left
        if(col < self.puzzle_size - 1):
            moves.append(empty_idx + 1) # move right
        if(row > 0):
            moves.append(empty_idx - self.puzzle_size) # move up
        if(row < self.puzzle_size - 1):
            moves.append(empty_idx + self.puzzle_size) # move down
        
        for move in moves:
            new_state = self._swap_positions(empty_idx, move)
            child_node = Node(algo=self.algo, state=new_state, goal_state=self.goal_state, parent=self, level=self.level + 1, puzzle_size=self.puzzle_size)
            children.append(child_node)
  
        return children
        
    def print_path(self):
        """Prints the path from the root node to this node"""
        path = []
        current_node = self
        while current_node:
            path.append(current_node)
            current_node = current_node.parent

        path.reverse()
        # Print the path
        for node in path:
            print(node)
        