# visualization.py
import matplotlib.pyplot as plt

def print_grid(grid):
    """
    Prints the grid using ASCII characters to represent different elements.

    Args:
        grid (list): The grid representing the environment.
    """
    for row in grid:
        for cell in row:
            if cell == -1:
                print('██', end='')  # Obstacle
            elif cell == 0:
                print('  ', end='')  # Floor
            elif cell == 1:
                print('🤖 ', end='')  # Robot
            elif cell == 2:
                print('⚡', end='')   # Target (charging station)
            else:
                print('XX', end='')  # Unknown state
        print()

def visualize_path(grid, path):
    """
    Visualizes the robot's path by modifying the grid and printing it.

    Args:
        grid (list): The grid representing the environment.
        path (list): The planned path for the robot as a list of positions.
    """
    # Create a copy of the grid to avoid modifying the original
    visualized_grid = [row[:] for row in grid]

    # Mark the path on the grid
    for x, y in path:
        visualized_grid[x][y] = 3  # Use a different value to represent the path

    print("Visualizing the path:")
    print_grid(visualized_grid)

def visualize_grid(grid, path=None):
    """
    Visualizes the grid using matplotlib.

    Args:
        grid (list): The grid representing the environment.
        path (list, optional): The planned path for the robot as a list of positions.
    """
    rows, cols = len(grid), len(grid[0])
    fig, ax = plt.subplots(figsize=(cols, rows))

    for x in range(rows):
        for y in range(cols):
            cell_value = grid[x][y]
            if cell_value == -1:
                ax.add_patch(plt.Rectangle((y, x), 1, 1, facecolor='black'))  # Obstacle
            elif cell_value == 1:
                ax.add_patch(plt.Circle((y + 0.5, x + 0.5), 0.3, facecolor='green'))  # Robot
            elif cell_value == 2:
                ax.add_patch(plt.Circle((y + 0.5, x + 0.5), 0.3, facecolor='red'))  # Target

    if path:
        print("Plotting path:", path)  # Added for debugging
        path_x = [y for x, y in path]
        path_y = [x for x, y in path]  # Updated to plot correctly
        print("Path x-coordinates:", path_x)  # Added for debugging
        print("Path y-coordinates:", path_y)  # Added for debugging
        ax.plot(path_x, path_y, 'b--', linewidth=2)  # Plot the path

    ax.set_xticks(range(cols))
    ax.set_yticks(range(rows))
    ax.set_xticklabels(range(cols))
    ax.set_yticklabels(range(rows))
    ax.grid()
    plt.show()