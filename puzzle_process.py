from puzzle_state import Node 
from frontier import Frontier
class Problem:
    
    def __init__(self, puzzle_size, algorithm, initial_state, goal_state):
   
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.puzzle_size = puzzle_size
        self.algorithm = algorithm
        self.frontier = Frontier()

    def is_unsolvable(self):
        """The puzzle is solvable if the number of inversions is even."""
        inversion = 0
        state = self.initial_state
        
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if state[i] > state[j] and state[i] != 0 and state[j] != 0:
                    inversion += 1

        return inversion % 2 != 0
 
    def solve(self):
        """Check if the problem is solvable"""
        if self.is_unsolvable(): 
            print("This puzzle is unsolvable.")
            return None
        
        root_node = Node(algo=self.algorithm, state=self.initial_state, parent=None, level=0, puzzle_size = self.puzzle_size)
        self.frontier.insert(root_node)
        explored = set()
        
        while self.frontier:
            current_node = self.frontier.pop()
            explored.add(tuple(current_node.state)) 
            
            if(self.goal_state==current_node.state):
                print("Find it!")
                return current_node
            children = current_node.expand()
            
            for child in children:
                if tuple(child.state) not in explored and not self.frontier.contains_state(child.state):
                    self.frontier.insert(child)
                    
            return 0