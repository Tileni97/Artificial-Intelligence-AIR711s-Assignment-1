# search.py
from collections import deque

def a_star_search(grid, start, goal, heuristic):
    open_set = deque([(start, 0, heuristic(start, goal))])
    closed_set = set()
    g_cost = {start: 0}
    parent = {start: None}

    while open_set:
        current, cost_so_far, _ = open_set.popleft()

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path, cost_so_far

        closed_set.add(current)

        for neighbor in get_neighbors(grid, current):
            new_cost = cost_so_far + 1
            if neighbor not in closed_set or new_cost < g_cost.get(neighbor, float('inf')):
                g_cost[neighbor] = new_cost
                f_score = new_cost + heuristic(neighbor, goal)
                open_set.append((neighbor, new_cost, f_score))
                parent[neighbor] = current

    return [], float('inf')

def get_neighbors(grid, pos):
    rows, cols = len(grid), len(grid[0])
    x, y = pos
    neighbors = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != -1:
            neighbors.append((nx, ny))

    return neighbors