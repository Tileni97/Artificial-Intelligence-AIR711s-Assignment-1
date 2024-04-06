from tsp import TSP
from hill_climbing import hill_climbing
from comparison import compare_with_optimal
from visualization import visualize_route
from itertools import permutations
import random

# Define the places and distances
places = ["Dorado Park", "Khomasdal", "Katutura", "Eros", "Klein Windhoek"]
distances = [
    [0, 7, 20, 15, 12],
    [10, 0, 6, 14, 18],
    [20, 6, 0, 15, 30],
    [15, 14, 25, 0, 2],
    [12, 18, 30, 2, 0]
]

# Create an instance of the TSP problem
tsp = TSP(places, distances)

# Generate a random starting point
starting_point = random.choice(places)

# Generate all possible permutations of the places (excluding the starting point)
all_permutations = permutations([place for place in places if place != starting_point])

# Construct routes by adding the starting point at the beginning and end of each permutation
all_routes = []
for perm in all_permutations:
    route = [starting_point] + list(perm)
    all_routes.append(route)

# Solve the TSP problem using hill climbing algorithm
final_route, total_distance = hill_climbing(tsp)

# Add an edge from the last visited place to the starting point to ensure the loop
final_route.append(starting_point)

# Compare the solution with an optimal distance (if available)
optimal_distance = 100  # Placeholder for the optimal distance
compare_with_optimal(tsp, (final_route, total_distance), optimal_distance)

# Visualize the TSP routes
visualize_route(tsp, all_routes, final_route)
