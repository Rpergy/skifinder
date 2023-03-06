def dijkstras(vertex_list, adjacency_matrix, startingNodeIndex):
    infinity = 1000000000

    Q = vertex_list[:]
    S = []
    dist = []

    for i in range(len(Q)):
        if i == startingNodeIndex:
            dist.append(0)
        else:
            dist.append(infinity)

    while not len(Q) == 0: # while Q is not empty
        shortest_distance = infinity
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

    return dist
