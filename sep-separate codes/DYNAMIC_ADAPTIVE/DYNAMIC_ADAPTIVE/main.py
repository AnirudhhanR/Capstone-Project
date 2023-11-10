import numpy as np
import random
import math
import time
import final_traffic
# import new_adaptive
import dijkstra
x = True
while x:
    try:
            delay_link = 1
            delay_virtual = 1.4
            hop_count = 0
            final_path = []
            dest_reached = False
            temp = -1
            wait=0
            def available(node1, node2,tf_link):
                            # node_traffic(path)
                            #tf_link = eval(f"t{node1}_{node2}")  # value
                           # print("inside function tf_link: ", tf_link)
                            # print(f"The amount of traffic genarated randomly in the link is : { tf_link}")
                            tf_link_bits = math.floor(tf_link)  # traffic generated randomly in bits
                           # print(f"The Current traffic in the link ( in terms of bits) : {tf_link_bits}")
                            available_bit_space = 64 - tf_link_bits

                            print("")
                            print(f"The traffic present in path i,e node {node1} and node {node2} is {tf_link_bits}")
                            print(f"The available space between node {node1} and node {node2} in bits is {available_bit_space}")

                            return available_bit_space

            def xy_routing(src, dest, n):
                if(src!=dest):
                    s = dict1[src]
                    d = dict1[dest]
                    
                    
                    #print("Src Node coordinates = ", s, "\nDest Node = ", d)

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




                    #print("Path: ", path)



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

                        #print(neighbors)

                        return neighbors




                    # Calculate total delay
                    total_delay = 0.0
                    total_traffic = 0.0


                    for i in range(len(path)-1):
                        x1, y1 = path[i]
                        x2, y2 = path[i + 1]
                        node1 = nodes[x1][y1]
                        node2 = nodes[x2][y2]
                        data_generator = final_traffic.generate_data()

                        # packet_bits=int(input("Enter packets(in bits):"))
                        t0_1, t1_0, t1_2, t2_1, t2_3, t3_2, t0_4, t4_0, t4_5, t5_4, t1_5, t5_1, t5_6, t6_5, t2_6, t6_2, t6_7, t7_6, t3_7, t7_3, t4_8, t8_4, t8_9, t9_8, t5_9, t9_5, t6_10, t10_6, t9_10, t10_9, t7_11, t11_7, t11_10, t10_11, t12_13, t13_12, t8_12, t12_8, t9_13, t13_9, t10_14, t14_10, t13_14, t14_13, t14_15, t15_14, t11_15, t15_11 = next(
                            data_generator)
                        #print(t0_1)
                        tf_link = eval(f"t{node1}_{node2}")
                        #print("node1 :",node1)
                        #print("node2: ",node2)
                        #print("tf_link :",tf_link)
                        
                        # def available(node1, node2,tf_link):
                        #         # node_traffic(path)
                        #         #tf_link = eval(f"t{node1}_{node2}")  # value
                        #         print("inside function tf_link: ", tf_link)
                        #         # print(f"The amount of traffic genarated randomly in the link is : { tf_link}")
                        #         tf_link_bits = math.floor(tf_link)  # traffic generated randomly in bits
                        #         print(f"The Current traffic in the link ( in terms of bits) : {tf_link_bits}")
                        #         available_bit_space = 64 - tf_link_bits

                        #         print(f"The path is taken from node  {node1}  to node {node2}")
                        #         print(f"The traffic present in path i,e node {node1} and node {node2} is {tf_link_bits}")
                        #         print(f"The available space between node {node1} and node {node2} in bits is {available_bit_space}")

                        #         return available_bit_space

                        
                        available_bit_space = available(node1, node2,tf_link)
                        neighbor_list = []
                        value = []
                        if n <= available_bit_space:
                            print("")
                            print("Required space is available in the link and the data is sent ")
                            print("")
                            print("-"*60)
                            global hop_count
                            hop_count += 1
                            #global final_path
                            final_path.append(node2)
                            pass
                        else:
                            print("")
                            print("Required space is not available in the link so take adaptive routing")
                            print("")
                            print("-"*60)
                            print("")
                            #adaptive.hello(node1,dest,n)
                            #algorithm.find_shortest_path_with_min_traffic(node1, dest, n)
                            # new_adaptive.adaptive_route(node1, dest)
                            global temp
                            index_node1 = final_path.index(node1)
                            temp = final_path[index_node1-1]
                            neighbor_list = get_neighbors(dict1[node1],4,4)
                            for final_node in neighbor_list:
                                #print(final_node)
                                for i in dict1 :
                                    
                                    if dict1[i] == final_node:
                                        value.append(i)
                                        
                            value.remove(node2)
                            if temp in value:
                                
                                value.remove(temp)
                            value = sorted(value)
                            #print("previous node is removed:")
                            #print("final value list : ",value)
                            adaptive_route(node1,dest, n, value)
                            # dijkstra.print_paths(node1, dest, value)
                            break
                        #adaptive.hello(node1,dest,n)
            def adaptive_route(src,dest,n,value):

                dict1 = {
                    0: (0, 0), 1: (0, 1), 2: (0, 2), 3: (0, 3),
                    4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (1, 3),
                    8: (2, 0), 9: (2, 1), 10: (2, 2), 11: (2, 3),
                    12: (3, 0), 13: (3, 1), 14: (3, 2), 15: (3, 3)
                }

                blocked_node = src
                print("*"*30)
                print("blocked_node is ",blocked_node)
                print("neighboring nodes are: ", value)
                print("*"*30)

                adj = value                              # chumma instead of changing everything, keep like this only
                traffic_prediction = []
                for i in adj:
                    #print("IN ADAPTIVE")
                    coordinate = dict1[i]
                    data_generator = final_traffic.generate_data()
                    #print(main.available(main.node1,i))
                    t0_1, t1_0, t1_2, t2_1, t2_3, t3_2, t0_4, t4_0, t4_5, t5_4, t1_5, t5_1, t5_6, t6_5, t2_6, t6_2, t6_7, t7_6, t3_7, t7_3, t4_8, t8_4, t8_9, t9_8, t5_9, t9_5, t6_10, t10_6, t9_10, t10_9, t7_11, t11_7, t11_10, t10_11, t12_13, t13_12, t8_12, t12_8, t9_13, t13_9, t10_14, t14_10, t13_14, t14_13, t14_15, t15_14, t11_15, t15_11 = next(
                        data_generator)
                    #print(t0_1)
                    tf_link = eval(f"t{src}_{i}")
                    #print("node1 :",src)
                   ##print("tf_link :",tf_link)
                
                    available_bit_space = available(src,i,tf_link)
                    if available_bit_space >= n:
                        traffic_prediction.append(1)
                    else:
                        traffic_prediction.append(0)
                        print("")
                    print("traffic prediction list= ",traffic_prediction)

                count_1 = 0
                count_0 = 0
                for i in range(len(traffic_prediction)):
                    if traffic_prediction[i] == 1:
                        count_1 += 1
                    elif traffic_prediction[i] == 0:
                        count_0 += 1



                #traffic_prediction = [1,0]
                allow_adj = []
                for j in range(len(adj)):
                    if traffic_prediction[0] == 1 and adj[0] == 0:
                        allow_adj.append(0)
                    if adj[j]*traffic_prediction[j] != 0:
                        # print("adj[j] : ",adj[j])
                        # print("traffic_prediction[j] : ",traffic_prediction[j])
                        allow_adj.append(adj[j]*traffic_prediction[j])

               # print("allow_adj ", list(set(allow_adj)))
                # if count_1 <= len(traffic_prediction):
                #     dijkstra.print_paths(main.node1, main.dest, allow_adj)

                if len(allow_adj) !=0:
                    if(src!=dest):
                        next_node = dijkstra.print_paths(src, dest, list(set(allow_adj)))
                        allow_adj.clear()
                        traffic_prediction.clear()
                        global hop_count
                        hop_count += 1
                       # print("allow_adj : empty",allow_adj)
                        final_path.append(next_node)
                        if next_node != dest:
                            #print("hello")
                            xy_routing(next_node, dest,n)        
                else:
                    data_generator = final_traffic.generate_data()
                    t0_1,t1_0,t1_2,t2_1,t2_3,t3_2,t0_4,t4_0,t4_5,t5_4,t1_5,t5_1,t5_6,t6_5,t2_6,t6_2,t6_7,t7_6,t3_7,t7_3,t4_8,t8_4,t8_9,t9_8,t5_9,t9_5,t6_10,t10_6,t9_10,t10_9,t7_11,t11_7,t11_10,t10_11,t12_13,t13_12,t8_12,t12_8,t9_13,t13_9,t10_14,t14_10,t13_14,t14_13,t14_15,t15_14,t11_15,t15_11 = next(data_generator)
                    #tf_link=eval(f"t{src}_{}") 
                    
                    #tf_link_bits=math.floor(math.log2(tf_link))
                    global wait
                    wait += 1
                    print("WAIT",wait)
                    adaptive_route(src,dest,n,value)
                

           

            # Input
            src = int(input("Enter src node: "))
            dest = int(input("Enter dest node: "))
            n = int(input("Enter number of bits that you want to send between source node and destination node:"))
            final_path.append(src)
            # Nodes
            nodes = np.arange(0, 16).reshape(4, 4)
            print("Network: \n", nodes)

            dict1 = {
                0: (0, 0), 1: (0, 1), 2: (0, 2), 3: (0, 3),
                4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (1, 3),
                8: (2, 0), 9: (2, 1), 10: (2, 2), 11: (2, 3),
                12: (3, 0), 13: (3, 1), 14: (3, 2), 15: (3, 3)
            }

         

            
            xy_routing(src, dest, n)

            x = "->".join(map(str,final_path))
            print("Final_path : ",x)
            print(f"WAIT DELAY : {wait} Cycles")


            delay = len(final_path)-1
            total_delay = hop_count + wait
            print(f"FINAL DELAY : {total_delay} Cycles")
            break


           
    except:
            print("Entered except")
        
            print("DEADLOCK!")
            break