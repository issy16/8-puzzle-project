import heapq
from puzzle_state import Node
def uniform_cost_search(initial_state, goal_state):
    open_set = []
    root_node = Node(algo='ucs', state=initial_state, parent=None, level=0)
    heapq.heappush(open_set, root_node)
    
    while open_set:
        current_node = heapq.heappop(open_set)
        if current_node.state == goal_state:
            return current_node  # Solution found

        children = current_node.expand()
        for child in children:
            heapq.heappush(open_set, child)
    
    return None  # No solution

# Define your initial state and goal state
initial_state = [1, 2, 3, 4, 0, 6, 7, 5, 8]  # Example initial state
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]  # The goal state

# Perform uniform cost search
result_node = uniform_cost_search(initial_state, goal_state)

# If a solution exists, print the steps to solve the puzzle
if result_node:
    path = []
    while result_node.parent is not None:  # Trace back the path from goal to start
        path.append(result_node.state)
        result_node = result_node.parent
    path.reverse()  # Reverse the path to get it from start to goal
    for step in path:
        print(step)
else:
    print("No solution found.")