from puzzle_state import Node 
from frontier import Frontier
class Problem:
    
    def __init__(self, puzzle_size, algorithm, initial_state, goal_state):
   
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.puzzle_size = puzzle_size
        self.algorithm = algorithm
        self.frontier = Frontier()
        self.node_expanded_count = 0

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
        #"""Check if the problem is solvable"""
        #if self.is_unsolvable(): 
         #   print("This puzzle is unsolvable.")
         #   return None
        
        root_node = Node(algo=self.algorithm, state=self.initial_state, goal_state=self.goal_state, parent=None, level=0, puzzle_size = self.puzzle_size)
        self.frontier.insert(root_node)              # Initialize the frontier using the initial state of problem
        explored = set()                             # Initialize the explored set to be empty
        
        while not self.frontier.is_empty():                       # If the frontier is empty, return failure
            current_node = self.frontier.pop()       # Choose a leaf node and remove it from the frontier 
            if(self.goal_state==current_node.state): # If the node contains a goal state then return the solution
                print("Find it!")
                current_node.print_path()
                print(f"Total nodes expanded:{self.node_expanded_count}")
                print(f"Maximum queue size: {self.frontier.max_queue_size()}")
                return current_node
            explored.add(tuple(current_node.state))  # Add the node to the explored set
            children = current_node.expand()         # Expand the chosen node
            self.node_expanded_count +=1               # Adding the result nodes to the frontier only if not in
            for child in children:                     # the frontier or explored set
                if tuple(child.state) not in explored and not self.frontier.contains_state(child.state):
                    self.frontier.insert(child)        
        
        print("This puzzle is unsolvable.")
        print(f"Total nodes expanded:{self.node_expanded_count}")
        print(f"Maximum queue size: {self.frontier.max_queue_size()}")
        return None