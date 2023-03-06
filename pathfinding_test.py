import numpy as np
import dijkstras

infinity = 100000000000

vertex_list = ["A", "B", "C", "D", "E", "F"]

verticies = [0, 1, 2, 3, 4, 5]

adjacency_matrix = [[0, 0, 0, 0, 5, 0], 
                    [0, 0, 0, 0, 5, 0],
                    [0, 2, 0, 0, 0, 0], 
                    [0, 7, 2, 0, 0, 0], 
                    [5, 0, 2, 2, 0, 5],
                    [5, 0, 0, 0, 0, 0]]

distance_table = [[ 0, 10, 12, 14,  5,  5],
                  [ 9,  0,  2,  4,  4, 14],
                  [ 7,  2,  0,  2,  2, 12],
                  [ 7,  4,  2,  0,  2, 12],
                  [ 5,  4,  2,  2,  0, 10],
                  [ 5, 14, 12, 12, 10,  0]]

startingNode = 0
targetNode = 3

path = [startingNode]

Q = [0, 1, 2, 3, 4, 5]

currentNode = startingNode

while not len(Q) == 0:
    Q.remove(currentNode)

    neighbors = []
    for i in range(len(adjacency_matrix)): # calculate all neighbors of current node
        dst = adjacency_matrix[i][currentNode]
        if not dst == 0:
            neighbors.append(i)

    currentNode = None
    lowestCost = 10000000000000

    #print(f"All neighbors: {neighbors}")

    for n in neighbors: # for each neighbor node, we need to calculate the cost relative to the parent node
        G = distance_table[n][startingNode] # distance from current node to starting node
        H = distance_table[n][targetNode] # distance from current node to target node
        F = H + G # cost
        #print(f"Cost of node {n}: {F}")
        if F < lowestCost and n in Q:
            currentNode = n
            lowestCost = F
    
    if currentNode == targetNode:
        path.append(currentNode)
        break

    path.append(currentNode)

print(path)
