from puzzle_process import Problem

def main():
    print("Welcome to the 8 puzzle solver.")
    choice = input("Type '1' to use a default puzzle, or '2' to enter your own puzzle: ")
    algorithm = 'uniform_cost'
    puzzle_size = 3
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0] 
    
    if choice == '1':
        initial_state = [1, 0, 3, 4, 2, 6, 7, 5, 8]  
    elif choice == '2':
        initial_state = []
        print("Enter your puzzle, use a zero to represent the blank")
        for i in range(3):  # a 3x3 puzzle
            row = input(f"Enter row {i+1}, use spaces between numbers: ")
            initial_state.extend(map(int, row.split()))
        for i in range(0, 9, 3):
            print(initial_state[i:i+3])
    else:
        print("Invalid choice. Exiting.")
        return
    
    print("\nChoose your algorithm:")
    print("1. Uniform Cost Search")
    print("2. A* with the Misplaced Tile heuristic")
    print("3. A* with the Euclidean Distance heuristic")
    choice = input("Enter your choice of algorithm: ")

    if choice == '1':
        algorithm = 'uniform'
    elif choice == '2':
        algorithm = 'misplaced'
    elif choice == '3':
        algorithm = 'euclidean'
    else:
        print("Invalid algorithm choice. Exiting.")
        return
    
    solver = Problem(puzzle_size, algorithm, initial_state, goal_state)
    solution = solver.solve()



main()
 