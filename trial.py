import numpy as np
import random
import math
import time
import final_traffic
# import new_adaptive
import dijkstra
import virtual_channel

delay_link = 1
delay_virtual = 1.4
hop_count = 0
final_path = []
dest_reached = False
temp = -1
hop_count_virtual = 0
wait_delay = 0
def available(node1, node2,tf_link):
                # node_traffic(path)
                #tf_link = eval(f"t{node1}_{node2}")  # value
                print("inside function tf_link: ", tf_link)
                # print(f"The amount of traffic genarated randomly in the link is : { tf_link}")
                tf_link_bits = math.floor(tf_link)  # traffic generated randomly in bits
                print(f"The Current traffic in the link ( in terms of bits) : {tf_link_bits}")
                available_bit_space = 64 - tf_link_bits

                print(f"The path is taken from node  {node1}  to node {node2}")
                print(f"The traffic present in path i,e node {node1} and node {node2} is {tf_link_bits}")
                print(f"The available space between node {node1} and node {node2} in bits is {available_bit_space}")

                return available_bit_space

def xy_routing(src, dest, n):
    if(src!=dest):
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
            #print(t0_1)
            tf_link = eval(f"t{node1}_{node2}")
            print("node1 :",node1)
            print("node2: ",node2)
            print("tf_link :",tf_link)
            
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
                print("Required space is available in the link and the data is sent ")
                global hop_count
                hop_count += 1
                #global final_path
                final_path.append(node2)
                pass
            else:
                print(" Required space is not available in the link so take adaptive routing")
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
                    #print(value)
                    value.remove(temp)
                value = sorted(value)
                #print("previous node is removed:")
                print("final value list : ",value)
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
    print("blocked_node is ",blocked_node)
    print("neighboring nodes are: ", value)

    adj = value                              # chumma instead of changing everything, keep like this only
    traffic_prediction = []
    for i in adj:
        print("in new adaptive")
        coordinate = dict1[i]
        data_generator = final_traffic.generate_data()
        #print(main.available(main.node1,i))
        t0_1, t1_0, t1_2, t2_1, t2_3, t3_2, t0_4, t4_0, t4_5, t5_4, t1_5, t5_1, t5_6, t6_5, t2_6, t6_2, t6_7, t7_6, t3_7, t7_3, t4_8, t8_4, t8_9, t9_8, t5_9, t9_5, t6_10, t10_6, t9_10, t10_9, t7_11, t11_7, t11_10, t10_11, t12_13, t13_12, t8_12, t12_8, t9_13, t13_9, t10_14, t14_10, t13_14, t14_13, t14_15, t15_14, t11_15, t15_11 = next(
            data_generator)
        #print(t0_1)
        tf_link = eval(f"t{src}_{i}")
        print("node1 :",src)
        print("node2: ",i)
        print("tf_link :",tf_link)
    
        available_bit_space = available(src,i,tf_link)
        if available_bit_space >= n:
            traffic_prediction.append(1)
        else:
            traffic_prediction.append(0)
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

    print("allow_adj ", list(set(allow_adj)))
    # if count_1 <= len(traffic_prediction):
    #     dijkstra.print_paths(main.node1, main.dest, allow_adj)

    if len(allow_adj) !=0:
        if(src!=dest):
            next_node = dijkstra.print_paths(src, dest, list(set(allow_adj)))
            s = dict1[next_node]
            d = dict1[dest]

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
            hop_count_adaptive = len(path)
            print("HOP COUNT ADAPTIVE : ",hop_count_adaptive)

            s = dict1[blocked_node]
            d = dict1[dest]

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
            hop_count_adaptive_xy = len(path) -1
            print("HOP COUNT ADAPTIVE_xy : ",hop_count_adaptive_xy)
            next_xy_node_coordinate = []
            next_xy_node_coordinate = path[1]
            print("next_xy_coordinate : ",next_xy_node_coordinate)
            for key,value in dict1.items():
                if list(value) == next_xy_node_coordinate:
                    next_xy_node = key
                    print("next_xy_node : ",next_xy_node)
            wait=0
            flag_wait_adaptive=0
            while(((wait+hop_count_adaptive_xy)+1)<=(hop_count_adaptive) and flag_wait_adaptive != 1):
                data_generator = final_traffic.generate_data()
                t0_1, t1_0, t1_2, t2_1, t2_3, t3_2, t0_4, t4_0, t4_5, t5_4, t1_5, t5_1, t5_6, t6_5, t2_6, t6_2, t6_7, t7_6, t3_7, t7_3, t4_8, t8_4, t8_9, t9_8, t5_9, t9_5, t6_10, t10_6, t9_10, t10_9, t7_11, t11_7, t11_10, t10_11, t12_13, t13_12, t8_12, t12_8, t9_13, t13_9, t10_14, t14_10, t13_14, t14_13, t14_15, t15_14, t11_15, t15_11 = next(
                data_generator)
                tf_link = eval(f"t{blocked_node}_{next_xy_node}")   
                available_space_adaptive_xy = available(blocked_node,next_xy_node,tf_link)
                if(available_space_adaptive_xy < n):
                    wait += 1
                    print("WAIT:",wait)

                elif(available_space_adaptive_xy >= n):
                    final_next_node = next_xy_node
                    wait += 1
                    print("WAIT: ",wait)
                    print("FINAL_XY_NODE from waiting : ",final_next_node)
                    flag_wait_adaptive=1

            if(flag_wait_adaptive != 1):
                new_next_node=next_node
                global wait_delay
                #wait_delay += wait
                final_path.append(new_next_node)
                xy_routing(new_next_node,dest,n)
            else:
                #final_next_node=next_xy_node
                #global wait_delay
                #wait_delay += wait
                final_path.append(final_next_node)
                xy_routing(final_next_node,dest,n)
            wait_delay += wait
            global hop_count
            hop_count += 1
            
            allow_adj.clear()
            traffic_prediction.clear()
            #print("new next node",next_node)
            print("allow_adj : empty",allow_adj)
            # while next_node != dest:
            #     #adaptive_route(next_node, main.dest)
            #     # main.xy_main(next_node, main.dest,main.n)
                
            #     xy_routing(next_node, dest ,n)
                
            #     break
             
    else:
        
        #virtual_channel.create_virtual_channel(src)
        print("virtual channel")
        ack=virtual_channel.request()
        print("Acknowledgemet is given, therefore flag value is "+str(ack))
        if(ack==1):

            vcNode=virtual_channel.create_virtual_channel(blocked_node)
            vc_delay = 4.4
            #******
            wait_or_not = 0
            
            s = dict1[src]
            d = dict1[dest]

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
            hop_count_xy = len(path)-1
            print("SRC",src)
            print("DEST : ",dest)
            print("HOP COUNT XY : ",hop_count_xy)
                
            flag_wait_virtual=0
            while(((wait_or_not+hop_count_xy)+1)  < (vc_delay) and (flag_wait_virtual!= 1)):
                

                s = dict1[src]
                d = dict1[dest]

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
                
                next_xy_node_coordinate = []
                next_xy_node_coordinate = path[1]
                print("next_xy_coordinate : ",next_xy_node_coordinate)
                for key,value in dict1.items():

                        if list(value) == next_xy_node_coordinate:
                          next_xy_node = key
                          print("next_xy_node : ",next_xy_node)
                data_generator = final_traffic.generate_data()
                t0_1, t1_0, t1_2, t2_1, t2_3, t3_2, t0_4, t4_0, t4_5, t5_4, t1_5, t5_1, t5_6, t6_5, t2_6, t6_2, t6_7, t7_6, t3_7, t7_3, t4_8, t8_4, t8_9, t9_8, t5_9, t9_5, t6_10, t10_6, t9_10, t10_9, t7_11, t11_7, t11_10, t10_11, t12_13, t13_12, t8_12, t12_8, t9_13, t13_9, t10_14, t14_10, t13_14, t14_13, t14_15, t15_14, t11_15, t15_11 = next(
                data_generator)
                tf_link = eval(f"t{src}_{next_xy_node}")   
                available_space_xy = available(src,next_xy_node,tf_link)
                if(available_space_xy < n):
                    wait_or_not += 1
                    print("WAIT_OR_NOT:",wait_or_not)

                elif(available_space_xy >= n):
                    final_next_node = next_xy_node
                    #global hop_count
                    wait_or_not += 1
                    print("WAIT_OR_NOT:",wait_or_not)
                    hop_count +=1
                    print("FINAL_XY_NODE from waiting : ",final_next_node)
                    #wait_delay += wait_or_not
                    flag_wait_virtual=1
                
                    
 






            if(((wait_or_not+hop_count_xy)+1)>(vc_delay)):
                final_next_node = virtual_channel.create_virtual_channel(src)
                print("FINAL NEXT NODE FROM VC : ",final_next_node)
                global hop_count_virtual
                hop_count_virtual +=1
                
            
                
                
            wait_delay += wait_or_not         
            final_path.append(final_next_node)
            xy_routing(final_next_node,dest,n)











            #global final_path
            # final_path.append(vcNode)
            # xy_routing(vcNode,dest,n)
            #total_delay+=1.414213562
            #print(total_delay)
        else:
            print("virtual channel is occupied")
    # elif count_0 == len(traffic_prediction):
    #     vc()

        
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




    # delay = eval(f"n{node1}_{node2}")
    # total_delay += delayF

# if (node2 == dest):
# #print("Traffic:",total_traffic)
#     print("Total Delay: ", total_delay)
# else:
#     print(f"Destination could not be reached, Total Delay=??")

xy_routing(src, dest, n)
print("HOP_COUNT (normal link): ", hop_count)
print("LINK_DELAY : ",delay_link*hop_count)
print("HOP_COUNT (virtual) : ",hop_count_virtual)
print("VC_DELAY : ", hop_count_virtual*1.4)
print("WAIT DELAY : ",wait_delay)
x = "->".join(map(str,final_path))
print("Final_path : ",x)
print("TOTAL DELAY : ",(delay_link*hop_count)+(hop_count_virtual*1.4)+(wait_delay))



'''
wait(1,2)
    generate
    time.sleep()


'''