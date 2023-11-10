# import numpy as np
# import math
# import main
# import dijkstra
# import final_traffic
# import adaptive

flag=0 
def request():
    global flag
    print("")
    print("Request for acknowledgement of virtual channel,therefore the flag value is "+str(flag))
    #if flag==0, noone has requested for virtual channel, else if flag ==1 virtual channel has been requested by another user
    if(flag != 0):
        return 0
    flag=1
    return flag

def create_virtual_channel(blocked_node,dest):
    #print(str(blocked_node)+" is requesting for virtual channel and therefore flag value is"+str(flag))
    virtual_control=[0,0,0,0]                # virtual nodes 5,6,9,10
    virtual_connections = {5:[0,2,8,10],
                        6:[1,3,9,11],
                        9:[4,6,12,14],
                        10:[5,7,13,15]
                        }

    deadlock_node = blocked_node
      # adaptive.deadlock_node shld be pulled from adaptive file
    virtual_length = 1.4
    link_length = 1
    minimum_length = []
    
    dict1 = {
        0: (0, 0), 1: (0, 1), 2: (0, 2), 3: (0, 3),
        4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (1, 3),
        8: (2, 0), 9: (2, 1), 10: (2, 2), 11: (2, 3),
        12: (3, 0), 13: (3, 1), 14: (3, 2), 15: (3, 3)
    }
    next_virtual_node  = 0
    key_list = []
    for key,value in virtual_connections.items():
        key_list.append(key)
    

    for key,value in virtual_connections.items():
        
        if(deadlock_node not in key_list):
            
            for i in range(len(value)):
                if deadlock_node == value[i]:
                    next_virtual_node = key
                    
                    
                    break
        elif(deadlock_node == key):
            #print("entered elif")
            for i in range(len(value)):
                
                s = dict1[value[i]]
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
                
                minimum_length.append(len(path)-1)
            
            next_node_length = min(minimum_length)
            
            index_next = minimum_length.index(next_node_length)
            
            next_virtual_node = value[index_next]
            
                
        
    print("NEAREST VIRTUAL NODE : ",next_virtual_node)
    global flag
    
    print("Flag",flag)
    flag=0
    return next_virtual_node
    
    

#create_virtual_channel(1,15)






    # global flag
    # print("virtual channel",virtual_channel)
    # print("flag",flag)
    # flag=0
    # return virtual_channel
def delay_vc(current_node,dest):
    dict1 = {
        0: (0, 0), 1: (0, 1), 2: (0, 2), 3: (0, 3),
        4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (1, 3),
        8: (2, 0), 9: (2, 1), 10: (2, 2), 11: (2, 3),
        12: (3, 0), 13: (3, 1), 14: (3, 2), 15: (3, 3)
    }
    s = dict1[current_node]
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
    delay = 1.4 + (len(path)- 1)
    return delay

#create_virtual_channel(5,12)












