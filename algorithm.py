#import adaptive_traffic
#import random_traffic
import math
import final_traffic
import adaptive


def dijkstra_algorithm(graph, src, dest, traffic_dict):
    # Create a dictionary to store the shortest distance to each node
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[src] = 0

    # Create a dictionary to store the previous node in the shortest path
    previous_nodes = {}

    # Create a set of unvisited nodes
    unvisited_nodes = set(graph)

    # traffic_generator = adaptive_traffic.generate_data()

    while unvisited_nodes:
        # Select the node with the smallest distance
        current_node = min(unvisited_nodes, key=lambda node: shortest_distances[node])

        # If the current node is the destination, construct the shortest path
        if current_node == dest:
            path = []
            while current_node is not None:
                path.insert(0, current_node)
                current_node = previous_nodes.get(current_node)
            return path

        # Mark the current node as visited
        unvisited_nodes.remove(current_node)

        # Update distances to neighboring nodes
        for neighbor in graph[current_node]:
            if neighbor in unvisited_nodes:
                link_name = f"t{current_node}_{neighbor}"
                # print(current_node)
                traffic_weight = math.floor((traffic_dict.get(link_name, 1)))  # Default to 1 if traffic data not found
                distance = shortest_distances[current_node] + traffic_weight
                # If this path is shorter, update the distance and previous node
                if distance < shortest_distances[neighbor]:
                    shortest_distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    print("link_name: " + str(link_name) + " " + "traffic_present: " + str(
                        traffic_weight))  # +"distance: "+" "+str(distance)+" "+"current_node: "+str(current_node)
                    # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    return []

    # If no path is found, return an empty list


def find_shortest_path_with_min_traffic(src, dest, n):
    graph = {
        0: [1, 4],
        1: [0, 2, 5],
        2: [1, 3, 6],
        3: [2, 7],
        4: [0, 5, 8],
        5: [1, 4, 6, 9],
        6: [2, 5, 7, 10],
        7: [3, 6, 11],
        8: [4, 9, 12],
        9: [5, 8, 10, 13],
        10: [6, 9, 11, 14],
        11: [7, 10, 15],
        12: [8, 13],
        13: [9, 12, 14],
        14: [10, 13, 15],
        15: [11, 14]
    }

    # Define the order of link names
    static_traffic = final_traffic.generate_data()
    # shortest_path = dijkstra_algorithm(graph, src, dest,tr)
    link_names = [
        "t0_1", "t1_0", "t1_2", "t2_1", "t2_3", "t3_2", "t0_4", "t4_0", "t4_5",
        "t5_4", "t1_5", "t5_1", "t5_6", "t6_5", "t2_6", "t6_2", "t6_7", "t7_6",
        "t3_7", "t7_3", "t4_8", "t8_4", "t8_9", "t9_8", "t5_9", "t9_5", "t6_10",
        "t10_6", "t9_10", "t10_9", "t7_11", "t11_7", "t11_10", "t10_11", "t12_13",
        "t13_12", "t8_12", "t12_8", "t9_13", "t13_9", "t10_14", "t14_10", "t13_14",
        "t14_13", "t14_15", "t15_14", "t11_15", "t15_11"
    ]
    traffic_data = next(static_traffic)
    traffic_dict = dict(zip(link_names, map(int, traffic_data)))
    shortest_path = dijkstra_algorithm(graph, src, dest, traffic_dict)
    if shortest_path:
        print("Shortest path with minimal traffic:", shortest_path)
        # Check if the packet can be transmitted through the shortest path
        total_packet_size = n
        # remaining_packet_size = n

        for i in range(len(shortest_path) - 1):
            node1 = shortest_path[i]
            node2 = shortest_path[i + 1]

            link_name = f"t{node1}_{node2}"
            traffic_weight = math.floor((traffic_dict.get(link_name, 1)))  # Default to 1 if traffic data not found
            available_bit_space = 64 - traffic_weight

            if total_packet_size <= available_bit_space:
                print(f"Traffic present at {link_name}: {traffic_weight}")
                print(f"Packet transmitted through link {link_name}.")
                if node2 == dest:
                    print("The packets have reached the destination node using DIJKSTRA Path  ")

            else:
                print(f"Traffic present at {link_name}: {traffic_weight}")
                print(f"Packet could not be transmitted due to less space: {available_bit_space} < packet_size: {n}")
                print("MAKE DIJKSTRA ADAPTIVE !!!!")
                adaptive.hello()
                break
    else:
        print("No path found.")