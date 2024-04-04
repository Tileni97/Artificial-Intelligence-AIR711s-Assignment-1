from environment import OBSTACLE  # Import the OBSTACLE constant from environment.py

def manhattan_distance(pos1, pos2):
    """
    Calculate the Manhattan distance between two positions.

    Args:
    - pos1 (tuple): Position 1 as a tuple (x1, y1).
    - pos2 (tuple): Position 2 as a tuple (x2, y2).

    Returns:
    - int: Manhattan distance between the two positions.
    """
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x1 - x2) + abs(y1 - y2)

def obstacle_aware_heuristic(grid, pos1, pos2, obstacle_penalty=15):
    """
    Calculate a heuristic that is aware of obstacles in the grid.

    Args:
    - grid (list of lists): The grid environment.
    - pos1 (tuple): Position 1 as a tuple (x1, y1).
    - pos2 (tuple): Position 2 as a tuple (x2, y2).
    - obstacle_penalty (int, optional): Penalty for encountering an obstacle.

    Returns:
    - int: Heuristic value.
    """
    rows, cols = len(grid), len(grid[0])  # Get the number of rows and columns
    x1, y1 = pos1
    x2, y2 = pos2
    obstacles = 0
    dx = 1 if x2 > x1 else -1
    dy = 1 if y2 > y1 else -1

    x, y = x1, y1
    while 0 <= x < rows and 0 <= y < cols and (x != x2 or y != y2):  # Check if within grid boundaries
        if grid[x][y] == OBSTACLE:
            obstacles += 1
        x += dx
        y += dy

    return manhattan_distance(pos1, pos2) + obstacles * obstacle_penalty  # Return the heuristic value
