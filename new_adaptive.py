import main
import dijkstra
import virtual_channel

def adaptive_route(src,dest):

    dict1 = {
        0: (0, 0), 1: (0, 1), 2: (0, 2), 3: (0, 3),
        4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (1, 3),
        8: (2, 0), 9: (2, 1), 10: (2, 2), 11: (2, 3),
        12: (3, 0), 13: (3, 1), 14: (3, 2), 15: (3, 3)
    }

    blocked_node = main.node1
    print("blocked_node is ",blocked_node)
    print("neighboring nodes are: ", main.value)

    adj = main.value
    traffic_prediction = []
    for i in adj:
        print("in new adaptive")
        coordinate = dict1[i]
        print(main.available(main.node1,i))
        if main.available_bit_space >= main.n:
            traffic_prediction.append(1)
        else:
            traffic_prediction.append(0)
    print("traffic prediction list= ",traffic_prediction)

    count_1 = 0
    count_0 = 0
    for i in traffic_prediction:
        if traffic_prediction[i] == 1:
            count_1 += 1
        elif traffic_prediction[i] == 0:
            count_0 +=1



    traffic_prediction = [1,0]
    allow = []
    for j in range(len(adj)):
        if adj[j]*traffic_prediction[j] != 0:
            # print("adj[j] : ",adj[j])
            # print("traffic_prediction[j] : ",traffic_prediction[j])
            allow.append(adj[j]*traffic_prediction[j])

    print("allow ", allow)
    # if count_1 <= len(traffic_prediction):
    #     dijkstra.print_paths(main.node1, main.dest, allow)

    if len(allow) !=0:
        next_node = dijkstra.print_paths(main.node1, main.dest, allow)
        allow =[]
        while next_node != main.dest:
            adaptive_route(next_node, main.dest)
    else:
        virtual_channel.create_virtual_channel()
    # elif count_0 == len(traffic_prediction):
    #     vc()


            


