import pygame, random



WIDTH = 600
HEIGTH = 600

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGTH))

verde = (0,255,0)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()



    pygame.display.update()