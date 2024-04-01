# environment.py

# Define cell states
OBSTACLE = -1
FLOOR = 0
ROBOT = 1
TARGET = 2

class Environment:
    def __init__(self, grid_size, obstacles, robot_pos, target_pos):
        self.grid_size = grid_size
        self.grid = [[FLOOR for _ in range(grid_size[1])] for _ in range(grid_size[0])]
        self.set_obstacles(obstacles)
        self.set_robot_position(robot_pos)
        self.set_target_position(target_pos)

    def set_obstacles(self, obstacles):
        for x, y in obstacles:
            self.grid[x][y] = OBSTACLE

    def set_robot_position(self, pos):
        x, y = pos
        self.grid[x][y] = ROBOT

    def set_target_position(self, pos):
        x, y = pos
        self.grid[x][y] = TARGET