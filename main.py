import PuzzleSolver


def main():
    print("Welcome to the 8 puzzle solver.")
    choice = input("Type '1' to use a default puzzle, or '2' to enter your own puzzle: ")
    
    if choice == '1':
        initial_state = [1, , 3, 4, 2, 6, 7, 5, 8]  # default puzzle 
    elif choice == '2':
        initial_state = []
        print("Enter your puzzle, use a zero to represent the blank")
        for i in range(3):  # a 3x3 puzzle
            row = input(f"Enter row {i+1}, use spaces between numbers: ")
            initial_state.extend(map(int, row.split()))

    print("\nChoose your algorithm:")
    print("1. Uniform Cost Search")
    print("2. A* with the Misplaced Tile heuristic")
    print("3. A* with the Euclidean Distance heuristic")
    algorithm_choice = input("Enter your choice of algorithm: ")

    if algorithm_choice == '1':
        algorithm = 'uniform_cost'
    elif algorithm_choice == '2':
        algorithm = 'misplaced_tile'
    elif algorithm_choice == '3':
        algorithm = 'euclidean_distance'
    else:
        print("Invalid algorithm choice. Exiting.")
        return
    
    solver = PuzzleSolver(algorithm, initial_state, goal_state=[1,2,3,4,5,6,7,8,0])
    solution = solver.solve()
    print(solution)  


main()
