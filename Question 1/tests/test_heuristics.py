# test_heuristics.py
from pathlib import Path
import sys

# Add the parent directory to the system path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from environment import Environment, OBSTACLE, FLOOR, ROBOT, TARGET
from heuristics import manhattan_distance, obstacle_aware_heuristic
from search import a_star_search

def run_test_case(grid, robot_pos, target_pos):
    env = Environment(grid_size=(len(grid), len(grid[0])), obstacles=[], robot_pos=robot_pos, target_pos=target_pos)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == OBSTACLE:
                env.set_obstacles([(x, y)])

    manhattan_path, manhattan_cost = a_star_search(env.grid, robot_pos, target_pos, manhattan_distance)
    obstacle_aware_path, obstacle_aware_cost = a_star_search(env.grid, robot_pos, target_pos, lambda pos1, pos2: obstacle_aware_heuristic(env.grid, pos1, pos2))

    print(f"Test Case: Grid={grid}, Robot={robot_pos}, Target={target_pos}")
    print(f"Manhattan Distance Heuristic: Path Length={len(manhattan_path)}, Total Cost={manhattan_cost}")
    print(f"Obstacle-Aware Heuristic: Path Length={len(obstacle_aware_path)}, Total Cost={obstacle_aware_cost}")
    print()

def test_heuristics():
    # Test Case 1
    grid = [
        [FLOOR, FLOOR, OBSTACLE, FLOOR],
        [FLOOR, FLOOR, FLOOR, FLOOR],
        [OBSTACLE, FLOOR, FLOOR, FLOOR],
        [FLOOR, FLOOR, FLOOR, FLOOR]
    ]
    robot_pos = (0, 0)
    target_pos = (3, 3)
    run_test_case(grid, robot_pos, target_pos)

    # Test Case 2 (Add more test cases as needed)
    # ...

if __name__ == "__main__":
    test_heuristics()