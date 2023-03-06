import numpy as np

infinity = 100000000000

vertex_list = ["A", "B", "C", "D", "E", "F"]

adjacency_matrix = np.array([[0, 0, 0, 0, 5, 0], 
                             [0, 0, 0, 0, 5, 0],
                             [0, 2, 0, 0, 0, 0], 
                             [0, 7, 2, 0, 0, 0], 
                             [5, 0, 2, 2, 0, 5],
                             [5, 0, 0, 0, 0, 0]])

startingNode = 0
endingNode = 4

Q = [0, 1, 2, 3, 4, 5]
S = []

dist = [infinity, 0, infinity, infinity, infinity, infinity]

while not len(Q) == 0: # while Q is not empty
    shortest_distance = infinity
    current_node = 0

    for i in Q: # find shortest distance away node
        if dist[i] < shortest_distance:
            shortest_distance = dist[i]
            current_node = i

    S.append(current_node) # add node to traversed nodes
    Q.remove(current_node) # remove node from leftover nodes

    neighbors = []
    for i in range(len(adjacency_matrix)): # calculate all neighbors of current node
        dst = adjacency_matrix[i][current_node]
        if not dst == 0:
            neighbors.append(i)

    print(f"Neighbors of {vertex_list[current_node]}: {neighbors}")
    
    for v in neighbors: # if any new shortest path is discovered, that path is selected
        if dist[v] > dist[current_node] + adjacency_matrix[v][current_node]: 
            dist[v] = dist[current_node] + adjacency_matrix[v][current_node]

print(dist)
