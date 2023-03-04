import numpy as np

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
print(f"Available Nodes from {vertex_list[4]}: {available_nodes}")