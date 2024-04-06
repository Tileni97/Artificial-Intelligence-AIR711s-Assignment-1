import networkx as nx
import matplotlib.pyplot as plt

def visualize_route(tsp, all_routes, final_route):
    """
    Visualize all possible routes and the chosen route using NetworkX.
    """
    # Create a graph
    G = nx.Graph()

    # Add nodes and edges for all possible routes
    for route in all_routes:
        for i in range(len(route) - 1):
            G.add_edge(route[i], route[i+1], weight=tsp.get_distance(route[i], route[i+1]))

    # Add nodes and edges for the final route
    for i in range(len(final_route) - 1):
        G.add_edge(final_route[i], final_route[i+1], weight=tsp.get_distance(final_route[i], final_route[i+1]))

    # Generate positions for nodes
    pos = nx.spring_layout(G)

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue', edgecolors='black', linewidths=2)

    # Draw edges for all possible routes
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='gray', alpha=0.3)

    # Draw edges for the final route
    nx.draw_networkx_edges(G, pos, edgelist=[(final_route[i], final_route[i+1]) for i in range(len(final_route) - 1)],
                           edge_color='blue', width=2)

    # Add labels for edges (distances)
    edge_labels = {(u, v): f"{tsp.get_distance(u, v)} km" for u, v in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='green')

    # Add labels for nodes
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    # Add starting point label
    starting_point = final_route[0]
    x, y = pos[starting_point]
    plt.text(x, y + 0.05, "Starting Point", fontsize=12, fontweight='bold', color='red', ha='center')

    # Add direction arrows manually
    for i in range(len(final_route) - 1):
        start_node = final_route[i]
        end_node = final_route[i+1]
        start_pos = pos[start_node]
        end_pos = pos[end_node]
        mid_pos = ((start_pos[0] + end_pos[0]) / 2, (start_pos[1] + end_pos[1]) / 2)
        dx = end_pos[0] - start_pos[0]
        dy = end_pos[1] - start_pos[1]
        plt.annotate("", xy=mid_pos, xytext=(mid_pos[0] - dx * 0.1, mid_pos[1] - dy * 0.1),
                     arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='maroon'))

    # Add title
    plt.title('TSP Routes')

    # Remove axis
    plt.axis('off')

    # Show plot
    plt.show()
