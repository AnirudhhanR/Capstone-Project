# import numpy as np
# import math
# import main
# import dijkstra
# import final_traffic
# import adaptive

def create_virtual_channel():
    print("inside virtual channel")
    virtual_control=[0,0,0,0]                # virtual nodes 5,6,9,10
    virtual_connections = {5:[0,2,8,10],
                        6:[1,3,9,11],
                        9:[4,6,12,14],
                        10:[5,7,13,15]
                        }

    deadlock_node = 3      # adaptive.deadlock_node shld be pulled from adaptive file

    for key,value in virtual_connections.items():
        for i in range(len(value)):
            if deadlock_node == value[i]:
                virtual_channel = key
                print(key)
                break













