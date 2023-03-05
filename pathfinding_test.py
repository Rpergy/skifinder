import numpy as np

infinite = 100000000000

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

dist = [infinite, 0, infinite, infinite, infinite, infinite]

while not len(Q) == 0: # while Q is not empty
    shortest_distance = infinite
    shortest_node = 0

    for i in Q: # find shortest distance away node
        if dist[i] < shortest_distance:
            shortest_distance = dist[i]
            shortest_node = i

    S.append(shortest_node) # add node to traversed nodes
    Q.remove(shortest_node) # remove node from leftover nodes

    neighbors = [] 
    for i in range(len(adjacency_matrix)): # calculate all neighbors of current node
        dst = adjacency_matrix[i][shortest_node]
        if not dst == 0:
            neighbors.append(i)
    
    for v in neighbors: # if any new shortest path is discovered, that path is selected
        if dist[v] > dist[shortest_node] + adjacency_matrix[v][shortest_node]:
            dist[v] = dist[shortest_node] + adjacency_matrix[v][shortest_node]
    

print(dist)
