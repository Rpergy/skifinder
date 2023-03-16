import pygame
import math
import json

pygame.init()

display_width = 568
display_height = 635
infinity = 9223372036854775807

def dijkstras(start, end, adjacency_matrix):
    verticies = []
    dist = []
    prev = []

    for i in range(len(adjacency_matrix)):
        dist.append(infinity)
        prev.append(None)
        verticies.append(i)
    dist[start] = 0

    while not len(verticies) == 0:
        minDist = infinity # vertex in Q with min distance
        u = 0
        for i in range(len(dist)):
            if dist[i] < minDist and i in verticies:
                minDist = dist[i]
                u = i

        if u == end: # if found target, work backwards to reconstruct path
            path = []
            u = end
            if not prev[u] == None or u == start:
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

    return path

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Map Editor')

clock = pygame.time.Clock()

def main():
    img = pygame.image.load('Maps/Loon.png')

    data = json.loads(open("mountains.json", "r").read())
    adjacency_table = data["Loon"]["adjacency_table"]
    verticies = data["Loon"]["verticies"]
    edges = data["Loon"]["edges"]
    important_verticies = data["Loon"]["important_verticies"]

    path = []

    font = pygame.font.Font("freesansbold.ttf", 20)

    startVertex = -1
    endVertex = -1

    debugLines = False
    debugText = False
    debugVerticies = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    debugLines = not debugLines
                if event.key == pygame.K_t:
                    debugText = not debugText
                if event.key == pygame.K_v:
                    debugVerticies = not debugVerticies
                if event.key == pygame.K_ESCAPE:
                    startVertex = -1
                    endVertex = -1
                    path = []
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mousePos = pygame.mouse.get_pos()
                    for i in range(len(verticies)):
                        distance = math.sqrt(pow(verticies[i][0] - mousePos[0], 2) + pow(verticies[i][1] - mousePos[1], 2))
                        if distance < 10 and (i in important_verticies or debugVerticies):
                            if startVertex == -1:
                                startVertex = i
                            else:
                                endVertex = i
                                print(f"Start Vertex: {startVertex}, End Vertex: {endVertex}")

                                path = dijkstras(startVertex, endVertex, adjacency_table)
                                print(path)
        
        gameDisplay.fill((44,64,49))
        gameDisplay.blit(img, (0, 0))

        for i in edges:
            startPoint = i[1]
            endPoint = i[2]

            if debugLines:
                for j in range(len(i[0]) - 1):
                    pygame.draw.line(gameDisplay, (0, 0, 0), i[0][j], i[0][j + 1], 3)

            for ii in range(len(path) - 1):
                start = path[ii]
                end = path[ii + 1]

                if startPoint == start and endPoint == end:
                    for j in range(len(i[0]) - 1):
                        pygame.draw.line(gameDisplay, (0, 255, 0), i[0][j], i[0][j + 1], 3)

        for i in range(len(verticies)): # draw verticies
            if i in important_verticies or debugVerticies:
                if i == startVertex or i == endVertex:
                    pygame.draw.circle(gameDisplay, (0, 255, 0), verticies[i], 10)
                else:
                    pygame.draw.circle(gameDisplay, (255, 0, 0), verticies[i], 10)
                if debugText:
                    text = font.render(str(i), True, (255, 255, 255))
                    textRect = text.get_rect()
                    textRect.center = verticies[i]
                    gameDisplay.blit(text, textRect)

        pygame.display.update()
        clock.tick(60)

main()
pygame.quit()
quit()
