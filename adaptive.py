import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
# import random
import math
import time
import final_traffic

def hello(source,destination,data_size):

    coordinates = {
    0: (0, 0), 1: (0, 1), 2: (0, 2), 3: (0, 3),
    4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (1, 3),
    8: (2, 0), 9: (2, 1), 10: (2, 2), 11: (2, 3),
    12: (3, 0), 13: (3, 1), 14: (3, 2), 15: (3, 3)
}
    # Define the grid graph

    G = nx.grid_2d_graph(4, 4)

    # Define the list of edges in the grid graph
    edges = list(G.edges())

    # Initialize all edges with a default traffic value
    default_traffic_value = 1
    for u, v in edges:
        G[u][v]['traffic'] = default_traffic_value

    # Custom weight function for Dijkstra's algorithm
    def custom_weight(u, v, d):
        return G[u][v].get('traffic', default_traffic_value)

    # Function to update traffic values in the graph
    def update_traffic_values(traffic_values):
        for (u, v), traffic in zip(edges, traffic_values):
            G[u][v]['traffic'] = traffic

    # Generate traffic values using the provided function
    '''def generate_random_traffic():
        # return np.uint64(2 ** np.random.randint(0, 40))
        return np.random.randint(0, 40)
    '''

    # Function to find and display the shortest path
    def find_shortest_path(source, destination):
        try:
            shortest_path = nx.shortest_path(G, source=source, target=destination, weight=custom_weight)
            print(f"Shortest path from {source} to {destination}: {shortest_path}")

            visualize_graph_with_path(G, pos, shortest_path)
        except nx.NetworkXNoPath:
            print(f"No path from {source} to {destination}")

    # Function to visualize the graph with highlighted shortest path
    def visualize_graph_with_path(G, pos, shortest_path):
        cmap = plt.get_cmap('coolwarm')

        # Create a list of edge colors based on traffic values
        edge_colors = [G[u][v]['traffic'] for u, v in edges]

        # Define a color for highlighting the shortest path (e.g., red)
        shortest_path_color = 'red'

        nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', edge_color=edge_colors, width=1,
                cmap=cmap)

        # Highlight the shortest path in red
        shortest_path_edges = list(zip(shortest_path, shortest_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=shortest_path_edges, edge_color=shortest_path_color, width=2)

        sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=min(edge_colors), vmax=max(edge_colors)))
        sm.set_array([])
        plt.colorbar(sm, label='Traffic Weight')
        plt.show()

    # Visualize the graph with edge colors representing traffic
    pos = {(x, y): (y, -x) for x, y in G.nodes()}
    cmap = plt.get_cmap('coolwarm')

    # Call the traffic generation function to determine traffic values
    traffic_values = [final_traffic.generate_random_traffic() for _ in range(len(edges))]
    update_traffic_values(traffic_values)
    

    # Print the traffic values used
    for i, traffic in enumerate(traffic_values):
        print(f'Traffic for edge {edges[i]}: {int(traffic):.2f}')

    # Define source and destination nodes
    # a = int(input("enter src node x: "))
    # b = int(input("enter src node y: "))
    # c = int(input("enter dst node x: "))
    # d = int(input("enter dst node y: "))
    # source = (a, b)
    # destination = (c, d)
    # print(source, destination)

    # Find and display the shortest path
    find_shortest_path(coordinates[source], coordinates[destination])
hello(0,15,3)