import numpy as np
import random
import math
import time
#import random_traffic
# import adaptive_traffic
#import algorithm
import final_traffic
import new_adaptive
import dijkstra


dest_reached = False
# Delays
'''
n0_1 = 4
n1_0 = 4
n1_2 = 6.67
n2_1 = 6.67
n2_3 = 4
n3_2 = 4
n0_4 = 10
n4_0 = 10
n4_5 = 6.67
n5_4 = 6.67
n1_5 = 8.33
n5_1 = 8.33
n5_6 = 12.2
n6_5 = 12.2
n2_6 = 4.25
n6_2 = 4.25
n6_7 = 7.6
n7_6 = 7.6
n3_7 = 16.67
n7_3 = 16.67
n4_8 = 6.34
n8_4 = 6.34
n8_9 = 7.75
n9_8 = 7.75
n5_9 = 18.33
n9_5 = 18.33
n6_10 = 4
n10_6 = 4
n9_10 = 6.5
n10_9 = 6.5
n7_11 = 6.33
n11_7 = 6.33
n11_10 =  9.9
n10_11 = 9.9
n12_13 = 4
n13_12 = 4
n8_12 = 7.3
n12_8 = 7.3
n9_13 = 4
n13_9 = 4
n10_14 = 4.85714
n14_10 = 4.85714
n13_14 = 9.5
n14_13 = 9.5
n14_15 = 8.67
n15_14 = 8.67
n11_15 = 4.14286
n15_11 = 4.14286
'''

# Input
src = int(input("Enter src node: "))
dest = int(input("Enter dest node: "))
n = int(input("Enter number of bits that you want to send between source node and destination node:"))

# Nodes
nodes = np.arange(0, 16).reshape(4, 4)
print("Network: \n", nodes)

dict1 = {
    0: (0, 0), 1: (0, 1), 2: (0, 2), 3: (0, 3),
    4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (1, 3),
    8: (2, 0), 9: (2, 1), 10: (2, 2), 11: (2, 3),
    12: (3, 0), 13: (3, 1), 14: (3, 2), 15: (3, 3)
}

print("Node Assignment : \n", dict1)

# s = list(dict1[src])
# d = list(dict1[dest])

# print("Src Node coordinates = ", s, "\nDest Node = ", d)

# sx = s[0]
# sy = s[1]
# dx = d[0]
# dy = d[1]

# length = len(nodes)
# print("Length = ", length)

# # print("Path\n")

# path = []

# if sx < dx:
#     while sx < dx:
#         path.append([sx, sy])
#         sy += 1
# elif sx > dx:
#     while sx > dx:
#         path.append([sx, sy])
#         sy -= 1

# if sy < dy:
#     while sy < dy:
#         path.append([sx, sy])
#         sy += 1
# elif sy > dy:
#     while sy > dy:
#         path.append([sx, sy])
#         sy -= 1

# path.append([dx, dy])

#print("Path: ", path)

s = dict1[src]
d = dict1[dest]

print("Src Node coordinates = ", s, "\nDest Node = ", d)

sx, sy = s
dx, dy = d

path = []

if sy < dy:
    while sy < dy:
        path.append([sx, sy])
        sy += 1
        
elif sy > dy:
    while sy > dy:
        path.append([sx, sy])
        sy -= 1

if sy==dy and sx < dx:
    while sx < dx:
            path.append([sx, sy])
            sx += 1
elif sy==dy and sx > dx:
    while sx > dx:
            path.append([sx, sy])
            sx -= 1

path.append([dx, dy])




print("Path: ", path)

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




# Calculate total delay
total_delay = 0.0
total_traffic = 0.0

for i in range(len(path) - 1):
    x1, y1 = path[i]
    x2, y2 = path[i + 1]
    node1 = nodes[x1][y1]
    node2 = nodes[x2][y2]
    data_generator = final_traffic.generate_data()

    # packet_bits=int(input("Enter packets(in bits):"))
    t0_1, t1_0, t1_2, t2_1, t2_3, t3_2, t0_4, t4_0, t4_5, t5_4, t1_5, t5_1, t5_6, t6_5, t2_6, t6_2, t6_7, t7_6, t3_7, t7_3, t4_8, t8_4, t8_9, t9_8, t5_9, t9_5, t6_10, t10_6, t9_10, t10_9, t7_11, t11_7, t11_10, t10_11, t12_13, t13_12, t8_12, t12_8, t9_13, t13_9, t10_14, t14_10, t13_14, t14_13, t14_15, t15_14, t11_15, t15_11 = next(
        data_generator)
    # print(t0_1)

    def available(node1, node2):
        tf_link = eval(f"t{node1}_{node2}")  # value
        # print(f"The amount of traffic genarated randomly in the link is : { tf_link}")
        tf_link_bits = math.floor(tf_link)  # traffic generated randomly in bits
        print(f"The Current traffic in the link ( in terms of bits) : {tf_link_bits}")
        available_bit_space = 64 - tf_link_bits

        print(f"The path is taken from node  {node1}  to node {node2}")
        print(f"The traffic present in path i,e node {node1} and node {node2} is {tf_link_bits}")
        print(f"The available space between node {node1} and node {node2} in bits is {available_bit_space}")

        return available_bit_space
    available_bit_space = available(node1, node2)
    neighbor_list = []
    value = []
    if n < available_bit_space:
        print("Required space is available in the link and the data is sent ")
        pass
    else:
        print(" Required space is not available in the link so take adaptive routing")
        #adaptive.hello(node1,dest,n)
        #algorithm.find_shortest_path_with_min_traffic(node1, dest, n)
        # new_adaptive.adaptive_route(node1, dest)

        neighbor_list = get_neighbors(dict1[node1],4,4)
        for final_node in neighbor_list:
             #print(final_node)
             for i in dict1 :
                
                 if dict1[i] == final_node:
                      value.append(i)
                      
        value.remove(node2)
        new_adaptive.adaptive_route(node1, dest)
        # dijkstra.print_paths(node1, dest, value)
        break
        #adaptive.hello(node1,dest,n)

    # delay = eval(f"n{node1}_{node2}")
    # total_delay += delayF

# if (node2 == dest):
# #print("Traffic:",total_traffic)
#     print("Total Delay: ", total_delay)
# else:
#     print(f"Destination could not be reached, Total Delay=??")