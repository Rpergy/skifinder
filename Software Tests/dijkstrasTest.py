"""
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
"""

infinity = 9223372036854775807

startingNode = 11
target = 9

adjacency_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 415, 0, 0, 0], [33, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [41, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 91, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 30, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 60, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 56, 29, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 49, 0, 0, 0, 0, 0], [0, 0, 0, 337, 0, 433, 0, 183, 0, 215, 0, 95], [0, 0, 304, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 178, 0, 0], [0, 0, 0, 0, 0, 0, 0, 81, 0, 0, 0, 0]]

verticies = []
dist = []
prev = []

for i in range(len(adjacency_matrix)):
    dist.append(infinity)
    prev.append(None)
    verticies.append(i)
dist[startingNode] = 0

while not len(verticies) == 0:
    minDist = infinity # vertex in Q with min distance
    u = 0
    for i in range(len(dist)):
        if dist[i] < minDist and i in verticies:
            minDist = dist[i]
            u = i
    
    if u == target: # if found target, work backwards to reconstruct path
        path = []
        u = target
        if not prev[u] == None or u == startingNode:
            while not u == None:
                path.insert(0, u)
                u = prev[u]
        break

    verticies.remove(u)

    neighbors = [] # calculate all neighbors of current node
    for i in range(len(adjacency_matrix)):
            dst = adjacency_matrix[i][u]
            if not dst == 0:
                neighbors.append(i)

    for n in neighbors:
        if n in verticies:
            alt = dist[u] + adjacency_matrix[n][u]
            if alt < dist[n]:
                dist[n] = alt
                prev[n] = u

print(path)
