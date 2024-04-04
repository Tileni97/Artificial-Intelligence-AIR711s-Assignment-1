import hillClimbingAlg as hillclimbing # import the hill climbing algorithm
import visualization as visualize_route # import the visualization module

def main():
    tsp = [
        ['Dorado Park', [0, 10, 20, 15, 12]],
        ['Khomasdal', [7, 0, 6, 14, 18]],
        ['Katutura', [20, 6, 0, 25, 30]],
        ['Eros', [15, 14, 25, 0, 2]],
        ['Klein Whk', [12, 18, 30, 2, 0]]
    ]

    # Run hill climbing algorithm
    final_solution, final_route_length = hillclimbing.hillclimbing(tsp)

    # Extract places and initial route from tsp data
    places = [place[0] for place in tsp]
    initial_route = final_solution  # Initial route is the final solution

    # Visualize the routes
    visualize_route.visualize_route(places, initial_route, [], final_solution)

    print("Final Route:", final_solution)
    print("Final Route Length:", final_route_length)

if __name__ == "__main__":
    main()