from collections import deque
from pathfinding import manhattan_distance, obstacle_aware_heuristic  # Import heuristic functions from pathfinding module

def a_star_search(grid, start, goal, heuristic):
    """
    A* search algorithm to find the optimal path from start to goal.

    Args:
    - grid (list of lists): The grid environment.
    - start (tuple): Start position as a tuple (x, y).
    - goal (tuple): Goal position as a tuple (x, y).
    - heuristic (function): Heuristic function to estimate the cost from a state to the goal.

    Returns:
    - tuple: Optimal path from start to goal and its total cost.
    """
    open_set = deque([(start, 0, heuristic(start, goal))])  # Initialize open set with start position, cost so far, and heuristic value
    closed_set = set()  # Initialize closed set
    g_cost = {start: 0}  # Initialize cost from start to current position
    parent = {start: None}  # Initialize parent map

    while open_set:
        current, cost_so_far, _ = open_set.popleft()  # Get current position and its cost from open set

        if current == goal:  # Check if the goal is reached
            path = []
            while current:
                path.append(current)
                current = parent[current]  # Trace back to find the path
            path.reverse()
            return path, cost_so_far  # Return the path and its total cost

        closed_set.add(current)  # Add current position to closed set

        for neighbor in get_neighbors(grid, current):  # Iterate through neighbors of the current position
            new_cost = cost_so_far + 1  # Calculate new cost from start to neighbor
            if neighbor not in closed_set or new_cost < g_cost.get(neighbor, float('inf')):
                # If neighbor is not in closed set or the new cost is less than the previous cost
                g_cost[neighbor] = new_cost  # Update cost from start to neighbor
                f_score = new_cost + heuristic(neighbor, goal)  # Calculate f-score using heuristic
                open_set.append((neighbor, new_cost, f_score))  # Add neighbor to open set with updated cost and f-score
                parent[neighbor] = current  # Update parent map with neighbor

    return [], float('inf')  # Return empty path and infinite cost if no path is found

def get_neighbors(grid, pos):
    """
    Get neighboring positions of a given position in the grid.

    Args:
    - grid (list of lists): The grid environment.
    - pos (tuple): Position as a tuple (x, y).

    Returns:
    - list: List of neighboring positions.
    """
    rows, cols = len(grid), len(grid[0])  # Get the number of rows and columns in the grid
    x, y = pos
    neighbors = []  # Initialize list of neighbors
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Define possible directions (right, left, down, up)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != -1:
            # Check if neighbor is within grid boundaries and not an obstacle
            neighbors.append((nx, ny))  # Add valid neighbor to the list

    return neighbors  # Return the list of neighboring positions
