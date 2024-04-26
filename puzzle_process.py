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
      
        return False

    def solve(self):
        """
        Solves the puzzle using the specified algorithm.
        :return: The solution to the puzzle, or None if unsolvable.
        """
        if self.is_unsolvable():
            print("This puzzle is unsolvable.")
            return None
        else:
            root_node = Node(algo=self.algorithm, state=self.initial_state, parent=None, level=0, puzzle_size = self.puzzle_size)
            self.frontier.insert(root_node)
            
            return 0