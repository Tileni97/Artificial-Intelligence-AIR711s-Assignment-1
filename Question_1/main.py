# main.py
from environment import Environment
from heuristics import manhattan_distance, obstacle_aware_heuristic
from search import a_star_search
from visualization import print_grid, visualize_path, visualize_grid

# Initialize the environment
grid_size = (10, 10)
obstacles = [(3, 4), (6, 2), (7, 7)]
robot_pos = (0, 0)
target_pos = (9, 9)
env = Environment(grid_size, obstacles, robot_pos, target_pos)

# Test with the Manhattan distance heuristic method
start_pos = robot_pos
goal_pos = target_pos
path, cost = a_star_search(env.grid, start_pos, goal_pos, manhattan_distance)
print("Path (Manhattan distance heuristic):", path)
print("Total cost (Manhattan distance heuristic):", cost)

# Test with the obstacle-aware heuristic
path, cost = a_star_search(env.grid, start_pos, goal_pos, lambda pos1, pos2: obstacle_aware_heuristic(env.grid, pos1, pos2))
print("\nPath (Obstacle-aware heuristic):", path)
print("Total cost (Obstacle-aware heuristic):", cost)

# Visualizes the environment and the planned path
print("\nInitial environment:")
print_grid(env.grid)
visualize_path(env.grid, path)
visualize_grid(env.grid, path)