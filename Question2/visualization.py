import matplotlib.pyplot as plt

def plot_route(places, route, title): # Function to plot the route
    plt.figure(figsize=(8, 6))

    # Plot places
    for place in places:
        plt.plot(place[0], place[1], 'ko')  # 'ko' represents black dots for places

    # Plot route
    for i in range(len(route) - 1): # Iterate over all places except the last one
        plt.plot([places[route[i]][0], places[route[i + 1]][0]], [places[route[i]][1], places[route[i + 1]][1]], 'b-')
    plt.plot([places[route[-1]][0], places[route[0]][0]], [places[route[-1]][1], places[route[0]][1]],
             'b-')  # Connect last place to first place

    plt.title('Windhoek')
    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')
    plt.grid(True)
    plt.show()

def visualize_route(places, initial_route, intermediate_routes, final_route): # Function to visualize the route
    if initial_route:
        plot_route(places, initial_route, 'Initial Route')

    for i, route in enumerate(intermediate_routes): # Iterate over all intermediate routes
        plot_route(places, route, f'Intermediate Route {i + 1}')

    plot_route(places, final_route, 'Final Route') # Plot the final route
