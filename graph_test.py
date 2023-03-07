import numpy as np
import dijkstras

vertex_list = np.array(["A", "B", "C", "D", "E", "F"])

adjacency_matrix = np.array([[0, 0, 0, 0, 5, 0], 
                             [0, 0, 0, 0, 5, 0],
                             [0, 2, 0, 0, 0, 0], 
                             [0, 7, 2, 0, 0, 0], 
                             [5, 0, 2, 2, 0, 5],
                             [5, 0, 0, 0, 0, 0]])

# weight lookup
firstNode = 5
secondNode = 0
print(f"Connection: {vertex_list[firstNode]} to {vertex_list[secondNode]}\nConnection Length: {adjacency_matrix[secondNode][firstNode]}\n")

# possible traversals
node = 4
available_nodes = []
for i in range(len(adjacency_matrix)):
    if not adjacency_matrix[i][node] == 0:
        available_nodes.append(vertex_list[i])
print(f"Available Nodes from {vertex_list[4]}: {available_nodes}\n")

# shortest distance
current_node = 0
shortest_distance = 100000
shortest_distance_node = 0

for selectedNode in range(len(adjacency_matrix)):
    dst = adjacency_matrix[selectedNode][current_node]

    if not dst == 0:
        if dst < shortest_distance:
            shortest_distance = dst
            shortest_distance_node = selectedNode

print(f"Shortest distance node from {vertex_list[current_node]}: {vertex_list[shortest_distance_node]}")

# create a table of all shortest distances, using dijkstras algorithm

adjacency_matrix = [[  0,   0,  0,  0,   0,  0, 0,  0,   0,   0,   0,  0, 303,   0,  0,  0,   0,  0, 0,  0], 
                    [ 77,   0,  0,  0,   0,  0, 0,  0,   0,   0,   0,  0,   0,   0,  0,  0,   0,  0, 0,  0], 
                    [  0,   0,  0, 94,   0,  0, 0,  0,   0,   0,   0,  0,   0,   0,  0,  0,   0,  0, 0,  0], 
                    [  0,  69,  0,  0,   0,  0, 0,  0,   0,   0,   0,  0,   0,   0,  0,  0,   0,  0, 0,  0], 
                    [  0,   0, 91,  0,   0,  0, 0,  0,   0,   0,   0,  0,   0,   0,  0,  0,   0,  0, 0,  0], 
                    [  0,   0,  0,  0, 275,  0, 0,  0, 212,   0,   0,  0,   0,   0,  0,  0,   0,  0, 0,  0], 
                    [  0,   0,  0,  0,   0, 52, 0,  0,   0,   0,   0, 53, 137,   0,  0,  0,   0,  0, 0, 97], 
                    [  0,  82,  0, 64,   0,  0, 0,  0,   0,   0,   0,  0,   0,   0,  0,  0,   0,  0, 0,  0], 
                    [  0,   0,  0,  0,   0,  0, 0, 57,   0,   0,   0,  0,   0,   0,  0,  0,   0,  0, 0,  0], 
                    [164,   0,  0,  0,   0,  0, 0,  0,   0,   0,   0,  0,   0,   0,  0,  0,   0,  0, 0,  0], 
                    [  0, 190,  0,  0,   0,  0, 0,  0,   0,   0,   0,  0,   0,   0,  0,  0,   0,  0, 0,  0], 
                    [  0,   0,  0,  0,   0,  0, 0,  0,   0,   0, 173,  0,   0,   0,  0,  0,   0,  0, 0,  0], 
                    [  0,   0,  0,  0,   0,  0, 0,  0, 116,   0,   0,  0,   0,   0,  0,  0,   0,  0, 0,  0], 
                    [123,   0,  0,  0,   0,  0, 0,  0,   0,   0,   0,  0,   0,   0,  0,  0,   0,  0, 0,  0], 
                    [  0,   0,  0,  0,   0,  0, 0,  0,   0,   0,   0,  0,   0, 153,  0,  0,   0,  0, 0,  0], 
                    [  0,   0,  0,  0,   0,  0, 0,  0,   0, 174,   0,  0,   0,   0, 60,  0,   0,  0, 0,  0], 
                    [  0,   0,  0,  0,   0,  0, 0,  0,   0,   0,   0,  0,   0,   0,  0, 68,   0,  0, 0,  0], 
                    [  0,   0,  0,  0,   0,  0, 0,  0,   0,   0,   0,  0,   0,   0,  0,  0, 104,  0, 0,  0], 
                    [  0,   0,  0,  0,   0,  0, 0,  0,   0,   0,   0,  0,   0,   0,  0,  0,   0, 74, 0,  0], 
                    [  0,   0,  0,  0,   0,  0, 0,  0,   0,   0,   0,  0,   0,   0,  0, 92,   0,  0, 0,  0]]

verticies = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
dist_table = adjacency_matrix[:]

for i in range(len(verticies)):
    connections = dijkstras.dijkstras(verticies, adjacency_matrix, i)
    for ii in range(len(connections)):
        dist_table[i][ii] = connections[ii]

print(dist_table)
