import random

def generate_initial_route(tsp):
    """
    Generate a random initial route visiting all places.
    """
    return random.sample(tsp.places, len(tsp.places))

def get_total_distance(route, tsp):
    """
    Calculate the total distance of a route visiting all places.
    """
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += tsp.get_distance(route[i], route[i + 1])
    total_distance += tsp.get_distance(route[-1], route[0])  # Return to starting point
    return total_distance

def explore_neighbours(route):
    """
    Explore neighbouring solutions by swapping the order of two randomly chosen places in the route.
    """
    new_route = route.copy()
    i, j = random.sample(range(len(route)), 2)
    new_route[i], new_route[j] = new_route[j], new_route[i]
    return new_route

def hill_climbing(tsp, max_iterations=1000):
    """
    Solve the TSP problem using the hill climbing algorithm.
    """
    current_route = generate_initial_route(tsp)
    current_distance = get_total_distance(current_route, tsp)
    
    for _ in range(max_iterations):
        neighbour_route = explore_neighbours(current_route)
        neighbour_distance = get_total_distance(neighbour_route, tsp)
        
        if neighbour_distance < current_distance:
            current_route = neighbour_route
            current_distance = neighbour_distance
    
    return current_route, current_distance
