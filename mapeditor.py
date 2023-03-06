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
    floatingLine = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    floatingLine = None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    verticies.append(mousePos)
                if event.button == 3:
                    if floatingLine == None:
                        for i in range(len(verticies)):
                            distance = math.sqrt(pow(mousePos[0] - verticies[i][0], 2) + pow(mousePos[1] - verticies[i][1], 2))
                            if distance < 10:
                                print("selected vertex")
                                floatingLine = i
                                break
                    else:
                        for i in range(len(verticies)):
                            distance = math.sqrt(pow(mousePos[0] - verticies[i][0], 2) + pow(mousePos[1] - verticies[i][1], 2))
                            if distance < 10:
                                length = math.sqrt(pow(verticies[floatingLine][0] - verticies[i][0], 2) + pow(verticies[floatingLine][1] - verticies[i][1], 2))
                                edges.append((floatingLine, i, length))
                                floatingLine = None
                                break

        gameDisplay.fill((255,255,255))
        gameDisplay.blit(img, (0,0))

        mousePos = pygame.mouse.get_pos()
        pygame.draw.circle(gameDisplay, (255, 0, 0), mousePos, 10)

        for i in verticies:
            pygame.draw.circle(gameDisplay, (255, 0, 0), i, 10)
        
        for i in edges:
            pygame.draw.line(gameDisplay, (0, 0, 0), verticies[i[0]], verticies[i[1]], width=3)

        if not floatingLine == None:
            pygame.draw.line(gameDisplay, (0, 0, 0), verticies[floatingLine], mousePos, width=3)

        pygame.display.update()
        clock.tick(60)

main()
pygame.quit()

# build adjacency tables out of edges and verticies lists
adjacency_table = [[0 for x in range(len(verticies))] for y in range(len(verticies))]

for i in edges:
    adjacency_table[i[1]][i[0]] = int(i[2])

print(adjacency_table)

quit()
"""

[[  0,   0,   0, 134, 0], 
 [ 83,   0,   0,   0, 0], 
 [176,   0,   0,   0, 0], 
 [134,   0, 240,   0, 0], 
 [  0, 109,   0,  69, 0]]

"""