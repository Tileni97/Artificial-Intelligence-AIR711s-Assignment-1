# Import necessary modules and classes
from environment import Environment, OBSTACLE, FLOOR, ROBOT, TARGET  # Import Environment class and constants from environment.py
from heuristics import manhattan_distance, obstacle_aware_heuristic  # Import heuristic functions from heuristics.py
from search import a_star_search  # Import A* search algorithm from search.py

# Define a function to run a test case
def run_test_case(grid, robot_pos, target_pos):
    # Initialize the environment
    env = Environment(grid_size=(len(grid), len(grid[0])), obstacles=[], robot_pos=robot_pos, target_pos=target_pos)
    # Set obstacles in the environment based on the grid
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == OBSTACLE:
                env.set_obstacles([(x, y)])

    # Find path and cost using Manhattan distance heuristic
    manhattan_path, manhattan_cost = a_star_search(env.grid, robot_pos, target_pos, manhattan_distance)
    # Find path and cost using obstacle-aware heuristic
    obstacle_aware_path, obstacle_aware_cost = a_star_search(env.grid, robot_pos, target_pos, lambda pos1, pos2: obstacle_aware_heuristic(env.grid, pos1, pos2))

    # Print test case results
    print(f"Test Case: Grid={grid}, Robot={robot_pos}, Target={target_pos}")
    print(f"Manhattan Distance Heuristic: Path Length={len(manhattan_path)}, Total Cost={manhattan_cost}")
    print(f"Obstacle-Aware Heuristic: Path Length={len(obstacle_aware_path)}, Total Cost={obstacle_aware_cost}")
    print()

# Define a function to run multiple test cases
def test_heuristics():
    # Test Case 1
    grid1 = [
        [FLOOR, FLOOR, OBSTACLE, FLOOR],
        [FLOOR, FLOOR, FLOOR, FLOOR],
        [OBSTACLE, FLOOR, FLOOR, FLOOR],
        [FLOOR, FLOOR, FLOOR, FLOOR]
    ]
    robot_pos1 = (0, 0)
    target_pos1 = (3, 3)
    run_test_case(grid1, robot_pos1, target_pos1)

    # Test Case 2
    grid2 = [
        [ROBOT, OBSTACLE, FLOOR],
        [FLOOR, FLOOR, FLOOR],
        [FLOOR, FLOOR, TARGET]
    ]
    robot_pos2 = (0, 0)
    target_pos2 = (2, 2)
    run_test_case(grid2, robot_pos2, target_pos2)

    # Test Case 3
    grid3 = [
        [FLOOR, OBSTACLE, OBSTACLE, FLOOR],
        [FLOOR, FLOOR, FLOOR, OBSTACLE],
        [ROBOT, OBSTACLE, FLOOR, FLOOR],
        [FLOOR, FLOOR, FLOOR, TARGET]
    ]
    robot_pos3 = (0, 0)
    target_pos3 = (3, 3)
    run_test_case(grid3, robot_pos3, target_pos3)

# Run the test cases if the script is executed directly
if __name__ == "__main__":
    test_heuristics()
