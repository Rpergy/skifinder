import pygame
import math

pygame.init()

display_width = 1501
display_height = 757

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Map Editor')

clock = pygame.time.Clock()
img = pygame.image.load('Resources/map.png')

verticies = []
edges = []

def main():
    showImg = True

    edgeLines = []
    currentEdge = []
    edgeStart = None

    font = pygame.font.Font("freesansbold.ttf", 20)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # Cancel Floating Line
                    currentEdge = []
                    edgeStart = None
                if event.key == pygame.K_s: # Show/Hide Map
                    showImg = not showImg
                if event.key == pygame.K_u: # Undo
                    verticies.pop(-1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    verticies.append(mousePos)
                if event.button == 3:
                    check = False
                    for i in range(len(verticies)):
                        distance = math.sqrt(pow(mousePos[0] - verticies[i][0], 2) + pow(mousePos[1] - verticies[i][1], 2))
                        if distance < 10: # If clicked on vertex
                            if len(currentEdge) == 0: # Start an edge
                                edgeStart = i
                                print(f"started edge at {edgeStart}")

                                currentEdge.append(mousePos)

                                check = True
                                break
                            else: # If floating line already exists (place edge)
                                print(f"finished edge at {i}")
                                currentEdge.append(mousePos)

                                length = 0
                                for j in range(len(currentEdge) - 1):
                                    firstPoint = currentEdge[j]
                                    secondPoint = currentEdge[j + 1]
                                    length += math.sqrt(pow(firstPoint[0] - secondPoint[0], 2) + pow(firstPoint[1] - secondPoint[1], 2))

                                edges.append((edgeStart, i, length))
                                edgeLines += [currentEdge]
                                #print(edgeLines)
                                currentEdge = []

                                check = True
                                break
                    if not len(currentEdge) == 0 and not check: 
                            print("selected intermediate")
                            currentEdge.append(mousePos)

        gameDisplay.fill((255,255,255))
        if showImg: gameDisplay.blit(img, (0,0))

        mousePos = pygame.mouse.get_pos()
        pygame.draw.circle(gameDisplay, (255, 0, 0), mousePos, 10)

        for i in edgeLines: # draw edges
            for j in range(len(i) - 1):
                pygame.draw.line(gameDisplay, (0, 0, 0), i[j], i[j + 1], 3)
        
        if len(currentEdge) > 0:
            for i in range(len(currentEdge) - 1): # draw edges being made
                pygame.draw.line(gameDisplay, (0, 0, 255), currentEdge[i], currentEdge[i + 1], 3)
            pygame.draw.line(gameDisplay, (0, 0, 255), currentEdge[-1], mousePos, 3)

        for i in range(len(verticies)): # draw verticies
            pygame.draw.circle(gameDisplay, (255, 0, 0), verticies[i], 10)

            text = font.render(str(i), True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = verticies[i]

            gameDisplay.blit(text, textRect)

        pygame.display.update()
        clock.tick(60)

main()
pygame.quit()

print(f"Edges: {edges}")

# build adjacency tables out of edges and verticies lists
adjacency_table = [[0 for x in range(len(verticies))] for y in range(len(verticies))]

for i in edges:
    adjacency_table[i[1]][i[0]] = int(i[2])

print(adjacency_table)

quit()
