# Define cell states
OBSTACLE = -1  # Represents an obstacle in the grid
FLOOR = 0      # Represents an empty cell in the grid
ROBOT = 1      # Represents the position of the robot in the grid
TARGET = 2     # Represents the position of the target in the grid

class Environment:
    def __init__(self, grid_size, obstacles, robot_pos, target_pos):
        """
        Initialize the environment with the given parameters.

        Args:
        - grid_size (tuple): Size of the grid as (rows, columns).
        - obstacles (list of tuples): Positions of obstacles in the grid.
        - robot_pos (tuple): Initial position of the robot in the grid.
        - target_pos (tuple): Position of the target in the grid.
        """
        self.grid_size = grid_size
        # Initialize the grid with all cells set to FLOOR
        self.grid = [[FLOOR for _ in range(grid_size[1])] for _ in range(grid_size[0])]
        self.set_obstacles(obstacles)          # Set obstacles in the environment
        self.set_robot_position(robot_pos)     # Set initial position of the robot
        self.set_target_position(target_pos)   # Set position of the target

    def set_obstacles(self, obstacles):
        """
        Set obstacles in the grid.

        Args:
        - obstacles (list of tuples): Positions of obstacles in the grid.
        """
        for x, y in obstacles:
            self.grid[x][y] = OBSTACLE

    def set_robot_position(self, pos):
        """
        Set the position of the robot in the grid.

        Args:
        - pos (tuple): Position of the robot in the grid.
        """
        x, y = pos
        self.grid[x][y] = ROBOT

    def set_target_position(self, pos):
        """
        Set the position of the target in the grid.

        Args:
        - pos (tuple): Position of the target in the grid.
        """
        x, y = pos
        self.grid[x][y] = TARGET
