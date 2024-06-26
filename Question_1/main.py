# Import necessary modules
from environment import Environment  # Import the Environment class from environment.py
from heuristics import manhattan_distance, obstacle_aware_heuristic  # Import heuristics functions
from search import a_star_search  # Import A* search algorithm
from visualization import print_grid, visualize_path, visualize_grid  # Import visualization functions

# Initialize the environment
grid_size = (15, 10)  # Define the size of the grid
obstacles = [  # Define the positions of obstacles in the grid
    (0, 0), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
    (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0), (14, 0),
    (14, 9), (13, 9), (12, 9), (11, 9), (10, 9), (9, 9), (8, 9), (7, 9), (6, 9), (5, 9), (4, 9), (3, 9), (2, 9), (1, 9),
    (14, 1), (14, 2), (14, 3), (14, 4), (14, 5), (14, 6), (14, 7), (14, 9),
    (11, 8), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
    (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (8, 4), (9, 4), (8, 6), (8, 2), (9, 2), (7, 2), (6, 2), (10, 2),
    (5, 2), (4, 2), (4, 3), (4, 4), (4, 5), (5, 5), (12, 2), (13, 4), (12, 6)
]  # Define the positions of obstacles in the grid
robot_pos = (0, 1)  # Define the initial position of the robot
target_pos = (14, 8)  # Define the position of the target
env = Environment(grid_size, obstacles, robot_pos, target_pos)  # Create an instance of the Environment class

# Test with the Manhattan distance heuristic method
start_pos = robot_pos  # Define the start position of the robot
goal_pos = target_pos  # Define the goal position of the robot
# Find the optimal path using A* search algorithm with Manhattan distance heuristic
path, cost = a_star_search(env.grid, start_pos, goal_pos, manhattan_distance)
print("Path (Manhattan distance heuristic):", path)  # Print the optimal path
print("Total cost (Manhattan distance heuristic):", cost)  # Print the total cost of the path

# Test with the obstacle-aware heuristic
# Find the optimal path using A* search algorithm with obstacle-aware heuristic
path, cost = a_star_search(env.grid, start_pos, goal_pos, lambda pos1, pos2: obstacle_aware_heuristic(env.grid, pos1, pos2))
print("\nPath (Obstacle-aware heuristic):", path)  # Print the optimal path
print("Total cost (Obstacle-aware heuristic):", cost)  # Print the total cost of the path

# Visualizes the environment and the planned path
print("\nInitial environment:")  # Print the initial environment
print_grid(env.grid)  # Print the grid
visualize_path(env.grid, path)  # Visualize the path on the grid
visualize_grid(env.grid, path)  # Visualize the grid with path
