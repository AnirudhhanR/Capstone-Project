import random
import heapq

# Define the size of the mesh topology
rows = 4
columns = 4

# Initialize an empty 2D array to represent the links and traffic
#traffic = [[0] * columns for _ in range(rows)]

# Initialize congestion factors for each link
#congestion_factors = [[1.0] * columns for _ in range(rows)]

# Generate random traffic for adjacent links
'''for i in range(rows):
    for j in range(columns):
        # Initialize traffic for all links as zero
        top_traffic = random.randint(0, 100)
        bottom_traffic = random.randint(0, 100)
        left_traffic = random.randint(0, 100)
        right_traffic = random.randint(0, 100)

        # Apply congestion factors
        top_traffic *= congestion_factors[i][j]
        bottom_traffic *= congestion_factors[i][j]
        left_traffic *= congestion_factors[i][j]
        right_traffic *= congestion_factors[i][j]

        # Compare traffic for adjacent links and store the minimum
        traffic[i][j] = min(top_traffic, bottom_traffic, left_traffic, right_traffic)'''

# Define source and destination nodes
source = (2, 2)
destination = (0, 3)

# Function to calculate traffic from a node to its adjacent nodes considering congestion
def calculate_traffic_from_node(node):
    i, j = node
    adjacent_nodes = []

    if i > 0:
        adjacent_nodes.append(((i - 1, j), "Top"))
    if i < rows - 1:
        adjacent_nodes.append(((i + 1, j), "Bottom"))
    if j > 0:
        adjacent_nodes.append(((i, j - 1), "Left"))
    if j < columns - 1:
        adjacent_nodes.append(((i, j + 1), "Right"))

    '''print(f"Traffic from node {node} to adjacent nodes ")
    for neighbor, direction in adjacent_nodes:
        traffic_value = traffic[neighbor[0]][neighbor[1]]
        congestion_factor = congestion_factors[neighbor[0]][neighbor[1]]
        adjusted_traffic = traffic_value * congestion_factor
        print(f"To node {neighbor} ({direction} link): {adjusted_traffic}")'''

# Calculate and print traffic for every node in the mesh considering congestion
for i in range(rows):
    for j in range(columns):
        calculate_traffic_from_node((i, j))

# Function to find the least congested path using Dijkstra's algorithm
# def dijkstra_with_congestion(source, destination, traffic, congestion_factors):
#     rows = len(traffic)
#     columns = len(traffic[0])

    # Initialize distances with infinity, except for the source node (distance = 0)
''' distances = [[float('inf')] * columns for _ in range(rows)]
    distances[source[0]][source[1]] = 0

    # Initialize priority queue with the source node
    queue = [(0, source)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == destination:
            return distances

        for neighbor in get_neighbors(current_node, rows, columns):
            i, j = neighbor
            traffic_value = traffic[i][j]
            congestion_factor = congestion_factors[i][j]
            adjusted_traffic = traffic_value * congestion_factor
            distance = current_distance + adjusted_traffic

            if distance < distances[i][j]:
                distances[i][j] = distance
                heapq.heappush(queue, (distance, neighbor))

    return None'''

# Function to get valid neighbors
def get_neighbors(node, rows, columns):
    i, j = node
    neighbors = []

    if i > 0:
        neighbors.append((i - 1, j))
    if i < rows - 1:
        neighbors.append((i + 1, j))
    if j > 0:
        neighbors.append((i, j - 1))
    if j < columns - 1:
        neighbors.append((i, j + 1))

    print(neighbors)

    return neighbors
    

# Find the least congested path and distances using Dijkstra's algorithm
'''distances = dijkstra_with_congestion(source, destination, traffic, congestion_factors)

if distances is not None:
    print(f"Least Congested Path from {source} to {destination}:")

    current_node = destination
    path = [current_node]

    while current_node != source:
        i, j = current_node
        neighbors = get_neighbors(current_node, rows, columns)
        min_neighbor = min(neighbors, key=lambda node: distances[node[0]][node[1]])
        path.append(min_neighbor)
        current_node = min_neighbor

    path.reverse()

    total_congestion = sum(traffic[i][j] * congestion_factors[i][j] for i, j in path)

    for i in range(len(path) - 1):
        node1 = path[i]
        node2 = path[i + 1]
        traffic_value = traffic[node1[0]][node1[1]]
        congestion_factor = congestion_factors[node1[0]][node1[1]]
        adjusted_traffic = traffic_value * congestion_factor
        print(f"{node1} to {node2} ")

    print(f"Destination reached")
else:
    print(f"No path found from {source} to {destination}.")'''

get_neighbors([1,2],rows,columns)