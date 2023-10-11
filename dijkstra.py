
import main
adj = main.value


def is_valid(node):
    return 0 <= node < 16

def find_paths(graph, src, dest, path, paths):
    if src == dest:
        paths.append(path[:])
        return

    for neighbor in graph[src]:
        if neighbor not in path:
            path.append(neighbor)
            find_paths(graph, neighbor, dest, path, paths)
            path.pop()

def print_paths(src, dest):
    graph = {
        0: [1,4],
        1: [0, 2, 5],
        2: [1, 3, 6],
        3: [2, 7],
        4: [0, 5, 8],
        5: [1, 4, 6, 9],
        6: [2, 5, 7, 10],
        7: [3, 6, 11],
        8: [4, 9, 12],
        9: [5, 8, 10, 13],
        10: [6, 9, 11, 14],
        11: [7, 10, 15],
        12: [8, 13],
        13: [9, 12, 14],
        14: [10, 13, 15],
        15: [11, 14]
    }


    paths = []
    find_paths(graph, src, dest, [src], paths)

    paths.sort(key=len)
    print(paths)

    
    hoplist=[]
    for i in paths:
        if i[2] == adj[i]:
            hoplist.append(i)

    print(hoplist)
    print('hoplist=',hoplist)
    
    for path in paths:
        print(" -> ".join(map(str, path)))
    

if __name__ == "__main__":
    source = int(input("Enter the source node : ")) 
    destination = int(input( "Enter the destination node :"))

    print("All paths from source to destination using DIJKSTRA Algorithm :")
    print_paths(source, destination)

