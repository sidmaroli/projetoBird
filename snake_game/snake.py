import pygame, random





WIDTH = 800
HEIGTH = 400

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGTH))

verde = (0,255,0)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()



    pygame.display.update()