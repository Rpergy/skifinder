import pygame
import math

pygame.init()

display_width = 852
display_height = 721

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Map Editor')

clock = pygame.time.Clock()

verticies = []
edges = []

def main():
    display_width = 852
    display_height = 721

    display_scale = 1.0

    showImg = True

    img = pygame.image.load('Resources/googleEarthTest.png')
    originalImg = pygame.image.load('Resources/googleEarthTest.png')

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
                
                if event.key == pygame.K_q: # zoom in
                    display_scale += 0.05
                    img = pygame.transform.smoothscale(originalImg, (display_width * display_scale, display_height * display_scale))
                if event.key == pygame.K_e: # zoom out
                    display_scale -= 0.05
                    img = pygame.transform.smoothscale(originalImg, (display_width * display_scale, display_height * display_scale))
                
                if event.key == pygame.K_u: # Undo
                    verticies.pop(-1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    verticies.append((mousePos[0]/display_scale, mousePos[1]/display_scale))
                    print(f"Added vertex at: {(mousePos[0]/display_scale, mousePos[1]/display_scale)}")
                if event.button == 3:
                    check = False
                    for i in range(len(verticies)):
                        scaledMousePos = (mousePos[0]*display_scale, mousePos[1]*display_scale)
                        scaledVerticies = (verticies[i][0]*display_scale, verticies[i][1]*display_scale)
 
                        distance = math.sqrt(pow(scaledMousePos[0] - scaledVerticies[0], 2) + pow(scaledMousePos[1] - scaledVerticies[1], 2))

                        print(distance)

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
                scaledPos1 = (i[j][0]*display_scale, i[j][1]*display_scale)
                scaledPos2 = (i[j + 1][0]*display_scale, i[j + 1][1]*display_scale)

                pygame.draw.line(gameDisplay, (0, 0, 0), scaledPos1, scaledPos2, 3)
        
        if len(currentEdge) > 0: # draw edges being currently made
            for i in range(len(currentEdge) - 1): 
                scaledPos1 = (currentEdge[i][0]*display_scale, currentEdge[i][1]*display_scale)
                scaledPos2 = (currentEdge[i + 1][0]*display_scale, currentEdge[i + 1][1]*display_scale)

                pygame.draw.line(gameDisplay, (0, 0, 255), scaledPos1, scaledPos2, 3)
            
            scaledPos = (currentEdge[-1][0]*display_scale, currentEdge[-1][1]*display_scale)
            scaledMousePos = (mousePos[0]*display_scale, mousePos[1]*display_scale)

            pygame.draw.line(gameDisplay, (0, 0, 255), scaledPos, scaledMousePos, 3)

        for i in range(len(verticies)): # draw verticies
            scaledPos = (verticies[i][0]*display_scale, verticies[i][1]*display_scale)
            pygame.draw.circle(gameDisplay, (255, 0, 0), scaledPos, 10)

            text = font.render(str(i), True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = scaledPos

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
