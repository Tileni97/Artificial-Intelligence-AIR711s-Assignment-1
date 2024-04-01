# heuristics.py

def manhattan_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x1 - x2) + abs(y1 - y2)

def obstacle_aware_heuristic(grid, pos1, pos2, obstacle_penalty=10):
    x1, y1 = pos1
    x2, y2 = pos2
    obstacles = 0
    dx = 1 if x2 > x1 else -1
    dy = 1 if y2 > y1 else -1

    x, y = x1, y1
    while x != x2 or y != y2:
        x += dx
        y += dy
        if grid[x][y] == -1:
            obstacles += 1

    return manhattan_distance(pos1, pos2) + obstacles * obstacle_penalty