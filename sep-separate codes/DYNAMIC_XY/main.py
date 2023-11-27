import numpy as np
import random
import math
import time
from traffic_generation import generate_data
import pandas as pd
totaldelay_list = []
hopcount_list = []
for ghi in range(100):
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

    # Input
    final_path = []
    src = 0 # int(input("Enter src node: "))
    dest = 15 # int(input("Enter dest node: "))
    n = 5 # int(input("Enter number of bits that you want to send between source node and destination node:"))
    delay = 0
    # Nodes
    nodes = np.arange(0, 16).reshape(4, 4)
    # print("Network: \n", nodes)
    final_path.append(src)
    wait  = 0
    dict1 = {
            0: (0, 0), 1: (0, 1), 2: (0, 2), 3: (0, 3),
            4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (1, 3),
            8: (2, 0), 9: (2, 1), 10: (2, 2), 11: (2, 3),
            12: (3, 0), 13: (3, 1), 14: (3, 2), 15: (3, 3)
        }

    #print("Node Assignment : \n", dict1)
    print("")


    def xy_routing(src,dest):
        if(src!=dest):
            s = list(dict1[src])
            d = list(dict1[dest])

            # print("Src Node cordinates = ", s, "\nDest Node = ", d)

            sx = s[0]
            sy = s[1]
            dx = d[0]
            dy = d[1]




            #print("Path\n")

            path = []

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
            # print("PATH:",path)
            hop_count = len(path)-1

            flag = 0
            data_generator = generate_data()
            t0_1,t1_0,t1_2,t2_1,t2_3,t3_2,t0_4,t4_0,t4_5,t5_4,t1_5,t5_1,t5_6,t6_5,t2_6,t6_2,t6_7,t7_6,t3_7,t7_3,t4_8,t8_4,t8_9,t9_8,t5_9,t9_5,t6_10,t10_6,t9_10,t10_9,t7_11,t11_7,t11_10,t10_11,t12_13,t13_12,t8_12,t12_8,t9_13,t13_9,t10_14,t14_10,t13_14,t14_13,t14_15,t15_14,t11_15,t15_11 = next(data_generator)


            # Calculate total delay

            for i in range(len(path) - 1):
                x1, y1 = path[i]
                x2, y2 = path[i + 1]
                node1 = nodes[x1][y1]
                node2 = nodes[x2][y2]
                # data_generator = traffic_generation.generate_data()
            

                #packet_bits=int(input("Enter packets(in bits):"))
                
                #print(t0_1)
                tf_link=eval(f"t{node1}_{node2}") #value
                #print(f"The amount of traffic genarated randomly in the link is : { tf_link}")
                tf_link_bits=math.floor(math.log2(tf_link)) #traffic generated randomly in bits
                #print(f"The Current traffic in the link ( in terms of bits) : {tf_link_bits}")
                # available_bit_space=64-tf_link_bits

                
                # #print(f"The path is taken from node  {node1}  to node {node2}")
                # print(f"The traffic present in path i,e node {node1} and node {node2} is {tf_link_bits}")
                # print(f"The available space between node {node1} and node {node2} in bits is {available_bit_space}")
                
                available_bit_space = available(node1, node2,tf_link_bits)
                if(n<=available_bit_space):
                    # print("Required space is available in the link and the data is sent  ")
                    # print("")
                    # print("-"*60)
                    final_path.append(node2)
                    # print("")
                    pass
                else:
                    data_generator = generate_data()
                    t0_1,t1_0,t1_2,t2_1,t2_3,t3_2,t0_4,t4_0,t4_5,t5_4,t1_5,t5_1,t5_6,t6_5,t2_6,t6_2,t6_7,t7_6,t3_7,t7_3,t4_8,t8_4,t8_9,t9_8,t5_9,t9_5,t6_10,t10_6,t9_10,t10_9,t7_11,t11_7,t11_10,t10_11,t12_13,t13_12,t8_12,t12_8,t9_13,t13_9,t10_14,t14_10,t13_14,t14_13,t14_15,t15_14,t11_15,t15_11 = next(data_generator)
                    tf_link=eval(f"t{node1}_{node2}") 
                    tf_link_bits=math.floor(math.log2(tf_link))
                    # print("before")
                    # available_bit_space = available(node1,node2,tf_link_bits)
                    # print("after")
                    global wait
                    wait += 1
                    
                    xy_routing(node1,node2)

    xy_routing(src,dest)
    # print("FINAL PATH:",final_path)
    # print("")


    # print(f"WAIT DELAY : {wait} Cycles")


    delay = len(final_path)-1
    total_delay = delay + wait
    # print(f"FINAL DELAY : {total_delay} Cycles")

    totaldelay_list.append(total_delay)
    hopcount_list.append(6)
    # print(totaldelay_list)
    # print(hopcount_list)
    testingdata = pd.DataFrame({"Hop Count":hopcount_list, "Total Delay":totaldelay_list})

testingdata.to_csv("TESTING/testfiles/RANDOM_TRAFFIC/DYNAMIC_XY/0_to_15_bitsize_5.csv")