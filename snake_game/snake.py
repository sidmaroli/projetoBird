import pygame
import random


WIDTH = 700
HEIGTH = 400

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGTH))


white = (225,225,225)
green = (0,128,0)
blue = (0,0,225)
red = (225,0,0)
black = (0,0,0)


snake_block = 10
tickt = 13

clock = pygame.time.Clock()
snake_speed = 10


game_over = False
game_close = False

x1_change = 0
y1_change = 0

x1 = WIDTH/2
y1 = HEIGTH/2

foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, HEIGTH - snake_block) / 10.0) * 10.0

while not game_over:

    while game_close == True:
        screen.fill(white)
        pygame.display.update()
 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block 
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0


    x1 += x1_change
    y1 += y1_change
    screen.fill(white)

    pygame.draw.rect(screen, red,[foodx, foody, snake_block, snake_block])
    pygame.draw.rect(screen, green,[x1, y1, snake_block, snake_block])

    clock.tick(tickt)
 
    pygame.display.update()        

