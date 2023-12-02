import numpy as np
import random
import math
import time
import final_traffic_edge
# import new_adaptive
import dijkstra
import virtual_channel
import pandas as pd


linkdelay_list = []
hopcount_list = []
vcdelay_list = []
hopcountvirtual_list = []
waitdelay_list = []
totaldelay_list = []

for abc in range(0,100):


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
                    #print("inside function tf_link: ", tf_link)
                    # print(f"The amount of traffic genarated randomly in the link is : { tf_link}")
                    tf_link_bits = math.floor(tf_link)  # traffic generated randomly in bits
                    #print(f"The Current traffic in the link ( in terms of bits) : {tf_link_bits}")
                    available_bit_space = 64 - tf_link_bits

                    #print(f"The path is taken from node  {node1}  to node {node2}")
                    # print(f"The traffic present in path i,e node {node1} and node {node2} is {tf_link_bits}")
                    # print(f"The available space between node {node1} and node {node2} in bits is {available_bit_space}")
                    # print("")
                    # print("*"*100)

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

                # print(neighbors)

                return neighbors




            # Calculate total delay
            total_delay = 0.0
            total_traffic = 0.0


            for i in range(len(path) - 1):
                x1, y1 = path[i]
                x2, y2 = path[i + 1]
                node1 = nodes[x1][y1]
                node2 = nodes[x2][y2]
                data_generator = final_traffic_edge.generate_data()

                # packet_bits=int(input("Enter packets(in bits):"))
                t0_1, t1_0, t1_2, t2_1, t2_3, t3_2, t0_4, t4_0, t4_5, t5_4, t1_5, t5_1, t5_6, t6_5, t2_6, t6_2, t6_7, t7_6, t3_7, t7_3, t4_8, t8_4, t8_9, t9_8, t5_9, t9_5, t6_10, t10_6, t9_10, t10_9, t7_11, t11_7, t11_10, t10_11, t12_13, t13_12, t8_12, t12_8, t9_13, t13_9, t10_14, t14_10, t13_14, t14_13, t14_15, t15_14, t11_15, t15_11 = next(
                    data_generator)
                #print(t0_1)
                tf_link = eval(f"t{node1}_{node2}")
            

                
                available_bit_space = available(node1, node2,tf_link)
                neighbor_list = []
                value = []
                if n <= available_bit_space:
                    # print("Required space is available in the link and the data is sent ")
                    # print("")
                    # print("*"*100)
                    global hop_count
                    hop_count += 1
                    #global final_path
                    final_path.append(node2)
                    pass
                else:
                
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
        # print("Blocked_node is ",blocked_node)
        # print("Neighboring nodes are: ", value)

        adj = value                              # chumma instead of changing everything, keep like this only
        traffic_prediction = []
        for i in adj:
            
            coordinate = dict1[i]
            data_generator = final_traffic_edge.generate_data()
            #print(main.available(main.node1,i))
            t0_1, t1_0, t1_2, t2_1, t2_3, t3_2, t0_4, t4_0, t4_5, t5_4, t1_5, t5_1, t5_6, t6_5, t2_6, t6_2, t6_7, t7_6, t3_7, t7_3, t4_8, t8_4, t8_9, t9_8, t5_9, t9_5, t6_10, t10_6, t9_10, t10_9, t7_11, t11_7, t11_10, t10_11, t12_13, t13_12, t8_12, t12_8, t9_13, t13_9, t10_14, t14_10, t13_14, t14_13, t14_15, t15_14, t11_15, t15_11 = next(
                data_generator)
            #print(t0_1)
            tf_link = eval(f"t{src}_{i}")
            # print("node1 :",src)
            # print("node2: ",i)
            # print("tf_link :",tf_link)
        
            available_bit_space = available(src,i,tf_link)
            if available_bit_space >= n:
                traffic_prediction.append(1)
            else:
                traffic_prediction.append(0)
            # print("Traffic prediction list : ",traffic_prediction)

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

        # print("Possible next nodes : ", list(set(allow_adj)))
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
                # print("HOP COUNT ADAPTIVE : ",hop_count_adaptive)

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
                # print("HOP COUNT ADAPTIVE_xy : ",hop_count_adaptive_xy)
                next_xy_node_coordinate = []
                next_xy_node_coordinate = path[1]
                #print("next_xy_coordinate : ",next_xy_node_coordinate)
                for key,value in dict1.items():
                    if list(value) == next_xy_node_coordinate:
                        next_xy_node = key
                        #print("next_xy_node : ",next_xy_node)
                wait=0
                flag_wait_adaptive=0
                while((wait+hop_count_adaptive_xy)+1<=hop_count_adaptive and flag_wait_adaptive != 1):
                    data_generator = final_traffic_edge.generate_data()
                    t0_1, t1_0, t1_2, t2_1, t2_3, t3_2, t0_4, t4_0, t4_5, t5_4, t1_5, t5_1, t5_6, t6_5, t2_6, t6_2, t6_7, t7_6, t3_7, t7_3, t4_8, t8_4, t8_9, t9_8, t5_9, t9_5, t6_10, t10_6, t9_10, t10_9, t7_11, t11_7, t11_10, t10_11, t12_13, t13_12, t8_12, t12_8, t9_13, t13_9, t10_14, t14_10, t13_14, t14_13, t14_15, t15_14, t11_15, t15_11 = next(
                    data_generator)
                    tf_link = eval(f"t{blocked_node}_{next_xy_node}")   
                    available_space_adaptive_xy = available(blocked_node,next_xy_node,tf_link)
                    if(available_space_adaptive_xy < n):
                        wait += 1
                        #print("WAIT:",wait)

                    elif(available_space_adaptive_xy >= n):
                        final_next_node = next_xy_node
                        wait += 1
                        # print("WAIT:",wait)
                        # print("FINAL_XY_NODE from waiting : ",final_next_node)
                        # print("")
                        flag_wait_adaptive=1

                if(flag_wait_adaptive != 1):
                    new_next_node=next_node
                    global wait_delay
                    wait_delay += wait
                    # print("WAIT delay (adaptive if)",wait_delay)
                    final_path.append(new_next_node)
                    # print("FINAL_XY_NODE (adaptive) : ",new_next_node)
                    # print("")
                    xy_routing(new_next_node,dest,n)
                else:
                    #final_next_node=next_xy_node
                    #global wait_delay
                    wait_delay += wait
                    # print("WAIT delay (adaptive else)",wait_delay)
                    #print("")
                    final_path.append(final_next_node)
                    xy_routing(final_next_node,dest,n)
                
                global hop_count
                hop_count += 1
                
                allow_adj.clear()
                traffic_prediction.clear()
                #print("new next node",next_node)
                # print("allow_adj : empty",allow_adj)
                # while next_node != dest:
                #     #adaptive_route(next_node, main.dest)
                #     # main.xy_main(next_node, main.dest,main.n)
                    
                #     xy_routing(next_node, dest ,n)
                    
                #     break
                
        else:
            
            #virtual_channel.create_virtual_channel(src)
            #print("virtual channel")
            ack=virtual_channel.request()
            # print("Acknowledgemet is given, therefore flag value is "+str(ack))
            if(ack==1):

                vcNode=virtual_channel.create_virtual_channel(blocked_node,dest)

                vc_delay = virtual_channel.delay_vc(vcNode,dest)
                # print("VC DELAY (if): ",vc_delay)
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
                # print("SRC",src)
                # print("DEST : ",dest)
                # print("HOP COUNT XY : ",hop_count_xy)
                    
                flag_wait_virtual=0
                while((wait_or_not+hop_count_xy)+1  < vc_delay and (flag_wait_virtual!= 1)):
                    

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
                    #print("next_xy_coordinate : ",next_xy_node_coordinate)
                    for key,value in dict1.items():

                            if list(value) == next_xy_node_coordinate:
                                next_xy_node = key
                            #print("next_xy_node : ",next_xy_node)
                    data_generator = final_traffic_edge.generate_data()
                    t0_1, t1_0, t1_2, t2_1, t2_3, t3_2, t0_4, t4_0, t4_5, t5_4, t1_5, t5_1, t5_6, t6_5, t2_6, t6_2, t6_7, t7_6, t3_7, t7_3, t4_8, t8_4, t8_9, t9_8, t5_9, t9_5, t6_10, t10_6, t9_10, t10_9, t7_11, t11_7, t11_10, t10_11, t12_13, t13_12, t8_12, t12_8, t9_13, t13_9, t10_14, t14_10, t13_14, t14_13, t14_15, t15_14, t11_15, t15_11 = next(
                    data_generator)
                    tf_link = eval(f"t{src}_{next_xy_node}")   
                    available_space_xy = available(src,next_xy_node,tf_link)
                    if(available_space_xy < n):
                        wait_or_not += 1
                        #wait_delay += wait_or_not
                        # print("WAIT_OR_NOT:",wait_or_not)
                        #print("Wait delay(VC if)",wait_delay)

                    elif(available_space_xy >= n):
                        final_next_node = next_xy_node
                        #global hop_count
                        wait_or_not += 1
                        # print("WAIT_OR_NOT:",wait_or_not)
                        hop_count +=1
                        # print("FINAL_XY_NODE from waiting : ",final_next_node)
                        #wait_delay += wait_or_not
                        #print("Wait delay(VC elif)",wait_delay)
                        flag_wait_virtual=1
                    
                        
    





                wait_delay += wait_or_not
                #print("VC WAIT DELAY",wait_delay)
                if((wait_or_not+hop_count_xy)+1>vc_delay):
                    final_next_node = virtual_channel.create_virtual_channel(src,dest)
                    # print("FINAL NEXT NODE FROM VC : ",final_next_node)
                    global hop_count_virtual
                    hop_count_virtual +=1
                    
                
                    
                    
                        
                final_path.append(final_next_node)
                xy_routing(final_next_node,dest,n)

            else:
                print("virtual channel is occupied")
        # elif count_0 == len(traffic_prediction):
        #     vc()

            


    # Input
    src = 0 #int(input("Enter src node: "))
    dest = 15 #int(input("Enter dest node: "))
    n = 64 #int(input("Enter number of bits that you want to send between source node and destination node:"))
    final_path.append(src)
    # Nodes
    nodes = np.arange(0, 16).reshape(4, 4)
    # print("Network: \n", nodes)

    dict1 = {
        0: (0, 0), 1: (0, 1), 2: (0, 2), 3: (0, 3),
        4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (1, 3),
        8: (2, 0), 9: (2, 1), 10: (2, 2), 11: (2, 3),
        12: (3, 0), 13: (3, 1), 14: (3, 2), 15: (3, 3)
    }



    xy_routing(src, dest, n)

    linkdelay = delay_link*hop_count
    VCDelay = hop_count_virtual*1.4
    totaldelay = (linkdelay)+(VCDelay)+(wait_delay)

    linkdelay_list.append(linkdelay)
    hopcount_list.append(hop_count)
    vcdelay_list.append(VCDelay)
    hopcountvirtual_list.append(hop_count_virtual)
    waitdelay_list.append(wait_delay)
    totaldelay_list.append(totaldelay)
    # print(linkdelay_list)
    # print("*"*100)
    print("HOP_COUNT (normal link): ", hop_count)
    print("LINK_DELAY : ",linkdelay)
    print("HOP_COUNT (virtual) : ",hop_count_virtual)
    print("VC_DELAY : ", VCDelay)
    print("WAIT DELAY : ",wait_delay)
    x = "->".join(map(str,final_path))
    print("Final_path : ",x)
    print("TOTAL DELAY : ",totaldelay)
    print("\n\n")


    
    testingdata = pd.DataFrame({"Hop Count":hopcount_list, "link Delay":linkdelay_list, "Virtual Hop Count":hopcountvirtual_list, "VC Delay":vcdelay_list,"Wait Delay":waitdelay_list,"Total Delay":totaldelay_list})
    # {"Source":[0 for i in range(100)],"Destination":[15 for i in range(100)],"Packet Size":[15 for i in range(100)],


print(testingdata)
testingdata.to_csv("C:/Users/Deepa V/Documents/GitHub/Capstone-Project/TESTING/testfiles/Random_Traffic/0_to_15_bitsize_64_new_final_final.csv")
