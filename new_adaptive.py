import main
import dijkstra
import virtual_channel

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
        #print(main.available(main.node1,i))
        available_bit_space = main.available(src,i)
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
            count_0 +=1



    #traffic_prediction = [1,0]
    allow_adj = []
    for j in range(len(adj)):
        if adj[j]*traffic_prediction[j] != 0:
            # print("adj[j] : ",adj[j])
            # print("traffic_prediction[j] : ",traffic_prediction[j])
            allow_adj.append(adj[j]*traffic_prediction[j])

    print("allow_adj ", allow_adj)
    # if count_1 <= len(traffic_prediction):
    #     dijkstra.print_paths(main.node1, main.dest, allow_adj)

    if len(allow_adj) !=0:
        next_node = dijkstra.print_paths(src, dest, allow_adj)
        allow_adj.clear()
        traffic_prediction.clear()
        #print("new next node",next_node)
        print("allow_adj : empty",allow_adj)
        while next_node != dest:
             #adaptive_route(next_node, main.dest)
             # main.xy_main(next_node, main.dest,main.n)
             print("hello")
    else:
        virtual_channel.create_virtual_channel()
    # elif count_0 == len(traffic_prediction):
    #     vc()


            


