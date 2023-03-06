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

verticies = [0, 1, 2, 3, 4, 5]
dist_table = adjacency_matrix[:]

for i in range(len(verticies)):
    connections = dijkstras.dijkstras(verticies, adjacency_matrix, i)
    for ii in range(len(connections)):
        dist_table[i][ii] = connections[ii]

print(dist_table)
